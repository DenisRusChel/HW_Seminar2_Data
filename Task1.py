# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_nechet(x):
    sum = 0
    for i in range(len(x)):
        if i % 2 == 1:
            sum += list_1[i]
    print(sum)


x = list_1 = [2, 3, 5, 9, 3, -1, 1]
sum_nechet(x)
