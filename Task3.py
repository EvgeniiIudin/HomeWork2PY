# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

# N = random.randrange(1,10)    можно и через рандомную длину массива!!!!

N = int(input('Задайте длину массива: '))
a = [random.randrange(-10, 10) for i in range(N)]
print("N = ", N)
print("Array:\n", a)
M = 0
for x in a:
    if x < 0:
        M += 1
a.extend([0]*M)
j = 0
for i in range(N-1, -1, -1):
    if a[i] < 0:
        a[(N+M-1)-j] = 0
        j += 1
    a[(N+M-1)-j] = a[i]
    j += 1
print("New Array:\n", a)