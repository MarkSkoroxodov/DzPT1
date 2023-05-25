S = int(input("Введите общее количество журавликов: "))
if not S % 6:
     x = S // 6
     print(f'Катя {x * 4} ')
     print(f'Сережа {x} ')
     print(f'Петя {x}')