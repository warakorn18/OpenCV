
import cv2
img = cv2.imread("image/cat.jpg",0)
imgresize = cv2.resize(img,(500,580))
cv2.imshow("My cat",imgresize)

cv2.imwrite("output.jpg",imgresize)

cv2.waitKey()
cv2.destroyAllWindows()