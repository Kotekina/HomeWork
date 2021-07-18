# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

total = int(input("Введите время в секундах"))
hours = total//3600
minutes = ((total-3600*hours)//60)
seconds = total-hours*3600-minutes*60

print(f'{hours}:{minutes}:{seconds}')



