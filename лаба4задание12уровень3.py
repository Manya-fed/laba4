
n = int(input("Введите размерность квадратной матрицы: "))

a = [[0] * n for i in range(n)]

for i in range(n):
    s = input(f"Введите элементы {i + 1} строки матрицы, разделяя значения элементов пробелом: ")
    c = list(map(int, s.split()))
    for j in range(n):
        a[i][j] = c[j]

print("Исходная матрица:")
for row in a:
    print(row)


for j in range(n - 1):
    for k in range(j + 1, n):
        for m in range(j, n):
            a[k][m] = a[k][m] - a[j][m] * a[k][j] // a[j][j]


print("Результирующая матрица:")
for row in a:
    print(row)
