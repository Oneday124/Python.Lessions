# На столе лежат n монет. Некоторые лежат вверх решкой, некоторые гербом
# Определите минимальное количество монет, которые нужно перевернуть,
# чтобы все монеты были повернуты вверх одной стороной
# import random
#
# n = 5
# up = 0
# down = 0
#
# for i in range(n):
#     temp = random.randint(0, 1)
#     print(temp)
#     if temp == 1:
#         up +=1
#     if temp == 0:
#         down +=1
# print(f'Нужно перевернуть {min(up,down)} монеты')

# Петя помогает Кате с математикой. Задумывает 2 натуральных числа X и Y (<=1000)
# Катя должна отгадать числа. Петя называет сумму чисел S и произведение P. Помогите Кате отгадать числа

# S = int(input('Введите сумму чисел: '))
# P = int(input('Введите произведение чисел: '))
# x = 0
# y = 0
# for i in range(1, P):
#     if S - i == P / i:
#         x = i
#         y = S-i
# print(f'Число X = {x}\nЧисло Y = {y}')

# Вывести все целые степени двойки, не превосходящие числа N

N = int(input("Введите N: "))
for i in range(N):
    if 2**i <= N:
        print(2**i)