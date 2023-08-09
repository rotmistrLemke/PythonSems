'''
Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
'''
import math

N = int(input('Введитн число N '))
count = 0
a = 0
res = []
while a < N:
       a = pow(2,count)
       if a < N:
            res.append (a)
       count += 1
print(res)
