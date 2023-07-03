# # Задание 1
# a = input('Введите числа через пробел:\n')
# a = list(map(int, a.split()))
# print('Среднее арифметическое = ', sum(a)/len(a))
#
# # Задание 2
# import math
# r = int(input('Введите радиус круга:\n'))
# s = math.pi * r**2
# print('Площадь круга = ', s)
#
# # Задание 3
# fig = int(input('Выберите фигуру:\n1 - Круг\n2 - Прямоугольник\n3 - Овал\n4 - Ромб\n5 - Пятиугольник\n6 - Шестиугольник\n'))
#
#
# def f1():
#     r = int(input('Введите радиус круга:\n'))
#     s = math.pi * r ** 2
#     print('Площадь круга = ', s)
#     return
#
# def f2():
#     d = int(input('Введите длину:\n'))
#     v = int(input('Введите высоту:\n'))
#     s = d * v
#     print('Площадь прямоугольника = ', s)
#     return
#
# def f3():
#     pb = int(input('Введите большую полуось:\n'))
#     pm = int(input('Введите малую полуось:\n'))
#     s = math.pi * pb * pm
#     print('Площадь овала = ', s)
#     return
#
# def f4():
#     d1 = int(input('Введите первую диагональ ромба:\n'))
#     d2 = int(input('Введите вторую диагональ ромба:\n'))
#     s = (d1 * d2)/2
#     print('Площадь ромба = ', s)
#     return
#
# def f5():
#     r = int(input('Введите радиус вписанной окружности:\n'))
#     s = 5 * r**2 * math.tan(math.pi/5)
#     print('Площадь пятиугольника = ', s)
#     return
#
# def f6():
#     r = int(input('Введите радиус вписанной окружности:\n'))
#     s = 2 * math.sqrt(3) * r**2
#     print('Площадь шестиугольника = ', s)
#     return
#
# match fig:
#     case 1: f1()
#     case 2: f2()
#     case 3: f3()
#     case 4: f4()
#     case 5: f5()
#     case 6: f6()


# # Задание 4
# import random
# name = ['ivan', 'petr', 'sergey', 'igor', 'evgen']
# prof = ['slesar', 'programmist', 'ingener', 'voditel', 'uchitel']
# city = ['moscow', 'ufa', 'e-burg', 's-peterburg', 'voronej']
#
# persons = {}
# for i in range(5):
#     n = random.randint(0, len(name)-1)
#     p = random.randint(0, len(prof)-1)
#     c = random.randint(0, len(city)-1)
#     m = {'name': name[n], 'prof': prof[p], 'city': city[c]}
#     name.pop(n)
#     prof.pop(p)
#     city.pop(c)
#     person_num = 'person' + str(i + 1)
#     persons.update({person_num: m})
#
# for i in persons:
#     print(i, persons[i])
#
#
# # Задание 5
# moves = ['К', 'Н', 'Б']
# win = ['КН', 'БК', 'НБ']
# fail = ['НК', 'КБ', 'БН']
# things = ['Камень', 'Ножницы', 'Бумага']
# schet = [0, 0]
# while True:
#     move = input('Ваш выбор:\nК - Камень\nН - Ножницы\nБ - Бумага\n0 - Выйти из игры\n').upper()
#     if move == 0:
#         break
#     move_comp = random.randint(0, 2)
#     if move + moves[move_comp] in win:
#         schet[0] += 1
#         print('Выбор соперника', things[move_comp], 'Вы выиграли! Счёт:', ':'.join(map(str, schet)))
#     elif move + moves[move_comp] in fail:
#         schet[1] += 1
#         print('Выбор соперника', things[move_comp], 'Вы проиграли. Счёт:', ':'.join(map(str, schet)))
#     else:
#         print('Ничья. Счёт:', ':'.join(map(str, schet)))

# Задание 6
import random

number = ''
for i in range(4):
    number += str(random.randint(0, 9))
print(number)
while True:
    guess = input('Введите 4 цифры без пробелов:\n')
    k = 0
    b = 0
    for i in range(len(number)):
        if guess[i] in number:
            if guess[i] == number[i]:
                b += 1
            else:
                k += 1
    if b == 4:
        print('Вы угадали!')
        break
    else:
        print('Коров:', k, 'Быков:', b)
