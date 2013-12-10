# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# WMCKEE PIL EDITZ

# <rawcell>

# Opens up images and edits them

# <codecell>

from PIL import Image
import random
import os
from PIL import ImageChops
from ftplib import FTP


# <codecell>

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in ('.txt', '.htm', '.html'):
        ftp.storlines('STOR ' + file, open(file))
    else:
        ftp.storlines('STOR ' + file, open(file, 'rb'), 1024)

# <codecell>

ftp = FTP('ftp.freshfigure.com')

# <codecell>

ftp.login('ipython', 'PassWord123!')

# <codecell>

os.chdir('/home/will/Desktop/output/')

# <codecell>

chdirz = random.choice(os.listdir('/home/will/Desktop/output/'))

# <codecell>

chdirz2 = random.choice(os.listdir('/home/will/Desktop/output/'))

# <codecell>

img2 = Image.open(chdirz)

# <codecell>

imgza2 = Image.open(chdirz)

# <codecell>

imgAgain = img2.rotate(180)

# <codecell>

imgSapz = ImageChops.lighter(imgAgain, img2)

# <codecell>

imgCepz = ImageChops.darker(imgza2, imgSapz)

# <codecell>

enzSapz = ImageChops.subtract(imgSapz, img2)

# <codecell>

enzSapz.save('edit.jpg')

# <codecell>

def colorz(swapColor):
    return enzSapz

# <codecell>

from PIL import ImageEnhance

# <codecell>

imgLower = ImageChops.constant(imgAgain, 2)

# <codecell>

imgOver = ImageEnhance.Brightness(imgLower)

# <codecell>

img4 = Image.open('edit.jpg')

# <codecell>

imgNever = ImageChops.blend(img4, imgAgain, .5)

# <codecell>

imgTitle = Image.open(chdirz)

# <codecell>

imgComt = ImageChops.blend(imgTitle, imgNever, .5)

# <codecell>

imgConvertz = ImageEnhance.Color(imgComt)

# <codecell>

img3 = ImageChops.screen(imgNever, img2)

# <codecell>


bighImg = ImageChops.darker(img2, imgNever)

# <codecell>

screen = ImageChops.difference(imgAgain,img2)

# <codecell>

screen.save('edit.jpg')

# <codecell>

brightLight = ImageEnhance.Brightness(screen)


# <codecell>

openFilz = Image.open('edit.jpg')
openFilz.show()

# <codecell>

lightFilz = ImageChops.lighter(screen, img2)

# <codecell>

imgSwap = ImageChops.difference(lightFilz, img2)

# <codecell>

lightXus = ImageChops.darker(img2, imgSwap)

# <codecell>

lightGone = ImageChops.invert(lightXus)

# <codecell>

fileSwap = ImageChops.lighter(lightGone, img2)

# <codecell>

import ImageDraw
import math

# <codecell>

piz = math.pi

# <codecell>

print piz

# <codecell>

draw = ImageDraw.Draw(img2)

# <codecell>


# <codecell>

draw.rectangle([(0, 0), (1920, 150)], fill='black')

# <codecell>

draw.rectangle([(0, 500), (1920, 1080)], fill='black')

# <codecell>


# <codecell>


# <codecell>

del draw 

# <codecell>

img2.save("hello.PNG")

# <codecell>

helloz = Image.open("hello.PNG")

# <codecell>

helloz.show()

# <codecell>

os.chdir('/home/will/Desktop/wirepil')

# <codecell>

import ImageFont, ImageDraw

draw = ImageDraw.Draw(img2)
# use a truetype font
font = ImageFont.truetype("cs.ttf", 24)

draw.text((100, 200), "a film by William Mckee", font=font)

# <codecell>

imgSwapz = ImageChops.difference(img2, fileSwap)
imgSwapz.show()

# <codecell>

img2.show()
img2.save(chdirz)

# <codecell>

imgBlack = ImageChops.darker(imgSwapz, imgNever)

# <codecell>

imgBlack.show()

# <codecell>

imgZero = ImageChops.invert(imgBlack).show()

# <codecell>


# <codecell>


# <codecell>


# <codecell>


