# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 22:47:29 2022

@author: Vikanksh
"""

import argparse
 
parser = argparse.ArgumentParser(description="Segregate the folder files",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("--src", help="Complete Source Folder location")
# parser.add_argument("--dest", help="Destination folder location, if not given source loc used")
args = parser.parse_args()

config = vars(args)
print(config)

import os
import shutil
from glob import glob
import sys

input_folder = args.src

#dest same as input 
destination_folder = input_folder

#list of image paths
image_paths = glob(input_folder + '/*.tiff') + glob(input_folder + '/*.png') \
    + glob(input_folder + '/*.jpg')

#list of text paths
text_paths = glob(input_folder + '/*.txt') 

# print(image_files) #-> ['i/p folder/1.png', 'path2'...]

#creating the os path str for the folders
image_folder = os.path.join(input_folder, 'image_folder')
text_folder = os.path.join(input_folder, 'text_folder')


#set exist_ok True so that no error shown if path exists
os.makedirs(image_folder, exist_ok=True)
os.makedirs(text_folder, exist_ok=True)

#moving files
# input folder:
#     image folder
#     textfolder
for image in image_paths:
  shutil.move(image, os.path.join(image_folder, os.path.basename(image)))
for text in text_paths:
  shutil.move(text, os.path.join(text_folder, os.path.basename(text)))
