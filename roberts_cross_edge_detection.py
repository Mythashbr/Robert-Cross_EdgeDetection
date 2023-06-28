import cv2
import numpy as np
import math

img1 = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

horizontal_filter = np.array([[1, 0], [0, -1]])
vertical_filter = np.array([[0, 1], [-1, 0]])

height, width = img1.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixels1 = np.array([
            [img1[i, j], img1[i, j + 1]],
            [img1[i + 1, j], img1[i + 1, j + 1]]
        ])
        
        pixels2 =  np.array([
            [img1[i, j], img1[i, j + 1]],
            [img1[i + 1, j], img1[i + 1, j + 1]]
        ])

        x = abs(np.sum(np.multiply(horizontal_filter, pixels1)))
        y = abs(np.sum(np.multiply(vertical_filter, pixels2)))
        result = math.sqrt(x**2 + y**2)
        img2[i, j] = result


cv2.imshow('output.jpg', img2)
cv2.waitKey(0)