print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
print()

if first_number > second_number and first_number > third_number:
  print('Первое число максимальное')
elif second_number > first_number and second_number > third_number:
  print('Второе число максимальное')
elif third_number > first_number and third_number > second_number:
  print('Третье число максимальное')
else:
  print('Числа равны')

exit()
