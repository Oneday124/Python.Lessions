# Сколько дней длилась самая длинная оттепель. Оттепель = температура > 0 градусов.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит N - количество дней. (1<= N <=100)
# В следующих строках располагается N целых числел.
# Каждое число - среднесуточная температура
# Температуры лежат в диапазоне от -50 до 80 (целые числа)

# import random
#
# N = int(input('Введите количество дней от 1 до 100: '))
# count = 0
# day_max = 0
# for i in range(N):
#     day_temp = random.randint(-50, 50)
#     if day_temp > 0:
#         count += 1
#     else:
#         if day_max < count:
#             day_max = count
#         count = 0
# if day_max < count:
#     day_max = count
# print(day_max)

# Иван решил купить 2 арбуза, 1 себе, второй теще. Арбуз для себя тяжелее. Арбузов много, нужно выбрать самый легкий и
# самый тяжелый. Пользователь вводит N - количество арбузов.
# Вторая строка содержит N чисел записанных на новой строчке каждое (число = масса арбуза)
# Все числа натуральные и не превышают 30 000

import random

n = int(input("Введите количество арбузов: "))
max = 0
min = 30000
for i in range(n):
    temp = random.randint(3000, 30000)
    print(temp)
    if temp > max:
        max = temp
    if temp < min:
        min = temp
print(f'Минимальный вес: {min}\nМаксимальный вес: {max}')



