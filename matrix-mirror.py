#!/usr/bin/python

# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import os
import Image
import ImageDraw
from time import sleep
from io import BytesIO
from picamera import PiCamera
from rgbmatrix import Adafruit_RGBmatrix

camera = PiCamera()
camera.resolution = (320, 240)
camera.vflip = True
camera.start_preview()

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)
matrix.Fill(0x6F85FF) # Fill screen with color
sleep(2)

def showImg():
    stream = BytesIO()
    camera.capture(stream, resize=(43,32), format='jpeg')
    stream.seek(0)
    image = Image.open(stream)
    image.load()          # Must do this before SetImage() calls
    matrix.SetImage(image.im.id, -10, 0)
    image.close()

var = 0
while var < 4800:
    showImg()
    var += 1
    sleep(.500)

# reboot and reload to flush memory
matrix.Clear()
os.system("sudo reboot now")
