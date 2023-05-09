import cv2
import numpy as np
img=cv2.imread("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (3).png")
resize =cv2.resize(img,(250,250))
cv2.imshow("resize",resize)
resize=cv2.resize(img,(50,50))
cv2.imshow("small",resize)
