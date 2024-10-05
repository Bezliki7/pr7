try :
    a = int(input('Введите число для аргумента a: '))
    b = int(input('Введите число для аргумента b: '))
    c = int(input('Введите число для аргумента c: '))   

    x = 7*b + 2*c - a

    print(f"Ответ: {x}")
except ValueError:
    print("Неверный ввод!")


