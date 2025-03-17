def task6_2(x):
    try:
        return 100/int(x)
    except ValueError:
        return("Ошибка! ValueError!")
    except ZeroDivisionError:
        return("Ошибка! Деление на ноль!")
x=input("Введите число: ")
print(task6_2(x))
