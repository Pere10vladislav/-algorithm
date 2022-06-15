import math

def binary_search(list, item):
    #Обьявляем переменную мин и макс (в первой интерации это первый елемент списка и последний)
    low = 0
    high = len(list) - 1

    #Запускачем цикл пока элемент не останится один
    while low <= high:
        mid = math.floor((low + high) / 2)
        guest = list[mid]
        if guest == item:
            return mid
        if guest > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(binary_search(my_list, 7))
