#name_patient = input('Ф.И.О: ')

weight = input('Вес (кг): ')
height = input('Рост (см): ')

print('Рост: ',height,'см, ','Вес: ',weight,' кг.')
BSA = 0.007184 * (int(weight)**0.425) *(int(height) **0.725)

day_start =input('День начала курса (дд): ')
month_start = input('Месяц начала курса (мм): ')
year_start = input('Год начала курса (гг/гггг): ')

print('Дата начала курса: ',day_start,'.',month_start,'.',year_start,'.')

time_start = input('Время начала курса (чч.мм): ')

rotation = input('Ротация антрациклинов? (да/нет): ')


day_one = day_start,month_start,year_start
day_two = int(day_start)+1,month_start,year_start
day_three = int(day_start)+2,month_start,year_start
day_four = int(day_start)+3,month_start,year_start
day_five = int(day_start)+4,month_start,year_start
day_six = int(day_start)+5,month_start,year_start
day_seven = int(day_start)+6,month_start,year_start

ara_c = round(BSA*200)
dauno = round(BSA*60)

print('1) ','Цитарабин ',ara_c,' мг + 0,9% NaCl 500 мл в/в через инфузомат '
                               'круглосуточно со скоростью v = 20,8 мл/ч','в ', time_start)
print(day_one, end = '    ')
print(day_two, end = '    ')
print(day_three)
print(day_four, end = '    ')
print(day_five, end = '    ')
print(day_six)
print(day_seven)


print('2) ','Даунорубицин',dauno,' мг + 0,9% NaCl 500 мл в/в капельно в')

if rotation == 'нет' or rotation == 'no':
    print(day_one, end = '    ')
    print(day_two, end = '    ')
    print(day_three)
if rotation == 'да' or rotation == 'yes' or rotation ==  'y':
    print(day_five, end='    ')
    print(day_six, end='    ')
    print(day_seven)