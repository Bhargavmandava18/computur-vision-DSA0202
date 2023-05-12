import cv2

face_cascade = cv2.CascadeClassifier("C://Users\BHARGAV\Pictures\Screenshots\Screenshot (4).png")
image = cv2.imread('1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
