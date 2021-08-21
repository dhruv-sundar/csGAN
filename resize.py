from PIL import Image
import os, sys
#weapons = next(os.walk('.'))[1]
path = "D:\Documents\scripts\csgan\\archive\Train\\"
dst = "D:\Documents\scripts\csgan\\archive\\resized\\"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((128,128), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'png', quality=90)

resize()
print("done")
