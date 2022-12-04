# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# list = [2, 3, 5, 9, 3]
# list2 = []
# for idx, num in enumerate(list):
#     if idx % 2 != 0:
#         list2.append(num)
# print(f' Сумма чисел на нечетных позициях - {sum(list2)} ')

# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
# import random
# dlinna = int(input('Введите длинну: '))
# visota = int(input('Введите высоту: '))
# res = []
# for num in range(visota):
#     res.append(list())
#     for num_sec in range(dlinna):
#         res[num].append(random.randint(0, 10))
#     print(f'{res[num]}')

# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
# from random import randint
# arr = []
# for i in range(30):
#     arr.append(randint(1, 99))
# lst = []
# i = 0
# maxi = 0
# while i < len(arr) - 1:
#     for num in arr:
#         if num > maxi:
#             maxi = num
#     lst.append(maxi)
#     arr.remove(maxi)
#     maxi = 0
#     i += 1
# lst.append(arr[0])
# print(lst[::-1])














