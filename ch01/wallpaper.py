#!/usr/bin/python2.5

import optparse
import sys
from PIL import Image, ImageColor

def usage():
    print """\
Usage:

    wallpaper.py --xpos=  --ypos=  --xsize=  --ysize= --scale=<scale>

Example:

    wallpaper.py --xsize=800 --ysize=600 --xpos=10 --ypos=20 --scale=123

# FIXME: need to add command-line options:
#   - corner_a, corner_b, size, color

    """

def main():

    op = optparse.OptionParser()
    op.add_option("--xpos", action="store", type="int", dest="xpos",
                  help="x position in field", default=123, metavar="XPOS")
    op.add_option("--ypos", action="store", type="int", dest="ypos",
                  help="y position in field", default=456, metavar="YPOS")
    op.add_option("--xsize", action="store", type="int", dest="xsize",
                  help="x dimension of generated image", default=800,
                  metavar="XSIZE")
    op.add_option("--ysize", action="store", type="int", dest="ysize",
                  help="y dimension of generated image", default=600,
                  metavar="YSIZE")
    op.add_option("--scale", action="store", type="int", dest="scale",
                  help="scale of field scan", default=10, metavar="SCALE")

    opts, args = op.parse_args()

    side = 234
    corner_a = 10
    corner_b = 10

    im = Image.new('RGB', (opts.xsize, opts.ysize))   # init to black
    white = ImageColor.getrgb('#fff')

    for i in range(0, opts.xsize):
        for j in range(0, opts.ysize):
            x = opts.xpos + float(opts.scale) * float(i) / float(opts.xsize)
            y = opts.ypos + float(opts.scale) * float(j) / float(opts.ysize)
            c = int(x * x + y * y) % 2
            if c == 0:
                im.putpixel((i, j), white)

    im.save('wallpaper.png')

if __name__ == "__main__":
    main()
