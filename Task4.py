# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binary_number(n):
    if n > 1:
        binary_number(n//2)
    print(n%2, end='')

binary_number(45)
