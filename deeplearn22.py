import cv2
import numpy as np

weight = [] #重み
theta = [55487,55486,0.5] #シグモイドの時の閾値(適当)
v_1 = [[],[]] #かくれ層1層目のベクトル
t = {'0': 0, '1': 10, '2': 20, '3': 30, '4': 40, '5': 50, '6': 60, '7': 70, '8': 80, '9': 90}

def sigmoid(x):
    f = 1 / (1 + np.exp(-1 * x))
    return f

img = cv2.imread(str("0.png"))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
x = np.ravel(v) #ベクトル(1次元配列)に直す
weight.append([])
for i in range(len(x)):
    weight[0].append(1) #とりあえず画素数分重みを用意して、全部1にする
weight.append([1,1]) #y出すときに使うweight

#1回、出力層を算出
def handle():
    v_1[0] = float(sigmoid(np.dot(x, weight[0]) - theta[0])) #xとweightの内積
    v_1[1] = float(sigmoid(np.dot(x, weight[0]) - theta[1]))
    return sigmoid(np.dot(v_1, weight[1]) - theta[2])
y = handle()

#誤差逆伝播法
def error_backpropagation(num,answer):
    d = ((y - t[answer]) * (1 - y) * y * x[num]) #xの1個目について...
    g = 1 #ゲイン
    return weight[0][num] - (g * d)

#w_1について誤差逆伝播法してみる
for i in range(2):
    print('y:' + str(y))
    weight[0][0] = error_backpropagation(0,'0')
    print('weight:' + str(weight[0][0]))
    y = handle()
input()