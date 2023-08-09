'''
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
'''
from random import randint

coinCount = int(input('Введитн количество монет '))

coins = []
orelCount = 0
reshkaCount = 0
for i in range(coinCount):
    coins.append (randint(0, 1))
    if coins[i] == 0:
        reshkaCount += 1
    else:
        orelCount += 1

print(coins)
if reshkaCount > orelCount:
    print('Необходимо перевернуть', orelCount, 'монет с орла на решку')
else:
    print('Необходимо перевернуть', reshkaCount, 'монет с решки на орла')

