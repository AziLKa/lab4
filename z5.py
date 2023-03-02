import random
p = ""

number = random.randint(1, 10)
for i in range(number):
    slovo = str(input("введите слово: "))
    p = p + " " + slovo

print(p)
