x = 0
while x == 0: #цикл будет просить ввести значения, пока пользов. не введет правильные данные
    try:
        prev_val = int(input('введите предыдущее значение: '))
        cur_val = int(input('введите текущее значение: '))
        if prev_val > cur_val: #если счетчик обнулился
            prev_val += 10000
        x += 1
        if prev_val > 9999 or cur_val > 9999: #область значений счетчика
            print('введите значение до 9999')
            x = 0
    except: #если польз. введет строку 
        print('введите цифорки')
used = cur_val - prev_val 
remainder = 0 #промежуток между 300 и 600
remainder2 = 0 #промежуток между 600 и 800
remainder3 = 0 #все после 800
if used > 300:
    remainder = used - 300
    if used > 600:
        remainder2 = used - 600
        remainder = 300
        if used > 800:
            remainder3 = used - 800
            remainder2 = 200 
cost = 21 + remainder * 0.06 + remainder2 * 0.04 + remainder3 * 0.025
if used != 0:
    avg = cost / used
    avg = round(avg, 2)
else:
    avg = 'фикс цена'
print('предыдущее: ', prev_val, ' текущее: ', cur_val, ' использовано: ', used, ' к оплате: ', cost, ' сред. цена m^3: ', avg)