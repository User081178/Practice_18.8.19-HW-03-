
price_disc = 1
total_price = 0
#--------- Ввод кол-ва билетов со стороны пользователя

while True:
    try:
        ticket_num = int(input('Сколько билетов вы хотите приобрести ?:'))
        
        if ticket_num:
            break
    except ValueError:
        print('Неверный ввод ! Введите целое число.')
        
if ticket_num > 3:
    price_disc = .9
    print ('Для Вас скидка 10 % !')

#---------Запрос возраста посетителя для каждого билета 

for i in range(ticket_num):
    i+= 1
    while True:
        try:
            ticket_age = int(input(f'Для какого возраста билет № {i} ? :'))
        
            if ticket_age < 18:
                print(f'Билет №{i} -  бесплатный')
            elif 25 > ticket_age >= 18:
                total_price += 990
                print(f'Стоимость билета № {i} -  990 руб.')
            else:
                total_price += 1390
                print(f'Стоимость билета № {i} -  1390 руб.')
            if ticket_age:
                break
        except ValueError:
            print('Неверный ввод ! Введите целое число.')

#---------Вывод общего кол-ва билетов + итоговая сумма с учетом скидки
print ('-------------------------')
print()
print (f'Количество приобретаемых билетов - {ticket_num}')
print(f'Итоговая стоимомть с у - {total_price * price_disc} руб.')
