# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d10-10


import math
d = float(input("Введите точность: "))
a = int(math.log10(1/d))
pi = 0
for i in range(10000):
    pi += (-1)**i/((2*i) + 1)*4     # формула для вычисления пи
pi = str(pi)
pi = pi[:a+2]
print(pi)

# 30*** , Подумать, что если точность вычисления до 1000 знаков после запятой
# https://habr.com/ru/post/309674/