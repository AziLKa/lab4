p = str

while (slovo := str(input("Enter a word: "))) != "stop":
    if "f" in slovo:
        print("Woooow! You have a relic word")
    else:
        print("it's regular word...")