try :
    userInput = int(input('Введите число: '))

    print(f"введенное число: {userInput}")
    print(f"число в двоичной СС: {bin((userInput))[2:]}")
    print(f"число в восьмеричной СС: {oct(userInput)[2:]}")

except ValueError:
    print("Неверный ввод!")


