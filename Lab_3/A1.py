x = 0
while x == 0: #цикл будет просить ввести координаты, пока пользователь не введет правильные данные
    try:
        x1, y1 = map(int, input('введите координаты первой точки (x1, y1): ').split(', '))
        x2, y2 = map(int, input('введите координаты второй точки (x2, y2): ').split(', '))
        x = 1
        if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0: 
            print('введите числа без нулей')
            x = 0 #если координаты нулевые цикл запускается заново 
    except:
        print('введите числа по образцу (x, y)')
if (x1 > 0 and y1 > 0) and (x2 > 0 and y2 > 0):
    dot = 'YES, I' 
elif (x1 < 0 and y1 < 0) and (x2 < 0 and y2 < 0):
    dot = 'YES, III'
elif (x1 < 0 and y1 > 0) and (x2 < 0 and y2 > 0):
    dot = 'YES, II'
elif (x1 > 0 and y1 < 0) and (x2 > 0 and y2 < 0):
    dot = 'YES, IV'
else:
    dot = 'NO'
print(dot)