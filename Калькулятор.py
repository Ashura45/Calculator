# Запрашиваем у пользователя два числа и знак операции
numb_1 = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))
sign = input('Введите знак: ')
# Создаем бесконечный цикл, который будет продолжаться, пока пользователь не введет "ЗАКОНЧИТЬ"
while True:
    # Выполняем операцию в зависимости от введенного знака
    if numb_2 == 0 and sign == '/':
        print('На ноль делить нельзя')
    elif sign == '+':
        print(numb_1, sign, numb_2, '=', numb_1 + numb_2)
        result = numb_1 + numb_2
    elif sign == '-':
        print(numb_1, sign, numb_2, '=', numb_1 - numb_2)
        result = numb_1 - numb_2
    elif sign == '*':
        print(numb_1, sign, numb_2, '=', numb_1 * numb_2)
        result = numb_1 * numb_2
    elif sign == '/':
        print(numb_1, sign, numb_2, '=', numb_1 / numb_2)
        result = numb_1 / numb_2
    elif sign == '**':
        print(numb_1, sign, numb_2, '=', numb_1 ** numb_2)
        result = numb_1 ** numb_2
    elif sign == '//':
        print(numb_1, sign, numb_2, '=', numb_1 // numb_2)
        result = numb_1 // numb_2
    elif sign == '%':
        print(numb_1, sign, numb_2, '=', numb_1 % numb_2)
        result = numb_1 % numb_2
    else:
        print('Ошибка ввода переменной')

    # Запрашиваем у пользователя, хочет ли он перезапустить программу
    TF = input('Перезапуск? ДА или НЕТ ')
    TF = TF.lower()
    # Если пользователь вводит "ДА" или "да", "YES" или "yes", то запрашиваем новые числа и знак
    if TF in ['да', 'yes']:
        numb_1 = int(input('Введите первое число: '))
        numb_2 = int(input('Введите второе число: '))
        sign = input('Введите знак: ')

    # Если пользователь вводит "НЕТ" или "нет", "NO" или "no", то запрашиваем, хочет ли он продолжить с текущим выражением или закончить программу
    elif TF in ['нет', 'no']:
        end_or_contin = input(
            'Хотите продолжить с текущим выражением или хотите завершить программу? ПРОДОЛЖИТЬ или ЗАКОНЧИТЬ ')
        end_or_contin = end_or_contin.lower()
        # Если пользователь вводит "ЗАКОНЧИТЬ" или "закончить", "END" или "end", то прерываем цикл
        if end_or_contin in ['закончить', 'end']:
            break

        # Если пользователь вводит "ПРОДОЛЖИТЬ" или "продолжить", то продолжаем цикл с текущим выражением
        elif end_or_contin in ['продолжить', 'continue']:
            numb_1 = result
            numb_2 = int(input('Введите второе число: '))
            sign = input('Введите знак: ')
