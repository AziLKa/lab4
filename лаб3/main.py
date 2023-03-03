N = int(input("Сколько слов вы хотите ввести?: "))
p = ""

for i in range(N):
    slovo = str(input("Введите слово: "))
    p = p + " " + slovo

print(p)