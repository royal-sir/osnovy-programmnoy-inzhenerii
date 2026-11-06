import string
password = input('введите пароль для проверки: ')
x = 0 
if len(password) < 8: #длинна пароля
    print('длина пароля не равна 8')
    x += 1
if password.lower() == password: #проверка на верхний регистр
    print('в пароле отсутствуют заглавные буквы')
    x += 1
if password.upper() == password: #проверка на нижний регистр
    print('в пароле отсутствуют строчные буквы')
    x += 1
if not any(symbol.isdigit() for symbol in password): #цифра
    print('в пароле отсутствуют цифры')
    x += 1
allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits + '*-#'
if not all(symbol in allowed for symbol in password): #допустимые
    print('в пароле отсутствуют специальные символы')
    x += 1
ssym = '*-#'
if not any(symbol in ssym for symbol in password):
    print('в пароле отсутствуют специальные символы')
    x += 1
if x == 0:
    print('надежный пароль')