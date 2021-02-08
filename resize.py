"""
This scrip resizes all images in a directory and converts them to jpeg

input directory: large/
output directory: resized/

"""

import os
import glob
from PIL import Image
import sys

IN_FOLDER = 'large/'
OUT_FOLDER = 'resized/'

args = sys.argv
if len(args) > 3:
    print ("too many arguments")
    quit()

# if there are no arguments, default to jpg
format = "jpg" # default
if len(args) > 1:
    if args[1] not in ["png", "jpg", "jpeg", "tiff"]:
        print ("not requesting a supported file type. arguments must be in order [fileformat] [integer]")
        quit()
    format = args[1]

#resize all images to this width
width = 1200 # default
if len(args) > 2:
    arg2 = 0
    try:
        arg2 = int(sys.argv[2])
    except ValueError:
        print ("arguments must be in order [fileformat] [integer]")
        quit()
    width = arg2

for file in glob.glob(IN_FOLDER + '*'):
    file_base = os.path.basename(file)[:-4]
    file_format = os.path.basename(file)[-3:]
    if(file_format not in ["png", "jpg"]):
        print("this program only resizes png and jpg images")
        continue
    output_file = OUT_FOLDER + '/' + file_base + '.' + format
    print(file_base)

    #only resize if images are not already the output directory
    if not os.path.exists(output_file):
        print("resizing!")
        img = Image.open(file).convert('RGBA')
        icc_profile = img.info.get('icc_profile')
        w_percent = width/float(img.size[0])
        height = int(float(img.size[1])*float(w_percent))
        new_img = img.resize((width, height), Image.ANTIALIAS)
        new_img = new_img.convert('RGB')
        new_img.save(output_file, icc_profile=icc_profile, quality=95)
    else:
        print('already here, not resizing!')

print('yeeee we done!!')
