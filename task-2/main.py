n = 7
matrix = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(i, n):
        matrix[i][j] = j + 1

for row in matrix: print(' '.join(map(str, row)))