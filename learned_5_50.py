import cv2
import numpy as np

filter = np.array([
    [[0,0,0],[1,1,1],[0,0,0]],
    [[0,1,0],[0,1,0],[0,1,0]],
    [[1,0,0],[0,1,0],[0,0,1]],
    [[0,0,1],[0,1,0],[1,0,0]],
    [[0,1,0],[0,1,1],[0,0,0]],
    [[0,1,0],[1,1,0],[0,0,0]],
    [[0,0,0],[0,1,1],[0,1,0]],
    [[0,0,0],[1,1,0],[0,1,0]],
])

#結合層の重み
weight = [
    [-13, -24, -1, -20, -1, -17, -28, -76, -1, -2, -1, 1, 0, -1, -9, -7, -1, -1, -1, 1, 0, -1, 0, -1, -1, -1, 0, -1, 0, -1, 16, 9, -1, -1, -1, 0, 1, -24, -1, -20, -1, 26, -2, -1, -4, -19, 23, -6, -6, -24, -1, -16, -1, -8, -26, -45, -27, -19, -22, -27, -10, -8, -21, -56, 0, 20, 0, 1, 0, -17, 1, -3, 63, -41, -9, 67, -19, -68, -4, 35, 0, 40, 0, 16, 9, 41, 0, 32, 1, 19, 1, 1, 0, 12, 1, 14, -1, -3, -1, 0, 0, 8, 1, -23, 58, -47, 15, 36, 4, 0, 36, -5, -1, -7, -2, 9, 1, 25, 1, -12, 9, 4, -1, 33, 20, 33, 1, 30, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, -16, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, -29, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 16, 0, 0, 1, 36, 0, 0, 0, 1, 0, -1, 1, 0, 1, 0, 0, 1, 1, -1, 1, -6, 1, 0, 1, 1, 1, 0, 1, 1, 1, -6, 1, 1, 1, -87, 1, -18, 1, 0, 0, 1, 1, 0, 1, -1, -2, -11, -1, -25, -29, -15, -15, -5, 0, 1, 0, 1, 1, -36, 1, 0, 0, -2, 0, 1, 0, -1, 1, -3, -1, -1, -1, 0, 0, -24, -1, -30, -1, -3, -1, 10, 1, 31, 1, 13, 0, -1, -1, 1, 0, -32, 0, -1, -1, 0, 0, 0, 0, -1, 1, -1, 0, -1, -1, 1, 1, -37, 1, -4, -1, 34, -1, -1, -1, -23, 3, -23, -1, 0, -1, 1, 1, -2, 1, -2, -1, 0, -1, 17, -1, 0, -2, -23, -1, -15, -1, -2, -1, -2, -19, -26, 2, -15, -6, 33, 25, 53, 29, 82, -1, -10, -1, 1, -1, -1, -1, -9, -10, 31, -2, -1, 0, -11, 34, 15, -1, -8, -1, 1, 1, -21, 0, -32, -23, -9, 18, -18, -56, -78, 33, 10, -19, 12, -16, -1, -1, 9, -6, 18, -20, 99, -24, 8, 11, -1, 36, 103, -1, 0, 0, 0, 0, -7, 0, -1, 0, 11, -1, 16, 0, -12, 1, 56, 0, 0, 0, 1, 0, -1, 1, 0, -1, 0, 0, 0, 0, -1, 1, -1, 0, 0, 0, 1, 0, -25, 1, -1, -1, 17, -1, -1, 0, -65, 25, 34, -1, 0, 0, 1, 1, -8, 1, -19, -1, -1, 0, 16, 0, -18, -9, 18, 0, 0, 0, 0, 0, -33, 0, -10, 0, -39, 0, 1, -8, 56, -1, 21, 0, -1, -1, 1, 0, -1, 0, 0, 0, 0, 1, 0, 0, -2, 1, 0, 0, 17, -1, 1, 0, -5, 0, -4, 0, 26, -1, 0, -35, 2, -6, 21, -1, -1, 0, 1, 0, 9, 1, 12, -1, 42, 0, 15, -1, -24, -18, 34],
    [0, 0, 0, 0, -1, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, -2, 0, -2, 0, -1, 0, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -3, 0, -2, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, -1, 0, -2, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -5, -1, -14, 0, -3, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -2, 0, -1, -1, 0, 0, 0, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -1, 0, 0, -2, -2, -2, 0, -2, 0, 0, 0, -1, 0, -2, 0, -2, 0, 0, 0, 0, -2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-49, -14, -1, 23, -36, -114, 19, -117, 0, 9, 0, 0, 0, -1, 15, 29, 0, -1, 0, 0, 0, -1, 0, -1, 0, -2, 0, 0, 0, -1, -5, -34, 0, 0, 0, 0, 0, -1, 0, 9, -2, -15, -4, -1, 0, -12, -4, -7, -1, 34, 0, 23, 0, -24, 39, -21, 13, -30, 39, 4, 9, -64, -15, -87, 0, 0, 0, 0, 0, -1, 0, 0, 0, -58, 13, -28, -29, -87, 0, -22, 0, -4, 0, 0, 0, -16, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, -31, -22, 0, -3, 0, -3, 0, 0, 10, 30, -27, 0, -24, 24, 17, 0, -24, 0, 0, 0, -27, 0, 24, 0, 14, 0, 0, 0, -14, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, -15, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, -1, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, -1, 0, -1, -1, -2, 0, -1, -1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, -16, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -10, 0, 1, -20, 34, 0, 0, 0, 0, 0, -11, 0, 0, -11, -13, 9, -6, -18, 5, -31, 38, 0, -1, 0, 0, 0, 1, 0, 29, -1, 8, 0, -1, -1, -3, -1, 34, 0, -1, 0, -1, 0, -1, 0, -15, 0, 0, 0, 0, 0, -1, 0, -13, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -8, -1, 0, 0, 0, -1, 0, 0, -23, -1, -8, 34, 0, 0, 0, 0, 0, -1, 0, -1, 0, 14, 0, -1, 0, -1, 10, 14, -1, 18, -1, 9, -37, -4, 33, -35, 34, 7, 47, -1, 30, 25, 37, 4, 0, 14, 0, 0, 0, -1, 0, 34, 14, -2, 9, 0, -1, 2, 23, 25, 0, 15, -3, 0, -18, -4, 0, 43, 73, -10, 24, 34, 8, 11, -5, 59, 24, 4, 24, 10, -29, -3, 25, -24, 22, -27, 44, 6, 9, 16, -4, -76, -1, -1, 0, -1, 0, -1, 0, -1, 0, -5, 0, 0, 0, -16, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, -5, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, -40, 0, 0, 0, 39, -5, -20, 0, 0, 0, 0, 0, 9, 0, 34, 0, 16, 0, 0, 0, -9, 15, 33, -1, -1, 0, -1, 0, -1, 0, 14, 0, 2, 0, 0, -6, -16, 10, 23, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -20, -1, 0, -2, -1, 17, 0, -1, -16, -1, 23, 34, 0, 10, 0, 0, 0, -1, 0, 34, -1, 21, -1, -1, -6, -28, 29, 17],
    [0, 0, 0, 0, -1, 1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, -1, -1, -1, -1, -1, 0, -1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, -1, 0, -1, 0, -1, -1, 0, 0, 0, 1, 0, 2, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0, -1, -2, 2, -2, 0, -2, -1, -2, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 1, -1, -1, 0, 1, -1, 0, -1, -1, -1, -2, 2, -2, 1, -3, -1, 0, -1, -1, -1, 0, 0, -1, -1, 0, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 0, 0, 1, 0, -1, 0, -1, -1, -1, -1, -1, -1, 0, 2, 0, 0, 0, -1, 0, -1, -1, 0, -1, -1, -1, 0, 0, -1, -1, 0, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, 1, -1, -1, 0, 1, -1, 0, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0, 0, 0, 0, -1, 2, -1, -1, 1, 0, 1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 2, 1, 1, -1, 0, -2, 0, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 1, -1, -1, 2, -1, -1, 0, 1, 0, 1, 0, 0, -1, 1, 2, 0, 0, 0, 0, 0, -1, 0, 1, 1, 1, -1, 0, 0, 0, 0, 0, 1, -1, -1, -1, 0, -1, -1, -1, 0, 0, 0, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1, 0, 0, 2, 0, 0, 2, 0, 1, 0, -1, 0, -1, -1, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, 0, -1, -1, 0, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, 0, -1, -1, 0, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, -1, 0, 0, -1, 0, 0, 1, 0, -1],
    [52, -4, 8, 16, 142, 115, 6, -45, -13, -18, -10, 0, -12, -14, -5, -21, -5, -5, -7, -1, -7, 11, -1, -5, -7, -15, -4, 0, -5, 24, -12, -17, 50, -5, 15, -2, 40, 29, 10, -37, 12, -32, -6, -1, 52, -4, -43, -51, -4, 2, 22, -4, 29, -6, -7, -26, -34, -41, 1, 2, -16, -23, -29, -40, -6, -3, 0, 0, 23, -30, 0, -18, -13, -81, -19, -13, -54, -27, -8, -13, 7, -1, 7, 0, 24, -25, 14, -8, 0, 0, 0, 0, 15, -5, -1, -9, 14, -25, 5, 11, 22, -44, 21, -17, -30, -60, -12, -25, -29, -18, -32, -47, 13, 8, 22, 0, 31, -7, 17, -6, -5, -8, 10, 0, 2, -2, -9, -8, -5, -1, 0, 0, 0, -10, 0, -1, -1, -5, 0, 0, 0, -5, 0, -8, -11, -8, -5, -1, -8, -16, -3, -10, 0, 0, 0, 0, 0, 1, 0, 0, -9, -8, 0, 0, -4, -6, 0, -17, -4, -14, -5, 0, -12, 10, -11, -21, 0, 0, 0, 0, 0, -6, 0, 0, -4, -6, 0, -1, -5, -30, 0, -7, 8, -8, -9, 50, 15, 32, -12, -14, 35, -9, -1, 49, 25, 8, -8, -4, 0, 0, 0, 0, 12, 60, 0, 0, 38, 4, 32, 22, 11, 25, -38, 13, 39, 1, -4, 50, 61, 11, -3, -14, 1, -44, -8, 11, 12, 16, -22, -50, -8, -20, 0, 7, -7, -26, -1, -13, 10, 0, -5, 50, 16, 35, -12, -10, 8, 4, 22, -3, 23, 104, 19, -25, -19, -22, 1, 0, 3, -35, -3, -28, -17, -9, -4, -1, -2, -26, -1, -23, -1, -6, 0, 0, 6, 31, -1, -15, 2, -8, 11, 0, 3, 11, 25, -21, 10, -62, -8, -16, -21, 32, -46, -23, 11, 25, 33, -1, 29, 15, 30, -9, -9, -21, 20, 5, 3, 28, 1, -26, 26, -5, 19, 6, 63, 91, 18, -37, 2, -38, -5, -9, -6, 39, -10, -27, 9, 4, 7, 0, 24, 29, 6, -18, 37, -4, 7, 15, 72, 23, -18, 9, 67, -30, 17, 0, 45, 44, 21, -47, 24, -47, -5, 15, 37, 39, -67, -52, 4, 0, 29, 5, 5, 37, -19, -21, -9, -20, 15, 11, 1, 78, -10, -25, 3, -1, 14, 0, 42, 67, -1, -15, -5, -15, -2, 0, 7, -28, -1, -13, -5, -1, -4, 0, -2, 16, 0, -5, -4, -5, -1, 0, -1, 5, -12, -20, 6, 10, 17, 0, 31, -4, 14, -32, 7, -66, -8, -2, 27, -11, -34, -37, -2, 9, 10, 0, 22, -40, -2, -4, -8, -6, -1, 0, -1, 14, -1, -4, 0, -10, 15, -4, 20, -3, 7, -25, -6, -10, -5, 0, -3, -12, -1, -6, -1, -4, 14, -1, 13, -16, -1, -5, -2, -4, -3, 0, -1, 18, -4, -6, 4, -10, 18, 0, -5, 7, 17, -23, 14, -36, 5, -11, 39, 16, -20, -40, -1, -2, 17, 0, 27, -25, -2, -2, -18, -37, 18, -8, 0, -26, -9, -14],
    [-42, -21, -1, 27, -10, 101, -37, -86, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, -32, 0, 0, 0, 0, 0, 69, 0, -24, -5, 16, -8, 27, 0, 82, -42, -20, 0, -13, 0, 0, 0, 4, -9, -37, -8, -41, 0, -1, -3, 26, -45, -101, 0, 6, 0, 0, 0, 31, 0, 27, 0, -68, 0, -1, -31, -100, 0, 11, 0, -5, 0, 0, 0, -8, 0, -18, 0, 0, 0, 0, 0, -13, 0, -8, 0, 0, 0, 0, 0, 48, 0, -1, 0, -4, 0, 28, -20, -51, 0, 17, 0, 0, 0, 0, 0, 28, 0, 0, 0, 5, 0, 0, 0, 36, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, -2, 0, 0, 0, 0, -8, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 0, 0, 0, 0, 0, 0, 0, 23, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 51, 0, -17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -20, 0, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -85, 0, 0, 0, 0, 0, 0, 0, -14, 0, 0, -6, -54, 0, -43, -3, -153, 35, -27, 0, 0, 0, 0, 0, -3, 0, 0, 0, 0, 0, 0, 0, -10, 0, 0, 0, 0, 0, 0, 0, 51, 0, -24, 0, 0, 0, 0, 0, 33, 0, -12, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 85, 0, 25, 0, 50, 0, 4, 0, 64, 31, 68, 0, 0, 0, 0, 0, 19, 0, 0, -2, -5, 0, 0, 0, 63, 0, -35, 0, 19, 0, 19, -10, 9, 0, -21, 0, -20, -1, 0, -1, -90, -2, -3, 0, 0, 0, 0, 0, 23, 0, 4, 0, 0, 0, 0, 0, -14, 0, -18, 0, 0, 0, 0, 0, 2, 0, -22, -6, -3, -13, 38, -20, -86, -20, -36, 0, -2, 0, 0, 0, -44, 0, -20, 0, -2, 0, 0, 0, -5, -3, -25, 0, 0, 0, 0, 0, 35, 0, 2, 0, 0, 0, 0, 0, 14, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, -3, 0, 0, 0, 0, 0, 41, 0, -1, -1, -17, -2, 0, -7, -33, -4, -54, 0, 0, 0, 0, 0, 27, 0, 0, 0, 0, 0, 0, 0, 38, 0, -33, 0, 4, 0, 10, 0, 78, 0, 27, 0, -12, 0, 0, -15, -8, 0, 0, 0, 0, 0, 0, 0, 51, 0, 15, 0, 0, 0, 0, 0, 19, 0, 0, -2, -1, 0, 0, 0, 27, 0, -25, 0, 14, 0, 15, -9, 79, -1, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, -5, 63, -3, -4],
    [69, 53, 37, 6, 38, 46, 75, 55, 36, 26, -6, -1, 56, 5, 28, 24, 8, -8, -39, 11, 2, 13, 7, 8, -13, 10, 15, -16, 11, 6, 29, -7, 51, 30, -13, -8, 3, 29, 30, 58, 55, 24, 47, -38, 35, 19, 61, 50, 17, 24, -9, 11, 25, 8, 27, 8, 30, 16, 7, 2, 31, 7, 29, 20, -2, -18, -12, -5, -7, -43, -5, -37, 28, -82, -1, -19, -50, -59, -9, -6, 1, -20, -16, -5, -5, -55, -3, -31, -15, -31, -14, -14, -15, -44, 20, -32, 42, -53, -21, -11, -28, -29, -1, 14, 24, -48, 0, -36, -3, -30, 34, 4, 22, -24, -9, 0, 2, -53, 6, 1, 15, -47, -45, -16, -17, -46, 13, -40, 7, 10, -21, 5, 5, 18, 0, -15, -6, -8, -29, -3, -1, -29, 0, -40, 29, -17, -37, 6, 11, 6, 6, -14, -6, -7, -6, -5, -4, -21, -3, -16, 40, -10, -24, -3, -14, 20, 0, 6, 34, -38, -46, -6, 11, -3, -4, 1, -3, -3, -5, 0, 0, -15, 0, -21, -3, -21, -59, 19, -5, -11, 2, -3, 21, -20, -21, -7, 6, 2, -4, -24, -20, -15, -19, -4, -1, -24, 0, -41, -7, -11, -7, -7, -3, -50, -3, -38, -16, -48, -2, -17, -33, -37, -9, -26, 27, -6, -3, -3, -1, -9, 0, -3, 3, 1, 24, -37, 27, -17, 20, 12, 3, -7, -6, -5, -1, -50, 16, -4, -27, -39, -21, -11, -2, -35, -6, -44, 31, 13, -6, -7, -6, 16, 31, 37, 23, -41, -13, -10, -8, 15, 7, 37, 12, -2, -33, 10, -6, 2, 19, -11, 1, -1, 0, -16, -8, -52, 19, 0, 19, -28, 4, -3, -11, 13, 1, 44, 36, -35, -7, -25, -1, 3, 22, 26, 12, -7, -2, 14, 5, -26, 5, -2, 39, -13, -23, 13, 3, 24, 29, 31, 31, -25, -13, -30, 5, 13, -6, 42, 35, -17, 13, -24, -8, -13, 43, 1, -15, -59, -54, -13, -29, -44, -7, -35, -32, -21, -3, -37, -8, -17, 4, -26, 34, -38, 4, -15, -17, 16, 18, 29, 20, -10, 13, -57, -23, 2, 14, 44, 4, -57, -32, -8, -24, 7, 9, -20, 24, -46, -15, -16, -22, 3, -18, -22, 8, 14, 3, -11, 13, -17, 24, 5, 23, -4, -4, -11, 1, -8, 24, -8, 10, -7, -7, -6, -3, 36, 0, 7, 9, -3, 13, -3, 17, -38, 40, 4, 47, -8, 19, -2, -3, 1, 10, 46, 41, 0, 38, -31, 30, 8, 61, 43, 24, 19, 9, 9, 23, -9, 27, 25, -1, -1, -21, -18, 28, -5, 24, 1, 27, 16, -20, 1, 19, 2, 25, -3, 53, -6, -24, -9, 18, -15, 24, 5, 20, 13, -27, 14, 18, -13, 10, 10, 10, 3, 16, -12, 15, -25, 22, 9, 82, -8, -8, -3, -4, 32, 20, 52, 35, -18, -3, -29, 23, -10, 45, 19, 4, 14, -13, 2, 11, -1, 15, -1, 27, 2, -27, 0, 36, 7, 35, 9],
    [0, 0, 0, 0, -1, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, -2, 0, -2, 0, -1, 0, -1, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 19, 0, -2, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, -1, 0, -1, 0, -2, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, -9, -1, -50, 0, -3, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -2, 0, -1, -1, 0, 0, 0, -1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -2, -1, 0, 0, 48, -2, -2, 0, -2, 0, 0, 0, -1, 0, -2, 0, -2, 0, 0, 0, 0, -2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-4, -13, -7, -4, -17, -7, -5, 3, -5, -13, -5, -7, -9, -8, -4, -8, -4, -7, -4, -5, -7, -9, -4, -4, -5, -6, -4, -4, -5, -2, -4, 0, -5, -5, -5, -2, -7, -3, -4, -4, -8, 6, -7, -6, -2, 9, -2, -3, -5, -7, -5, -5, -5, 2, -4, -4, -5, -12, -5, -11, -14, -7, -6, 1, -5, -10, -7, -4, -8, 3, -5, -4, 2, 1, -9, 10, 6, 27, 1, 21, -5, -10, -5, -5, -7, -12, -4, -3, -5, -9, -5, 0, -4, 2, -4, -6, -2, 10, -5, 9, 0, 7, -4, 9, -3, 5, -16, 2, 3, 12, 1, 21, -5, -13, -7, -5, -5, 3, -4, -13, -4, 3, -7, -2, 1, 29, -7, -7, -4, -5, -4, -4, -4, -8, -3, -4, -4, -5, -4, -4, -5, -4, -3, -4, -4, -4, -4, -4, -4, -7, -3, -4, -4, -5, -4, -4, -3, -5, -3, -4, -4, -3, -4, -4, -5, -8, -3, -4, -4, -7, -4, -5, -7, -12, -4, -5, -3, -4, -3, -3, -4, -4, 0, -3, -3, -7, -3, -4, -5, -4, -3, -4, 8, 10, -4, 3, 9, -3, -1, 11, 5, 6, -4, 6, 12, 16, 1, 6, -4, -3, -4, -4, -2, -4, -4, -4, 11, 15, -4, 4, 12, 57, 1, 14, 0, 12, -4, 6, 5, -5, -1, 11, 5, 30, 1, -4, 13, 7, 25, 23, 3, 10, -4, 2, 14, 15, -3, 3, -1, 0, -4, -2, 10, 15, -1, -2, -5, -6, -5, -4, -7, -12, -4, -4, -5, 0, -7, 0, -4, 6, -4, -2, -7, -14, -7, -7, -9, -16, -4, -7, -7, -16, -5, -7, -7, -10, -4, -9, -7, -4, -7, 0, -7, -1, -4, -4, -13, 5, -7, 2, -2, -1, 6, 0, -4, -7, -5, -5, -4, 2, -3, -4, -2, -3, -5, -2, -6, 7, -4, 3, 3, 3, -8, 3, -1, 25, 0, 10, -3, 6, -10, 2, 2, 15, 9, 22, -5, -13, -7, -4, -6, 10, -5, -5, 2, 5, -7, 7, 1, 30, -4, 26, 6, 6, -5, 11, 10, 16, 9, 6, 1, 30, -15, 28, -3, 12, 12, 22, -5, 0, -7, -1, 1, 42, -5, -4, -3, 18, -8, -2, 4, 51, -9, 20, 8, -1, -7, -4, -2, 8, -4, 12, -2, 1, -7, -2, 3, 14, -4, 0, -5, -7, -5, -5, -7, -11, -4, -5, -5, -8, -4, -6, -5, 43, -4, -2, -2, 9, -5, 5, -2, 8, -3, 11, 6, 12, -7, 7, 6, 6, 11, 41, -4, -7, -5, -4, -4, 7, -3, -4, -2, -8, -5, -2, -1, 31, -4, -2, -5, -16, -5, -7, -14, -11, -4, -5, -5, -1, -5, -4, -1, 20, -4, -4, -4, -7, -4, -4, -7, -6, -4, -4, -4, -8, -4, -5, -7, -10, -4, -5, -5, -3, -5, -2, -4, 2, -4, -4, -3, -4, -7, -3, -7, 6, -2, -7, -4, -7, -4, -4, -5, -6, -3, -7, -5, -14, -5, -4, -11, -8, -5, -8],
    [-35, -7, 0, 0, -50, -34, -3, -18, 0, -1, 0, 0, -1, -30, 0, -1, 0, 0, 0, 0, 0, -10, 0, 0, 0, 0, 0, 0, 0, -14, -5, 0, -12, -5, 0, 0, -5, -19, -1, 0, -24, -34, 0, -1, 50, 37, -37, -36, 0, 0, 0, 0, -1, -11, -1, -11, -2, -30, 0, -8, 12, -57, -25, -37, -2, 9, 0, -8, -26, -35, -2, -8, 16, -69, -33, -18, 25, -188, 33, -44, -6, -22, -2, -8, -14, -32, -6, -13, -2, 61, 0, -6, -3, -17, -2, 4, -2, 39, 0, -6, -35, -18, -21, -10, 8, 47, -19, -38, 32, -84, 63, -38, -4, 48, 14, -8, 25, -19, -10, 18, -7, 77, -4, -17, 51, -69, 25, -21, 0, 0, 0, -2, 0, 32, 0, -2, 0, 27, 0, -4, 0, 64, 0, -6, 0, 18, 0, -2, -1, 43, 0, -1, 0, 0, 0, 0, 0, 12, 0, 0, 0, 28, 0, 0, -32, 65, 0, 25, 0, 45, 0, -2, 45, 27, 12, 16, 0, 0, 0, -2, 0, 16, 0, -6, -1, 17, 0, -8, 25, 19, -2, -13, 0, 45, 34, -14, 45, 4, -1, -2, -12, 125, 0, -18, 8, 30, -2, 41, 0, 18, 0, 0, 0, 28, 0, 0, -26, -42, -2, -35, -41, -13, -42, -28, -12, 44, 0, -15, -14, 54, 0, 23, 19, 25, 47, -51, 66, -52, -17, -20, 0, 45, 0, 0, 0, 25, 0, 14, -2, 62, 45, -21, 63, 39, -6, -8, 0, -27, 0, 0, -32, -20, -4, -1, -5, 82, -4, -8, -19, 82, -12, -34, 0, -4, 0, 0, -42, -19, 0, -1, 0, -14, 0, 0, -4, -29, -12, -2, -1, -11, -2, 0, -42, 76, -30, 24, -20, 41, -14, -12, 93, 60, -49, -26, 0, -17, 0, 0, -39, -7, -8, 0, 0, -22, -2, -13, -25, -61, -12, -5, 0, -6, 0, -2, -8, -6, -42, -27, -13, 70, -15, -6, 55, 26, -22, -61, 0, -6, 0, -2, -12, -3, -2, -6, -18, -44, 0, -16, -13, -61, -71, -42, -11, 72, -21, -6, -9, 102, -30, 14, 18, -24, 3, -37, 32, -48, -77, -67, -14, 1, -10, -14, -36, 6, -55, -57, -13, 48, -11, -22, 49, -61, -41, -67, 0, -5, 0, -2, -15, -46, 0, -8, -4, 68, 0, -8, 26, 7, 0, -14, 0, -5, 0, -4, -1, -13, 0, -6, 0, -6, 0, 0, -1, -32, -1, -5, 0, 20, 0, 0, -12, 7, -1, 0, -29, 78, 27, -17, 70, 48, -69, -41, 0, -1, 0, -2, -1, -29, 0, -6, -4, 42, 0, -8, 32, -35, -4, -23, 0, -6, 0, -6, -5, -19, -1, -8, 29, 112, -2, 36, 32, 74, 45, 26, 0, 5, 0, -5, 19, 0, 0, -6, 0, 15, 0, 0, 31, 18, 0, -2, -1, 12, -17, -7, -21, 61, -25, 28, 28, 104, -2, 11, 70, 2, 35, 10, -1, 56, 0, -6, 15, 23, 0, -13, -5, 100, 0, -8, 114, 39, -9, -27]
]
def sigmoid(x):
    f = 10 / (1 + np.exp(-1 * x))
    return f

