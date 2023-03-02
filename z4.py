color1 = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if (color1 != "red") and (color1 != "yellow") and (color1 != "blue"):
    print("КРАСНЫЙ, ЖЕЛТЫЙ ИЛИ СИНИЙ!??!? Заново вводи")
elif (color2 != "red") and (color2 != "yellow") and (color2 != "blue"):
    print("КРАСНЫЙ, ЖЕЛТЫЙ ИЛИ СИНИЙ!??!? Заново вводи")
elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
    print("Оранж!!!!!!")
elif color1 == "red" and color2 == "blue" or color1 == "blue" and color2 == "red":
    print("Маджэнта!!!!!!")
elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
    print("Грииин!!!!!!")