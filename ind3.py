import sys


if __name__ == '__main__':
# Одноклеточная амеба каждые три часа делится на 2 клетки. Определить, сколько будет клеток через 6 часов.
f = 1
n = int(input('Введите кол-во часов'))
u = n // 3
f = f*u
print(f)
