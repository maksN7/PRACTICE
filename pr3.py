lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']  # Вхідний список із чисел та рядків

def function_lst_unique(lst):  # Функція для отримання унікальних елементів зі списку
    lst_unique = []
    lst2 = []
    for d in lst:  # Перебираємо всі елементи у списку
        if type(d) == str:
            d_lower = d.lower()
            lst2.append(d_lower)
        else:
            lst2.append(d)

    lst_in_set = set()
    for item in lst2:
        if item not in lst_in_set:  # Якщо елемента ще немає у множині
            lst_unique.append(item)
            lst_in_set.add(item)

    return lst_unique

def function_lst_sort(lst):  # Функція для сортування списку
    lst_str = []
    lst_int = []

    lst_sort = g.copy()
    for c in lst_sort:
        if type(c) == int:  # Якщо елемент - ціле число
            lst_int.append(c)  # Додаємо його до списку чисел
        elif type(c) == str:
            lst_str.append(c)

    lst_str.sort()
    lst_int.sort()

    return lst_int + lst_str  # Повертаємо об'єднаний список чисел і рядків


g = function_lst_unique(lst)

sorted_list = function_lst_sort(g)

print(sorted_list)
