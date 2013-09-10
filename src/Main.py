#!/usr/bin/env python
#coding=utf8
'''
Created on Jul 15, 2013

@author: pitty <pitty.xu@gmail.com>
'''

import os
import sys
import Image
import ImageFilter
import ImageEnhance

if __name__ == '__main__':
    #test.image = open('../res/pin.png', 'r')
    img = Image.open('../res/pin (2).png', "r")

    #image = image.filter(ImageFilter.MedianFilter())
    #enhancer = ImageEnhance.Contrast(image)
    #image = enhancer.enhance(2)
    #image = image.convert('1')
    #image.show()

    #img = img.convert("RGBA")
    #pixdata = img.load()

    #二值化
    #for y in xrange(img.size[1]):
    #   for x in xrange(img.size[0]):
    #        if pixdata[x, y][0] < 90:
    #            pixdata[x, y] = (0, 0, 0, 255)
    #for y in xrange(img.size[1]):
    #    for x in xrange(img.size[0]):
    #        if pixdata[x, y][1] < 136:
    #            pixdata[x, y] = (0, 0, 0, 255)
    #for y in xrange(img.size[1]):
    #    for x in xrange(img.size[0]):
    #        if pixdata[x, y][2] > 0:
    #            pixdata[x, y] = (255, 255, 255, 255)

    #img = img.filter(ImageFilter.ModeFilter())
    #enhancer = ImageEnhance.Contrast(img)
    #img = enhancer.enhance(1)
    #img = img.convert('1')
    #img.show()

    #im = im.convert()

    #enhancer = ImageEnhance.Brightness(im)
    #im = enhancer.enhance(2.0) #加亮，效果见图1
    #im.show()
    #enhancer = ImageEnhance.Contrast(im)
    #im = enhancer.enhance(4) #提高对比度，效果见图2
    #im.show()
    #im = im.convert('1') #二值化，效果见图3
    #im.show()
    #im = im.filter(ImageFilter.MinFilter) #中值去噪，效果见图4
    #im.show()