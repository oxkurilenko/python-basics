import math

figure = input('Введите тип фигуры:')
if figure == 'круг':
    radius = int(input('Введите радиус круга:'))
    area = math.pi * (radius * radius)
    print('Площадь круга:' + str(round(area, 2)))
elif figure == 'треугольник':
    a = int(input('Введите длину стороны A:'))
    b = int(input('Введите длину стороны B:'))
    c = int(input('Введите длину стороны C:'))
    p = (a + b + c) / 2
    area = math.sqrt((p * (p - a) * (p - b) * (p - c)))
    print('Площадь треугольника:', str(round(area, 2)))
elif figure == 'прямоугольник':
    a = float(input('Введите длину стороны AB:'))
    b = float(input('Введите ширину стороны BС:'))
    area = a * b
    print('Площадь прямоугольника:' + str(round(area, 2)))