#!/usr/bin/python2.5

import PIL
from PIL import Image, ImageColor

im = Image.new('RGB',(200,200))
white = ImageColor.getrgb('#fff')
for x in range(90,110):
    for y in range(90,110):
        im.putpixel((x,y),white)
im.save('wallpaper.png')

