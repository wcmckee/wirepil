# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# WMCKEE PIL EDITZ

# <rawcell>

# Opens up images and edits them

# <codecell>

from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
import random
import os
from PIL import ImageChops
import cocos

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

draw = ImageDraw.Draw(lightFilz)

# <codecell>

bakColr = (183,203,235)

# <codecell>

draw.rectangle([(0, 0), (1920, 150)], fill='black')

# <codecell>

draw.rectangle([(0, 500), (1920, 1080)], fill='black')

# <codecell>

draw.rectangle([(90, 190), (370, 220)], fill=bakColr)

# <codecell>

draw.rectangle([(390, 290), (740, 320)], fill=bakColr)

# <codecell>

draw.rectangle([(590, 390), (1100, 420)], fill=bakColr)

# <codecell>

del draw 

# <codecell>

img2.save("hello.PNG")

# <codecell>

helloz = Image.open("hello.PNG")

# <codecell>

os.chdir('/home/will/Desktop/newOut')

# <codecell>

cRan = random.randint(1,30)

# <codecell>

import ImageFont, ImageDraw

draw = ImageDraw.Draw(lightFilz)
# use a truetype font
font = ImageFont.truetype("cs.ttf", 24)
draw.text((100, 200), "a film by William Mckee", fill=(49,cRan,2),font=font)
draw.text((400, 300), 'Suburb Nightmare: Mist City', fill =(49,3,cRan),font=font)
draw.text((600, 400), 'Based on the game: Suburb Warp Nighmare', fill=(cRan,3,2), font=font)


# <codecell>

imgSwapz = ImageChops.difference(img2, fileSwap)

# <codecell>

lightFilz.save(chdirz)

# <codecell>

lightFilz.show()

# <codecell>

imgBlack = ImageChops.darker(imgSwapz, imgNever)

# <codecell>

imgZero = ImageChops.invert(imgBlack)

