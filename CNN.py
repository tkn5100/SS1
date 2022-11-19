import cv2
import numpy as np

t = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5':1, '6': 0, '7': 0, '8': 0, '9': 0}

filter = np.array([[1,0,0],[0,1,0],[0,0,1]]) #とりあえずランダムのフィルター

def sigmoid(x):
    f = 1 / (1 + np.exp(-1 * x))
    return f

img = cv2.imread(str("5.png"))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
input_h,input_s,input_v = cv2.split(hsv)
print(input_v)
#画素を0,1に変換
for i_0 in range(len(input_v)):
    for i_1 in range(len(input_v[i_0])):
        if input_v[i_0][i_1] > 127.5:
            input_v[i_0][i_1] = 0
        else:
            input_v[i_0][i_1] = 1
print(input_v)

xh_1 = []
for i_0 in range(len(input_v) - 2):
    xh_1.append([])
    for i_1 in range(len(input_v[i_0]) - 2):
        xh_1[i_0].append(np.array([input_v[i_0][i_1:i_1 + 3], input_v[i_0 + 1][i_1:i_1 + 3], input_v[i_0 + 2][i_1:i_1 + 3]]) * filter)

u_1 = np.array(xh_1).sum(axis=3).sum(axis=2)
print(u_1)

p_1 = []
for i_0 in range(0, len(u_1), 2):
    p_1.append([])
    for i_1 in range(0, len(u_1[i_0]), 2):
        p_1[int(i_0 / 2)].append(np.array([u_1[i_0][i_1:i_1 + 2], u_1[i_0 + 1][i_1:i_1 + 2]]))
# print(np.array(p_1))
print(np.array(p_1).max(axis=3).max(axis=2))

input()