
m = [
    [1, -2, 3, 4, -1],
    [5, 6, -7, -8, 9],
    [-10, 11, 12, -13, 14],
    [15, -16, -17, 18, -19],
    [20, 21, -22, 23, 24],
    [-25, -26, 27, 28, -29],
    [30, 31, -32, 33, 34]
]


p = []

for i in range(7):
    c = 0
    for j in range(5):
        if m[i][j] > 0:
            c += 1
    p.append((c, i)) 


for a in range(len(p)):
    for b in range(0, len(p) - a - 1):
        if p[b][0] < p[b + 1][0]:  
            p[b], p[b + 1] = p[b + 1], p[b]

s = []
for c, i in p:
    s.append(m[i])


print("Исходная матрица:")
for r in m:
    print(r)


print("Отсортированная матрица:")
for r in s:
    print(r)
