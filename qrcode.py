import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("qrcode4.png")

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")
