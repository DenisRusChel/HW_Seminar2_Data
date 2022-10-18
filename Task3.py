# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



def diff_parts(list_1):
    list_2=[]
    for i in list_1:
        i %= 1 
        n = round(i, 2)
        list_2.append(n)
    print(f'{list_1} → {max(list_2) - min(list_2)}')


list_1 = [1.1, 1.2, 3.1, 5.1, 10.01]
diff_parts(list_1)