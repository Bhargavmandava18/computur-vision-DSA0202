import cv2
img = cv2.imread("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (3).png")
watermark = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', cv2.IMREAD_UNCHANGED)
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))
result = cv2.addWeighted(img, 1, watermark, 0.3, 0)
b cv2.imwrite('path/to/result.jpg', result)
