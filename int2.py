# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys


if __name__ == '__main__':
# Определить принадлежит ли точка кольцу определяемому окружностями
     x = int(input('Введите координату Х'))
     y = int(input('Введите координату Y'))
     r1 = 1
     r2 = 0.25
     if x*x + y*y < 1 and x*x + y*y > 0.25:
        print("Точка принаждежит кольцу")
     else:
        print("Точка не принаждежит кольцу")
        
