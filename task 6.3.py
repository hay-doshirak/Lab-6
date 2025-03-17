def task6_3_magic(date):
    day = int(date[:2:])
    month = int(date[2:4:])
    last_num = int(date[-2:])
    if day*month == last_num:
        return True, "Дата магическая."
    else: return False, "Волшебства не ждите."
print("Является ли дата магической?")
date = input("Ведите дату (DD.MM.YYYY): ")
date = date.replace(".","")
print(task6_3_magic(date))