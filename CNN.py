import cv2
import numpy as np

t = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5':1, '6': 0, '7': 0, '8': 0, '9': 0}

filter = np.array([
    [[0,0,0],[1,1,1],[0,0,0]],
    [[0,1,0],[0,1,0],[0,1,0]],
    [[1,0,0],[0,1,0],[0,0,1]],
    [[0,0,1],[0,1,0],[1,0,0]],
]) #とりあえずランダムのフィルター

def sigmoid(x):
    f = 1 / (1 + np.exp(-1 * x))
    return f

def softmax(array, numerator): #numeratorは分子という意味。求めたい数値のarrayでのインデックス。
    value = 0 #分母
    for i in range(len(array)):
        value = value + np.exp(array[i])
    
    f = np.exp(array[numerator]) / value
    return f

def convolution(input, filter):
    value = [] #フィルターかけたやつ(一時的なもの)
    for i_0 in range(len(input) - 2):
        value.append([])
        for i_1 in range(len(input[i_0]) - 2):
            value[i_0].append(np.array([input[i_0][i_1:i_1 + 3], input[i_0 + 1][i_1:i_1 + 3], input[i_0 + 2][i_1:i_1 + 3]]) * filter)
    return np.array(value).sum(axis=3).sum(axis=2)

def pooling(input):
    value = [] #2x2ずつ抽出(一時的なもの)
    for i_0 in range(len(input)):
        if i_0 % 2 == 0:
            value.append([])
            for i_1 in range(len(input[i_0])):
                if i_1 % 2 == 0:
                    value[int(i_0 / 2)].append(np.array([input[i_0][i_1:i_1 + 2], input[i_0 + 1][i_1:i_1 + 2]]))
                elif i_1 == len(input[i_0]) - 1:
                    value[int(i_0 / 2)].append(np.array([[input[i_0][i_1], 0], [input[i_0 + 1][i_1], 0]]))
        elif i_0 == len(input) - 1:
            value.append([])
            for i_1 in range(len(input[i_0])):
                if i_1 % 2 == 0:
                    value[int((i_0 + 1) / 2)].append(np.array([input[i_0][i_1:i_1 + 2], [0, 0]]))
                elif i_1 == len(input[i_0]) - 1:
                    value[int((i_0 + 1) / 2)].append(np.array([[input[i_0][i_1], 0], [0, 0]]))

    return np.array(value).max(axis=3).max(axis=2)


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

u_11 = convolution(input_v, filter[0]) #特徴マップ1
print(u_11)
u_21 = pooling(u_11)
print(u_21)

input()

u_12 = convolution(input_v, filter[1]) #特徴マップ2
print(u_12)
u_22 = pooling(u_12)
print(u_22)

input()

u_13 = convolution(input_v, filter[2]) #特徴マップ3
print(u_13)
u_23 = pooling(u_13)
print(u_23)

input()

u_14 = convolution(input_v, filter[3]) #特徴マップ4
print(u_14)
u_24 = pooling(u_14)
print(u_24)

input()

#2セット目
u_31 = convolution(u_21, filter[0])
print(u_31)
u_41 = pooling(u_31)
print(u_41)

input()

u_51 = convolution(u_41, filter[0])
print(u_51)

input()