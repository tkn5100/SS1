import cv2
import numpy as np

# シグモイド関数の定義
def sigmoid(x):
    f = 1 / (1 + np.exp(-x))
    return f

# 画像ファイルの読み込み
img = cv2.imread("zebra.jpg")
img_array = np.asarray(img)

# hsv形式に変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# h,s,vに分配
h,s,v = cv2.split(hsv)

# 明るさの平均値と標準偏差を画面表示
print("mean: " + str(np.mean(v)))
print("std : " + str(np.std(v)))

# 明るさをそのまま出力
print(v)

input()