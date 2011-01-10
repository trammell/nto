#!/usr/bin/python2.5

import PIL
from PIL import Image, ImageColor

im = Image.new('RGB',(200,200))
white = ImageColor.getrgb('#fff')
for x in range(90,110):
    for y in range(90,110):
        im.putpixel((x,y),white)
im.save('wallpaper.png')

# for i = 1..100:
#     for j = 1..100:
#         x = corner_a + i * side / 100
#         y = corner_b + j * side / 100
#         c = int(x^2 + y^2)

