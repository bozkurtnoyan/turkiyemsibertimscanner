#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os

os.system("pkg install figlet -y")
os.system("pkg install python2 -y")
os.system("pkg install git -y")
os.system("git clone https://github.com/TechnicalMujeeb/TM-scanner")
os.system("bash TM-scanner/install.sh")
os.system("python2 TM-scanner/tmscanner.py")