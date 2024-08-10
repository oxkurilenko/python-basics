width = int(input('Введите ширину в см:'))
length =int (input('Введите длину в см:'))
height =int (input('Введите высоту в см:'))
if (width) == (length) == (height) <= 15:
    print('Короба № 1')
elif (width) >= 200 or (length) >= 200 or (height) >= 200:
    print('Упаковка для лыж')
elif (width) >= 15 <= 50 or (length) >= 15 <= 50 or (height) >= 15 <= 50:
    print('Короба № 2')
else :
    print('Короба № 3')