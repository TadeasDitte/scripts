sudo pacman -Sy nextcloud-client qpwgraph git github-desktop dpkg firefox lynis steam wine protontricks qbittorrent tor torbrowser-launcher
# Caelesthia Dots
git clone https://github.com/caelestia-dots/caelestia.git ~/.local/share/caelestia
~/.local/share/caelestia/install.fish --noconfirm --spotify --discord --aur-helper=yay
# This one is obvious
yay -S visual-studio-code-bin --noconfirm
mkdir -p ~/Pictures/Wallpapers
mkdir -p ~/ISO
# Hardening script from a pookie of mine <3
git clone https://github.com/mokosak/linux-hardening.git
chmod +x ./linux-hardening/harden.sh
sudo ./linux-hardening/harden.sh
# Discord theme
wget -P .config/Equicord/themes/ https://raw.githubusercontent.com/refact0r/system24/refs/heads/main/theme/flavors/system24-tokyo-night.theme.css
