import cv2
import numpy as np

def sigmoid(x):
    f = 1 / (1 + np.exp(-x))
    return f

img = cv2.imread(str("mario.jpg"))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

print(np.ravel(v))

input()