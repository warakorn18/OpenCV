#นำรูปภาพเข้าและอ่านรูปภาพ
import cv2
img = cv2.imread("image/cat.jpg")

#แสดงภาพ
cv2.imshow("Output",img)
cv2.waitKey(delay=3000)
cv2.destroyAllWindows()