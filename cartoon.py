#Clarissa Dayle Fernandes
#101131520

#This is the cartoon program. This is just a compilation of all the functions
#required to perform the comic-cartoon effect.

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import code
#-------------------------------------------------------------------------------
#function to blur the image
def blur_image(img):

    print("in blur")
    return cv2.medianBlur(img, 3)
#-------------------------------------------------------------------------------
#function to get the thick edges from the grayed+smoothed image
def get_edges(img):

    pic = blur_image(img)

    #this function is taken from assignment 1 edges, without NPS(no thin edges)
    pic2 = code.get_edge(img)

    th, edge = cv2.threshold(pic2, 15, 255, cv2.THRESH_BINARY)

    result = np.zeros(edge.shape)
    x, y = edge.shape
    for i in range(x):
        for j in range(y):
            if (edge[i][j] == 255):
                result[i][j] = 0
            else:
                result[i][j] = 255

    return result
#-------------------------------------------------------------------------------
#function to smooth out the colours to remove harsh contrasts and edges between
#the colours
def smooth_color(img):

    img_smooth = cv2.medianBlur(img, 3)

    return img_smooth
#-------------------------------------------------------------------------------
#function to overlay the thick edges with the smoothed colour image. The result
#is returned.
def overlay(img_gray, img_color):

    edge = get_edges(img_gray)
    edge = edge.astype(np.uint8)

    #converting the grayscale edges to an rgb image so overlaying can be done
    edge_rgb = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)
    edge_rgb = edge_rgb.astype(np.uint8)

    #converting the rgb smooth colour image to bgr
    color_rgb = smooth_color(img_color)
    color_bgr = cv2.cvtColor(color_rgb, cv2.COLOR_RGB2BGR)

    #final overlaying is done by performing bitwise AND on the two images
    cartoon_result = cv2.bitwise_and(color_bgr, color_bgr, mask=edge)

    return cartoon_result
#-------------------------------------------------------------------------------
