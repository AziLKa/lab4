god = int(input("Введите god"))

if (god % 4 == 0) and (god % 100 != 0) or (god % 400 == 0):
    b=f"Поздравляю! {god} високосный год!"
    print(b)
else:
    print("meh...")