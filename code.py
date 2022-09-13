#Clarissa Dayle Fernandes
#101131520
#COMP 4102A Assignment 1, Question 2

import cv2
import numpy as np
import math
#----------------------------------------------------
#gaussian function
def gaussian_eq(h,k,sigma):
    return (1 / (2 * np.pi * (sigma ** 2))) * (np.e ** (-(h**2 + k**2)/ (2 * sigma**2)))

#----------------------------------------------------
#function for gaussian kernel creation
def gaussian_kernel(sigma):

    #calculating the size of the kernel
    hsize = 2 * math.ceil(3 * sigma) + 1

    #creating a 1D kernel
    x = np.linspace(-hsize/2, hsize/2, hsize)

    #find the middle
    mid = hsize // 2

    #create 2D Gaussian kernel
    x_2D = np.outer(x.T,x.T)

    #applying gaussian function
    for i in range(hsize):
        for j in range(hsize):
            x_2D[i][j]= gaussian_eq(j-mid,mid-i, sigma)

    x_2D = x_2D / np.sum(x_2D)

    return x_2D

#----------------------------------------------------
#function for convolution
def convolution(image, kernel):

    #getting dimensions of image and kernel
    img_x , img_y = image.shape
    kern_x , kern_y = kernel.shape

    #calculating the padding width
    pad = kern_x // 2

    #padding the image for convolsion
    temp = image
    temp = np.pad(temp, pad)

    #creating 2D array of size image
    result = np.zeros([img_x, img_y])

    #the convolution process
    for i in range(img_x):
        for j in range(img_y):
            curr = temp[i:i+kern_x, j:j+kern_y]
            multiplied = curr * kernel
            result[i, j] = np.sum(multiplied)

    return result

#----------------------------------------------------
def gaussian_blur(image, sigma):
    kernel = gaussian_kernel(sigma)
    result = convolution(image, kernel)

    return result

#----------------------------------------------------
#function to do Sobel
def sobel(img):

    #creating sobel x and y filters for sobel edge detection
    sobel_arr = np.array([[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]])
    sobel_arr2 = np.array([[-1.0, -2.0, -1.0], [0.0, 0.0, 0.0], [1.0, 2.0, 1.0]])

    #calculating the vertical gradient
    grad_x = convolution(img, sobel_arr)

    #calculating the horizontal gradient
    grad_y = convolution(img, sobel_arr2)

    #calculating the gradient magnitude
    grad_combined = img
    grad_combined = np.sqrt(np.square(grad_x) + np.square(grad_y))
    grad_combined *= 255.0 / grad_combined.max()

    #finding direction of gradient magnitude
    grad_direction = np.arctan2(grad_y, grad_x)

    return grad_combined, grad_direction

#----------------------------------------------------
def thresholding(img, tau):

    #getting dimension values
    img_x , img_y = img.shape

    #creating empty 2D array
    result = np.zeros(img.shape)

    for i in range(img_x):
        for j in range(img_y):
            if img[i][j] > tau:
                img[i][j] = 0
            else:
                img[i][j] = 255

    print("Non Maximum Suppression complete")

    return img
#----------------------------------------------------
def get_edge(img):
    blurred = gaussian_blur(img, 1)
    grad_magnitude, dir = sobel(blurred)
    #non_max = non_max_supp(grad_magnitude, dir)
    #thresh = thresholding(non_max, 10)

    return grad_magnitude
#----------------------------------------------------
