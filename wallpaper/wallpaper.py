import requests
from bs4 import BeautifulSoup
import os

wallpaper_directory = "/home/user/Pictures/Wallpapers"  ### ADDITIONAL CONFIG NEEDED
src_site = "https://wallhaven.cc/user/user/favorites/randomnumber" ### the same as above on user and random number [your public collection]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': 'https://wallhaven.cc/'
}

response = requests.get(src_site, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

wp_list = []
for wp in soup.find_all('figure'):
    wp_list.append(wp.get('data-wallpaper-id'))

print(f"Found {len(wp_list)} wallpapers")

download_format = "https://wallhaven.cc/w/"

os.makedirs(wallpaper_directory, exist_ok=True)

for id in wp_list:
    url = download_format + id
    print(f"Processing: {url}")
    
    url_response = requests.get(url, headers=headers)
    url_text = url_response.text
    soup = BeautifulSoup(url_text, 'html.parser')
    
    wallpaper_img = soup.find('img', {'id': 'wallpaper'})
    
    if wallpaper_img and wallpaper_img.get('src'):
        img_url = wallpaper_img['src']
        print(f"Downloading: {img_url}")
        
        img_response = requests.get(img_url, headers=headers, stream=True)
        
        if img_response.status_code == 200:
            filename = os.path.join(wallpaper_directory, f"{id}.{img_url.split('.')[-1]}")
            with open(filename, 'wb') as f:
                for chunk in img_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Saved: {filename}")
        else:
            print(f"Failed to download: {img_response.status_code}")
    else:
        print(f"Could not find wallpaper image for ID: {id}")
