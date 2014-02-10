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

# <codecell>

artimgs = ('/home/wcmckee/Pictures/art/wp-content/uploads/2013/02')

# <codecell>

os.chdir(artimgs)

# <codecell>

class Backup(object):
    def findfiles(self, filestring):
        filecur = os.listdir(os.curdir)
        for filename in filecur:
            if filestring in filename:
                yield filename

# <codecell>

app = Backup()

# <codecell>

photolist = []

# <codecell>

for aviz in app.findfiles('1024x682.jpg'):
    photolist.append(aviz)

# <codecell>

print photolist

# <codecell>

photoamou = len(photolist)

# <codecell>

ranznum = random.randint(0, photoamou)

# <codecell>

doubnum = ranznum + 1

# <codecell>

chdirz = photolist[ranznum]

# <codecell>

chdirz2 = photolist[doubnum]

# <codecell>

print chdirz2
print chdirz

# <codecell>

img2 = Image.open(chdirz)

# <codecell>

imgza2 = Image.open(chdirz2)

# <codecell>

imgAgain = img2.rotate(180)

# <codecell>


# <codecell>

imgSapz = ImageChops.lighter(imgAgain, img2)

# <codecell>

imgCepz = ImageChops.darker(imgza2, imgSapz)

# <codecell>

enzSapz = ImageChops.subtract(imgSapz, img2)

# <codecell>

imgLower = ImageChops.constant(imgAgain, 2)

# <codecell>

imgOver = ImageEnhance.Brightness(imgLower)

# <codecell>

imgTitle = Image.open(chdirz)

# <codecell>

imgComt = ImageChops.blend(imgTitle, enzSapz, .5)

# <codecell>

imgConvertz = ImageEnhance.Color(imgComt)

# <codecell>

img3 = ImageChops.screen(imgComt, img2)

# <codecell>


bighImg = ImageChops.darker(img2, imgComt)

# <codecell>

screen = ImageChops.difference(imgAgain,img2)

# <codecell>

brightLight = ImageEnhance.Brightness(screen)

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

cRan = random.randint(1,30)

# <codecell>

#import ImageFont, ImageDraw

#draw = ImageDraw.Draw(lightFilz)
# use a truetype font
#font = ImageFont.truetype("cs.ttf", 24)
#draw.text((100, 200), "a film by William Mckee", fill=(49,cRan,2),font=font)
#draw.text((400, 300), 'Suburb Nightmare: Mist City', fill =(49,3,cRan),font=font)
#draw.text((600, 400), 'Based on the game: Suburb Warp Nighmare', fill=(cRan,3,2), font=font)


# <codecell>

imgSwapz = ImageChops.difference(img2, fileSwap)

# <codecell>

lightFilz.show()

# <codecell>

imgBlack = ImageChops.darker(imgSwapz, img2)

# <codecell>

imgZero = ImageChops.invert(imgBlack)

# <codecell>

imgBlack.show()

# <codecell>


