import cv2
cap = cv2.VideoCapture(0)

while(True):
    check , frame = cap.read() #รับภาพจากกล้องเฟรมต่อเฟรม
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break
        cap.release()
        cv2.destroyAllWindows