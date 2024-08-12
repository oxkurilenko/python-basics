
year = int(input('Введите год:'))
x= year
if (x) % 4 == 0 and (x) % 100 != 0:
    print ('Високосный год')
elif (x) % 400 == 0:
    print ('Високосный год')
else :
    print ('Обычный год')