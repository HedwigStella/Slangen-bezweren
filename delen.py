def delen (x, y):
    return x / y

print("kies 1 om te delen")
print("1.delen")

while True: 
    keuze = input ("vul uw keuze in")

    if keuze in '1':
    num1 = float(input("Voer uw eerste nummer in: "))
    num2 = float(input("Voer uw tweede nummer in: "))
    num3 = float(input("Voer uw derde nummer in: "))

    if keuze == '1':
        print(num1, "/", num2, "/", num3 "=", delen (num1, num2, num3))