#Clarissa Dayle Fernandes
#101131520

#This is the sketch program. This is just a compilation of all the functions
#required to perform the pencil sketch effect.

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import code
#-------------------------------------------------------------------------------
#function to invert the image colours
def invert_image(img):

    temp = np.zeros(img.shape)

    temp = 255 - img

    return temp
#-------------------------------------------------------------------------------
#function to gaussian blur the inverted image
def blur_image(img):

    invert = invert_image(img)

    #using a mediam/big kernel size in order to accomodate larger images
    temp = cv2.GaussianBlur(invert, (25,25), 0, 0)

    return temp

#-------------------------------------------------------------------------------
def lighten(img):

    blurred = blur_image(img)
    invert_blurred = invert_image(blurred)

    #the sketch is created by performing bitwise DIVIDE betwen the original
    #blurred image and the inverted blurred image
    sketched =  cv2.divide(img, invert_blurred, scale=256)
    x, y = sketched.shape

    #read in the background paper image and resizing it to fit the input image
    temp = cv2.imread("bg.jpeg", 0)
    bg = cv2.resize(temp, (y, x))

    #images are overlayed by performing the bitwise AND function on them
    final = cv2.bitwise_and(sketched, sketched, mask=bg)

    return final

#-------------------------------------------------------------------------------
