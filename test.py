import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_range = np.array([90,50,50])
    upper_range = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    
    result = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', result)

    cv2.imshow('frame', frame)

    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()