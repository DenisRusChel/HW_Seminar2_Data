# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


def multiplication(list_):
    list_2 = []
    l = len(list_1)

    for i in list_1:
        num = i * list_1[l-1]
        l -=1
        if l < len(list_1)//2: break
        list_2.append(num)
    print(list_2)

list_1 = [2, 3, 4, 5, 6, 2, -1, -3]
multiplication(list_1)