import numpy as np
a = np.array([
    [
        [
            [1,0],
            [0,0]
        ],
        [
            [1,1],
            [0,0]
        ]
    ],
    [
        [
            [1,1],
            [1,0]
        ],
        [
            [1,1],
            [1,1]
        ]
    ]
])
print(np.sum(a, axis = 3))
print(np.sum(np.sum(a, axis = 3), axis=2))
# print(np.argmin(a,axis=3))
# print(np.array([[1,0,0],[0,1,0],[0,0,1]]))
# print(np.array([[0,1,0],[1,1,0],[1,1,1]]))
# print(np.array([[0,0,0],[0,1,0],[0,0,1]]))