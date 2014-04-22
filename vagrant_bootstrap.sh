#!/bin/bash

# Install git for version control, pip for install python packages
/usr/bin/yes | sudo apt-get install git
/usr/bin/yes | sudo apt-get install python3-pip
/usr/bin/yes | sudo apt-get install python-pip
/usr/bin/yes | sudo apt-get install python-dev
/usr/bin/yes | sudo apt-get install python3-dev
/usr/bin/yes | sudo apt-get install postgresql
/usr/bin/yes | sudo apt-get install nginx

# Install Django + various other pip packages for Django
sudo pip install django
sudo pip install python-memcached
sudo pip install South
sudo pip install markdown
sudo pip install uwsgi

# Install Django + various other pip packages for Django
sudo pip3 install django
sudo pip3 install python-memcached
sudo pip3 install South
sudo pip3 install markdown
sudo pip3 install uwsgi