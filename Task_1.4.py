# Не понял как решить это математически.
# Если бы в условиях была задана разрядность исходного числа, то я бы смог.
# Команду "list" подсмотрел в интернете, а "max" - по логике (угадал, не знал, что есть такая команда :-) )
x = input('Введите любое целое положительное число: ')
while(int(x) <= 0):
    print('Вы ввели отрицательное или число, которое равно нулю!')
    x = input('Введите любое целое положительное число: ')

y = max(list(str(x)))
print('Самая большая цифра заданного Вами числа', x, 'равна =', y)