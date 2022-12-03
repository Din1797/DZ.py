#1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

#n = int(input('Введите День недели:'))
#if n < 1 or n > 7:
    #print('Ввели неверное число!')
#elif n > 5:
   # print('этот день выходной!')
#else:
   # print('это рабочий день!')


#2.Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#  ⋀ - and ⋁ - or ¬ - not
print('Утверждение истино при: ')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y or z)) == (not x and y and not z):
                print (f'x = {bool(x)},\t y = {bool(y)},\t z ={bool(z)}')
        


#3.Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3     

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))
def inputKoord (x):
    x == [0] * x
    for i in range (x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Error! Введите пожалуйста числа!")
    return 
def Coordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    elif xy[0] > 0 and xy[1] < 0:
        text = 4
    print(f"Точка находится в {text} четверти плоскости")



#4.Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os
os.system('cls')
quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('x > 0, y > 0')
elif quarter == 2:
    print('x < 0, y > 0')
elif quarter == 3:
    print('x < 0, y < 0')
elif quarter == 4:
    print('x > 0, y < 0')
else:
    print('На координатной плоскости только 4 четверти')

#5.Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
x_cordinate_A = float(input('Введите координату точки A по оси X: '))
y_cordinate_A = float(input('Введите координату точки A по оси Y: '))
x_cordinate_B = float(input('Введите координату точки B по оси X: '))
y_cordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = (((x_cordinate_B - x_cordinate_A)**2 + (y_cordinate_B - y_cordinate_A)**2)**0,5)
print(distance)