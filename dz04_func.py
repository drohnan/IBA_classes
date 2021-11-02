# функция переводит км в мили
def convert_to_miles(km):
    return km * 0.6214

# возвращает количество дней в месяце
def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# возращает список делителей числа
def get_factors(num):
    return list([i for i in range(1, num + 1) if num % i == 0])

# проверяет, является ли число простым
def is_prime(num):
    flag = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if num > 1 and flag == True:
        return True
    else:
        return False