def softmax(array, numerator): #numeratorは分子という意味。求めたい数値のarrayでのインデックス。
    value = 0 #分母
    for i in range(len(array)):
        value = value + np.exp(array[i])
    # print("value: " + str(value))
    
    f = np.exp(array[numerator]) / value
    # print("f: " + str(f))
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

def probability(array, num):
    return np.round(softmax(array, num), decimals=3) * 100

while True:
    file_name = input("\n読み込むファイル名を拡張子まで入力:")
    img = cv2.imread(file_name)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    input_h,input_s,input_v = cv2.split(hsv)
    #画素を0,1に変換
    for i_0 in range(len(input_v)):
        for i_1 in range(len(input_v[i_0])):
            if input_v[i_0][i_1] > 127.5:
                input_v[i_0][i_1] = 0
            else:
                input_v[i_0][i_1] = 1
    # print(input_v)
    #1セット目
    u_1 = []
    for i in range(len(filter)):
        u_1.append(convolution(input_v, filter[i])) #特徴マップ
    u_2 = []
    for i in range(len(u_1)):
        u_2.append(pooling(u_1[i]))

    #2セット目
    u_3 = []
    for i in range(len(u_2)):
        for i_1 in range(len(filter)):
            u_3.append(convolution(u_2[i], filter[i_1]))
    u_4 = []
    for i in range(len(u_3)):
        u_4.append(pooling(u_3[i]))

    #3セット目
    u_5 = []
    for i in range(len(u_4)):
        for i_1 in range(len(filter)):
            u_5.append(convolution(u_4[i], filter[i_1]))

    u_6 = np.array(u_5).sum(axis=2).sum(axis=1)
    # print(u_6)
    #結合層
    u_7 = []
    for i in range(len(weight)):
        u_7.append(sigmoid(np.dot(u_6, weight[i]) / 30000))
    # print(u_7)
    print("\n---------------------------------------------------------\n")
    print(str(file_name) + "を読み込みました:")
    print("0である確率は" + str(probability(u_7, 0)) + "%です。")
    print("1である確率は" + str(probability(u_7, 1)) + "%です。")
    print("2である確率は" + str(probability(u_7, 2)) + "%です。")
    print("3である確率は" + str(probability(u_7, 3)) + "%です。")
    print("4である確率は" + str(probability(u_7, 4)) + "%です。")
    print("5である確率は" + str(probability(u_7, 5)) + "%です。")
    print("6である確率は" + str(probability(u_7, 6)) + "%です。")
    print("7である確率は" + str(probability(u_7, 7)) + "%です。")
    print("8である確率は" + str(probability(u_7, 8)) + "%です。")
    print("9である確率は" + str(probability(u_7, 9)) + "%です。")
    print("\n---------------------------------------------------------\n")