# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = int(input('Введите целое положительно число:'))
m = a % 10
while a>=1:
    a = a//10
    if a % 10 >m:
        m=a%10
    if a>0:
        continue
    else:
        print('Максимальная цифра в числе:' , m )
    break
