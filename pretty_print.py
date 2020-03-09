import math


def make_oneline(text, m):
    cost_matrix = [[0 for i in range(len(text))] for j in range(len(text))]
    for i in range(len(text)):
        for j in range(i, len(text)):
            cost = m - j + i - sum([len(x) for x in text[i:j]])
            if cost < 0:
                cost = math.inf
            cost_matrix[i][j] = cost**3
    return cost_matrix
