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
15. vi ~/.bashrc
16. #add LD_LIBRARY_PATH environment variable -> export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH (to the end)
17. source ~/.bashrc
18. cd .. (to REPO)
19. git clone --depth=1 -b v3.10.0 https://github.com/google/protobuf.git
20. cd protobuf/
21. ./autogen.sh
22. make -j1
23. sudo make install 
24. cd python/
25. export LD_LIBRARY_PATH=../src/.libs
26. python3 setup.py build --cpp_implementation
27. sudo python3 setup.py install --cpp_implementation
28. export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
29. export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=3
30. sudo ldconfig
31. protoc --version (libprotoc 3.10.0)
32. cd ../.. (to REPO)
