
tickets = int(input('Сколько Вам надо билетов  '))

age = [int(input('Ваш возраст ')) for i in range(tickets)]
sum = 0
for i in range(len(age)):
    if age [i] < 18:
        sum = 0
        tickets = tickets - 1
        print('Всем, кому нет 18 могут пройти без билета')
    elif 18 <= age [i] <= 25:
        sum = sum + 990
        #print(sum)
    else:
        sum = sum + 1390
        #print(sum)
if tickets  > 3 :
        print ('Вам скидка 10 %')
        All_sum = sum * 0.9
        print (All_sum)
else:
    print('Вам без скидки')
    print ('Сумма за билеты : ',sum)