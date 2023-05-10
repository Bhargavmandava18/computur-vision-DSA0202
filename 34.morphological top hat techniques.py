import cv2
import numpy as np

# Read in an image
img = cv2.imread("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (4).png")

# Define a kernel
kernel = np.ones((5,5), np.uint8)

# Perform the top-hat operation
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display the original and top-hat-processed images
cv2.imshow('Original', img)
cv2.imshow('Top-Hat', tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()
