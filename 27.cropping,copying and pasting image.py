import cv2
import numpy as np
img1 = cv2.imread("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (3).png")
img2 = cv2.imread("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (3).png")
roi = img1[y:y+h, x:x+w]
roi_resized = cv2.resize(roi, (w, h))
img2gray = cv2.cvtColor(roi_resized,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img2_bg = cv2.bitwise_and(img2,img2,mask = mask_inv)
img1_fg = cv2.bitwise_and(roi_resized,roi_resized,mask = mask)
dst = cv2.add(img2_bg,img1_fg)
img2[y:y+h, x:x+w] = dst
cv2.imshow('Result', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
