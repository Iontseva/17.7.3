per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input('Введите сумму вклада: ')

deposit_a = int(per_cent['ТКБ'] * int(money)/100)
deposit_b = int(per_cent['СКБ'] * int(money)/100)
deposit_c = int(per_cent['ВТБ'] * int(money)/100)
deposit_d = int(per_cent['СБЕР'] * int(money)/100)
deposit=[deposit_a, deposit_b, deposit_c, deposit_d]

print('Максимальная сумма, которую вы можете заработать:', max(deposit))
