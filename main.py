per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent.values()

b = list(a)
deposit = b
money = 100000
deposit = [float(x) * money /100 for x in b]
print('deposit = ', deposit)
print ("Максимальная сумма, которую вы можете заработать - ", max(deposit))