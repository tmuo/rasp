# Instructions how to install librealsense for Raspberry PI

Based on the video: https://www.youtube.com/watch?v=LBIBUntnxp8 (Raspberry Pi 4 + Intel's RealSense D435 Depth Camera Step-By-Step Installation)

## Step-by-steo

1.  ssh pi@XXX.XXX...
2.  sudo apt-get update && sudo apt-get dist-upgrade
3.  sudo raspi-config (Advanced Options -> Expand Filesystem)
4.  sudo nano /etc/dphys-swapfile (CONF_SWAPSIZE = 2048)
5.  sudo etc/init.d/dphys-swapfile restart swapon -s
6.  sudo apt-get install automake libtool vim cmake libusb-1.0.0-dev libx11-dev xorg-dev libglu1-mesa-dev
7.  mkdir REPO
8.  cd REPO
9.  git clone https://github.com/InterRealSense/librealsense.git
10. cd librealsense/
11. sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
12. sudo su
13. udevadm control --reload-rules && udevadm trigger
14. exit
