while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Ваш билет счастливый!')
        else:
            print('Ваш билет не счастливый')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз')