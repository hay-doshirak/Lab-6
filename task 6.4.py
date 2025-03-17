def task6_4_happyticket(ticket):
    sum1 = int(ticket[0])+int(ticket[1])+int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2:
        return "Это счастливый билет!"
    else: return "Это обычный билет..."
ticket = input("Введите номер билета: ")
print(task6_4_happyticket(ticket))