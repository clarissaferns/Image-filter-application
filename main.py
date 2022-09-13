#Clarissa Dayle Fernandes
#101131520

#This is the main program. This will take the user input for file name and
#which effect to apply. It will then call the functions from their respective
#.py files.

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import cartoon
import sketch

#-------------------------------------------------------------------------------
if __name__ == '__main__':

    #open the image...
    picture_name = input("Enter the name of the picture to use: ")
    picture_grayscale = cv2.imread(picture_name, 0)
    picture_raw = cv2.imread(picture_name)
    picture_rgb = cv2.cvtColor(picture_raw, cv2.COLOR_BGR2RGB)

    #user chooses which filter to apply...
    print("Enter which filter to use! ")
    print("1. Cartoon")
    print("2. Pencil Sketch")
    filter_input = input("Enter choice (1 or 2): ")

    #if chosen filter is comic cartoon...
    if (filter_input == "1"):
        print("in option 1")
        final = cartoon.overlay(picture_grayscale, picture_rgb)
        cv2.imshow("cartoon", final)

    #if chosen filter is pencil sketch...
    if (filter_input == "2"):
        print("in option 2")
        result = sketch.lighten(picture_grayscale)
        cv2.imshow("pencil sketch", result)

    cv2.waitKey(0)
