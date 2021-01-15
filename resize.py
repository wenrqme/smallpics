"""
This scrip resizes all images in a directory and converts them to jpeg

input directory: large/
output directory: resized/

"""

import os
import glob
from PIL import Image

IN_FOLDER = 'large/'
OUT_FOLDER = 'resized/'


#resize all images to this width
width = 1200

for file in glob.glob(IN_FOLDER + '*'):
    file_base = os.path.basename(file)[:-4]
    output_file = OUT_FOLDER + '/' + file_base + '.jpg'
    print(file_base)

    #only resize if images are not already the directory
    if not os.path.exists(output_file):
        print("resizing!")
        img = Image.open(file)
        icc_profile = img.info.get('icc_profile')
        w_percent = width/float(img.size[0])
        height = int(float(img.size[1])*float(w_percent))
        new_img = img.resize((width, height), Image.ANTIALIAS)
        new_img = new_img.convert('RGB')
        new_img.save(output_file, format='JPEG', icc_profile=icc_profile)
    else:
        print('already here, not resizing!')

print('yeeee we done!!')
