import random
count = 0

while (count != 3):
    numberone = random.randint(1, 9)
    numbertwo = random.randint(1, 9)
    otvet = input(str(numberone) + "+" + str(numbertwo) + "=")
    if int(otvet) == (numberone + numbertwo):
        print("great!")
    elif int(otvet) != (numberone + numbertwo):
        count += 1
        print("wrong!")