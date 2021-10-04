# Install miniconda using terminal

https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b

## Install miniconda

`wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh`
`sudo md5sum Miniconda3-latest-Linux-armv7l.sh # (optional) check md5`
`sudo /bin/bash Miniconda3-latest-Linux-armv7l.sh`

Change default directory to 
`/home/pi/miniconda3`
#open the bashrc or from the folder with text editor
`sudo nano /home/pi/.bashrc`
Add this line to any line in the file
`export PATH="/home/pi/miniconda3/bin:$PATH"`

## Install other python versions and create virtual environment

`conda install python=3.5`
`conda install python=3.6`

Afterwards I was able to create environments with the added Python version, e.g. with Python 3.5:
`conda create --name py35 python=3.5`

The new environment "py35" can now be activated:
`source activate py35`

Preview the markdown with Ctrl + Shift + V with extension