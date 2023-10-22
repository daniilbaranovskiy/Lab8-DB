import cv2
# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Baranovskiy.jpg")
# DISPLAY
cv2.imshow("Baranovskiy", img)
cv2.waitKey(0)