# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Вариант 1 (математический, неточный)
print('Введите число: ')
numb1 = float(input())
numb = numb1
if numb < 0:
    numb = numb * (-1)
while (numb % 1) != 0:
    numb = numb * 10
sum = 0
while numb > 0:
        sum = sum + numb % 10
        numb = int(numb // 10)
print(numb1,' -> ',sum)

# Вариант 2 (через строку)
print('Введите число: ')
str1 = str(input())
sum = 0
for elem in str1:
    if elem.isdigit():
        sum = sum + int(elem)
print(str1,' -> ',sum)