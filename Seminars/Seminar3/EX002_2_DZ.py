# Тербуется вычислить сколько раз встречается некоторое число Х в массиве А[1..N]
# Пользователь в первой строке вводит натуральное число N - количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
import random
#
# n = int(input('Введите количество элементов в массиве: '))
# arr = list()
# for i in range(n):
#     arr.append(random.randint(1, 10))
# print(arr)
# x = int(input('Введите Х: '))
# count = 0
# for i in arr:
#     if i == x:
#         count += 1
# print(count)

# Требуется в массиве А[1..N] найти самый близкий по величине элемент к заданному числу Х.
# Пользователь вводит N - кол-во элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X.

# n = int(input('Введите количество элементов в массиве: '))
# arr = list()
# for i in range(n):
#     arr.append(random.randint(0,10))
# print(arr)
# x = int(input('Введите X: '))
# res = max(arr)
# count = 0
# for i in arr:
#     temp = abs(i - x)
#     if temp < res:
#         res = temp
#         count = i
# print(count)

# В настольной игре скраббл каждая буква имеет определенну ценность.
# В случае с английским алфавитом очки распределяются так: A,E,I,O,U,L,N,S,T,R = 1 очко
# D,G - 2 очка, B,C,M,P - 3 очка, F,H,V,W,Y - 4 очка, K - 5 очков, J,X = 8, Q,Z = 10
# А русские буквы оцениваются так: А,В,Е,И,Н,О,Р,С,Т = 1, Д,К,Л,М,П,У = 2, Б,Г,Ё,Ь,Я = 3
# Й,Ы = 4, Ж,З,Х,Ц,Ч = 5, Ш,Э,Ю - 8, Ф,Щ,Ъ = 10.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.

dictionary = {1: 'aeioulnstrAEIOULNSTRавеинорстАВЕИНОРСТ',
              2: 'dgDGдклмпуДКЛМПУ',
              3: 'bcmpBCMPбгёьяБГЁЬЯ',
              4: 'fhvwyFHVWYйыЙЫ',
              5: 'kKжзхцчЖЗХЦЧ',
              8: 'jxJXшэюШЭЮ',
              10: 'qzQZфщъФЩЪ'}
count = 0
word = input('Введите слово: ')
for item in word:
    for i in dictionary:
        for j in dictionary[i]:
            if j == item:
                count += i
print(count)
