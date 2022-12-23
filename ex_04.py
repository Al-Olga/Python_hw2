# Реализуйте алгоритм перемешивания списка.
import random

list1 = [3, 7, 1, 0, 6, 4]
list2 = list1[:]
for i in range(len(list2)):
        index_random = random.randint(0, len(list2) - 1)
        temp = list2[i]
        list2[i] = list2[index_random]
        list2[index_random] = temp
print("Исходный список: ")
print(list1)
print("Перемешанный список: ")
print(list2)