import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser

new=2

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
s = ""
count = True
while count:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        s = str(obj.data)
        #print("Data", obj.data)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
    
    if s:
        url=s[2:-1]
        webbrowser.open(url, new=new)
        break
    
        
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break