 # ввод для изначальной задачи:   
    # while True:
    #     try:
    #         n = int(input('введите количество строк: '))
    #         m = int(input('введите количество столбцов: '))
    #         if n <= 0 or m <= 2:
    #             print('отказано')
    #         else:
    #             break
    #     except:
    #         print('введите лучше число')
    # sign = input('введите знак: ')
# програма принимает одно из трех названий фигур,
# просит ввести параметры ,а после выводит полученное в терминале
# также программа не завершается сразу, а спрашивает у пользователя
# хочет ли он продолжить, в зависимости от ответа программа
# или запускается заново или завершается
def draw_rectangle(rows, columns, ch): #функция прямоугольника
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print('')
#    draw_rectangle(n, m, sign)
def draw_triangle(rows, ch): #функция треугольника
    x = 1
    for i in range(rows):
        columns = ch * x
        print(columns)
        x += 1
#    print('')
#    draw_triangle(n, sign)
def draw_frame(rows, columns, ch): #функция рамки
    line = ch * columns # целая линия без пробелов
    print(line) #"крыша" рамки
    pass_columns = columns - 2 #колво столбцов с пробелами
    pass_rows = rows - 2 #колво строк с пробелами
    pass_columns_line = " " * pass_columns #пробелы из "окошка"
    for i in range(pass_rows):
        print(ch, pass_columns_line, ch, sep="")
    print(line) #"пол" рамки
#    print('')
#    draw_frame(n, m, sign)
while True:
    while True: #цикл для полчения фигуры
        figure = input('введите фигуру (прямоугольник, треугольник, рамка): ')
        if figure == "прямоугольник":
            break
        elif figure == "треугольник":
            break
        elif figure == "рамка":
            break
        else:
            print('выберите одну из трех фигур')
    while True: #цикл для получения колва строк
        try:
            n = int(input('введите количество строк: '))
            if n <= 0:
                print('отказано')
            else:
                break
        except:
            print('введите лучше число')
    while True: #цикл для полученя колва столбцов
        if figure != 'треугольник': #для треугольника столбцы не нужны 
            try:
                m = int(input('введите количество столбцов: '))
                if m <= 2:
                    print('отказано')
                else:
                    break
            except:
                print('введите лучше число')
        else:
            break
    sign = input('введите знак: ')
    if figure == "прямоугольник":
        draw_rectangle(n, m, sign)
    elif figure == 'треугольник':
        draw_triangle(n, sign)
    elif figure == 'рамка':
        draw_frame(n, m, sign)
    while True: #цикл для получения одного из двух значений
        end = input('хотите еще? (да, нет): ')
        if end == 'да' or end == 'нет':
            break
        else:
            print('введите по образцу')
    if end == 'нет': #для завершения программы
        break
