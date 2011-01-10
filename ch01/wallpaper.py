#!/usr/bin/python2.5

import getopt
import sys
from PIL import Image, ImageColor

def usage():
    print """\
Usage:

  wallpaper.py --scale=<scale>

# FIXME: need to add command-line options:
#   - corner_a, corner_b, size, color


    """

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    side = 234
    corner_a = 10
    corner_b = 10

    im = Image.new('RGB', (100, 100))   # init to black
    white = ImageColor.getrgb('#fff')

    for i in range(0, 100):
        for j in range(0, 100):
            x = corner_a + float(side) * float(i) / 100.0
            y = corner_b + float(side) * float(j) / 100.0
            c = int(x * x + y * y) % 2
            if c == 0:
                im.putpixel((i, j), white)

    im.save('wallpaper.png')

if __name__ == "__main__":
    main(sys.argv[1:])
