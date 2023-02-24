# Задача 3: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input('Введите номер билета:'))
sum1 = 0
sum2 = 0
if 99999<number<1000000:
    while number > 999:
        sum2 = sum2 + number%10
        number = number//10
    while number > 0:
        sum1 = sum1 + number%10
        number = number//10
    if sum1 == sum2:
        print('Ваш билет счастливый!')
    else:
        print('Ваш билет несчастливый!')
else:
    print('Введен неверный номер билета!')