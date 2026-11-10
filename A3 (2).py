import string
while True: #цикл будет просить ввести данные, пока пользователь не введет подходящие
    x = 0 #колисество ошибок
    packets = input("введите последовательных пакетов данных: ")
    if not all(char in '01' for char in packets):
        print('только нолики и единицы')
        x = 1
    if len(packets) < 5:
        print('попробуйте ввести больше 5')
        x = 1
    if x == 0:
        break
count = len(packets) #количество пакетов
count_0 = packets.count('0') #количество потеряных пакетов
prev_packet = None #предыдущий пакет
seq_0 = 0 #последовательность нулей
for packet in packets:
    if prev_packet == None:
        prev_packet = packet
    if packet == "0":
        if seq_0 == 0:
            seq_0 = 1
        if prev_packet == packet:
            seq_0 += 1
    prev_packet = packet
persent = (count_0 / count) * 100
persent = round(persent, 2) #округляет до двух знаков посде точки
print('общее количество пакетов:', count)
print('количество потерянных пакетов:', count_0)
print('длина самой длиной последовательности потерянных пакетов:', seq_0)
print('процент патерь: ', persent, '%', sep="")
if persent <= 1:
    print('качество связи: отличное качество')
elif persent <= 5:
    print('качество связи: хорошее качество')
elif persent <= 10:
    print('качество связи: удовлетворительное качество')
elif persent <= 20:
    print('качество связи: плохое качество')
else:
    print('качество связи: критическое состояние сети')