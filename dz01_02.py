"""
Вариант 6.
Bыполнить задание без хранения последовательностей. Дано натуральное k.
Определить k-ю цифру последовательности: 1248163264 ..., в которой выписаны подряд степени 2.
"""
k = int(input("Введите k: "))

stroka = "" # сюда будем записывать числа нашей последовательности

for i in range(k):  # Выбираем границу до k потому что до пяти k-ая цифра будет совпадать с количеством цифр в последовательности
                    # то есть: k == 0 -- 1 (1 цифра); k == 1 -- 2 (1 цифра) .. k == 5 -- 16 (2 цифры) ...
    stroka += str(2**i)
print("Наша последовательность:", stroka, sep="\n")

for j in range(1, k):    # Зачем-то захотел сделать указатель стрелку на k-й элемент
    print(" ", end="")
print("^", end="\n")

print(f"{k}-й элемент: {stroka[k-1]}") # Я решил, что мы все же считаем элементы с первого, а не с нулевого, как Питахон