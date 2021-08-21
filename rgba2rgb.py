from PIL import Image
import os
src = "D:\Documents\scripts\csgan\\archive\Test\\"
dst = "D:\Documents\scripts\csgan\\resizedData\\"
weapons = next(os.walk('D:\Documents\scripts\csgan\\archive\Test'))[1]

#os.mkdir(dst)
for folders in weapons:
    for each in os.listdir(src+folders):
        png = Image.open(os.path.join(src,folders,each))
        # print each
        if png.mode == 'RGBA':
            png.load() # required for png.split()
            background = Image.new("RGB", png.size, (0,0,0))
            background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
            background.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
        else:
            png.convert('RGB')
            png.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')

print("Done")
