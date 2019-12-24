import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser

new=2

image = cv2.imread("linkedin.png")

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    s = str(obj.data)
    print("Type: ", obj.type)
    print("Data: ", obj.data)

url=s[2:-1]

webbrowser.open(url, new=new)