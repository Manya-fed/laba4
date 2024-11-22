n = int(input("Введите размерность квадратной матрицы: "))

m = [[0] * n for i in range(n)]

for i in range(n):
    s = input(f"Введите элементы {i + 1} строки матрицы, разделяя значения элементов пробелом: ")
    c = list(map(int, s.split()))
    for j in range(n):
        m[i][j] = c[j]

print("Исходная матрица:")
for row in m:
    print(row)


 
for i in range(n):
    for j in range(i + 1, n):
        if m[j][i] != 0:  
            f = m[j][i] / m[i][i]
            for k in range(i, n):
                m[j][k] -= f * m[i][k]


 


print("Матрица в верхнеугольном виде:")
for row in m:
    print(row)
