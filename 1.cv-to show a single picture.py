import cv2
img=cv2.imread("rain.jpg")
cv2.imshow('rain',img)
cv2.imwrite('rain.jpg',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
