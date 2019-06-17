import numpy as np


def integral(img):
    integral_graph = np.zeros((img.shape[0], img.shape[1]), dtype=np.int32)
    for x in range(img.shape[0]):
        sum_cols = 0
        for y in range(img.shape[1]):
            sum_cols = sum_cols + img[x][y]
            integral_graph[x][y] = integral_graph[x-1][y] + sum_cols
    return integral_graph
