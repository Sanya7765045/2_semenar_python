# Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Все целые? Бесконечность не предел?
# Целые числа (integer numbers) - это числа из множества целых чисел, которое включает в себя все натуральные числа (положительные целые числа), нуль и все отрицательные числа.

# Формально, множество целых чисел обозначается символом ℤ (Z) и включает числа следующего вида:

# {..., -3, -2, -1, 0, 1, 2, 3, ...}

# Целые числа представляются без дробной части или показателя степени и могут быть отрицательными, положительными или нулём.

# Примеры целых чисел:
# -5, -3, 0, 1, 100, 1000, и так далее.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# *ЦЕЛЫХ степеней тут вводи не хочу, развлекайтесь :)

def number():
    list_for_two = []  # Создаем пустой список, в который будем добавлять целые степени двойки
    temp = 0
    degree_of_two = int(input('Введите минимальную целую степень двойки:  -> '))  # Запрашиваем у пользователя минимальную степень двойки
    n = int(input('Введите максимальную целую степень двойки:  -> '))  # Запрашиваем у пользователя максимальную степень двойки

    while True:
        temp = 2 ** degree_of_two  # Вычисляем текущую степень двойки
        if degree_of_two <= n:  # Если текущая степень двойки не превосходит заданное значение n
            list_for_two.append(temp)  # Добавляем текущую степень двойки в список
            degree_of_two += 1  # Переходим к следующей степени двойки (увеличиваем значение degree_of_two на 1)
        else:
            break  # Если текущая степень двойки превысила значение n, выходим из цикла

    print(*list_for_two)  # Выводим список всех целых степеней двойки, не превосходящих значение n

number()


