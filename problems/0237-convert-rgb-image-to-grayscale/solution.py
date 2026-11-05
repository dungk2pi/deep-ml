import numpy as np

def rgb_to_grayscale(image):
    new_image = []
    new_row = []
    for img in image:
        new_row = []
        for pixel in img:
            if not isinstance(pixel, list) or len(pixel) != 3:  
                return -1
            if pixel[0] not in range(0,256) or pixel[2] not in range(0,256) or pixel[1] not in range(0,256):
                return -1 
            new_pixel = round(0.299 * pixel[0] +0.587* pixel[1]+0.114*pixel[2])
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image