import random 
import time
while True: #цикл будет просить ввести данные, пока пользователь не введет подходящие
    try:
        N = int(input("введите количество примеров: "))
        if N <= 0:
            print("отказано")
        else:
            break
    except: #если пользователь введет строку
        print("введите число")
all_time = 0 #все вркемя, затраченное на примеры 
r_ans = 0 #правильных ответов
q = 1 #вопрос
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    x = 0
    print(F'вопрос {q}\\{N}')
    q += 1
    while True:
        try:
            ans = int(input(F"{a} × {b} = "))
            break
        except:
            print("введите число")
    spend_time = time.time() - start_time
    spend_time = round(spend_time, 2)
    all_time += spend_time
    sol = a * b #какой должен быть ответ
    if sol == ans:
        print(F'верно 😍 (время:{spend_time})')
        r_ans += 1
    else:
        print(F'неверно 😔 правильно:{sol} (время:{spend_time})')
avg_time = all_time / N #сред время
avg_time = round(avg_time, 2) #округление до 2 знаков после запятой
per = (r_ans / N) * 100 #процент правильных примеров
per = round(per, 2) #округление до 2 знаков после запятой
print('===========================================')
print('СТАТИСТИКА:')
print('===========================================')
print("общее время:", all_time)
print('среднее время на вопрос:', avg_time)
print(F'правильных ответов: {r_ans}\\{N}')
print('процент правильных: ', per, '%', sep="")