#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sun.09.12.2018 22:48      start code
mon.10.12.2018 01:10      working, converting

mission
  convert .rmvb to .mp4
how
  using ffmpeg in python
  loop files
  
guide > python ffmpeg
  https://stackoverflow.com/questions/42438380/ffmpeg-in-python-script
guide > ffmepg command in terminal
  https://stackoverflow.com/questions/50132902/how-to-convert-rmvb-to-mp4-with-same-quality-by-using-ffmpeg

env (any python 3 env)

sample command
  ffmpeg -i 002.rmvb -c:v h264 -c:a aac "002.mp4"

summary
  working
  but because the python code is in different directory to the .rmvb files
  i needed to code the full path manually

"""
import os

DIRECTORY = "<.rmvb files directory full path>"

for filename in os.listdir(DIRECTORY):
    if (filename.endswith(".rmvb")): 
        path_from = DIRECTORY + '/' + filename
        path_to = DIRECTORY + '/' + filename.replace('.rmvb', '.mp4')
        command = "ffmpeg -i {0} -c:v h264 -c:a aac '{1}'".format(path_from, path_to)
        print (command)
        os.system(command)
    else:
        continue
