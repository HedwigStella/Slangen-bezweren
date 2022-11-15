def plus(x, y):
    return x + y

def min(x, y):
    return x - y

def vermenigvuldigen(x, y):
    return x * y

def delen(x, y):
    return x / y


print("Maak uw keuze")
print("1.plus")
print("2.min")
print("3.vermenigvuldigen")
print("4.delen")

while True:
    keuze = input("Vul uw keuze in(1/2/3/4): ")

    if keuze in ('1', '2', '3', '4'):
        num1 = float(input("Voer uw eerste nummer in: "))
        num2 = float(input("Voer uw tweede nummer in: "))

        if keuze == '1':
            print(num1, "+", num2, "=", plus(num1, num2))

        elif keuze == '2':
            print(num1, "-", num2, "=", min(num1, num2))

        elif keuze == '3':
            print(num1, "*", num2, "=", vermenigvuldigen(num1, num2))

        elif keuze == '4':
            print(num1, "/", num2, "=", delen(num1, num2))
    
        volgende_berekening = input("Wil je nog een berekening doen? (ja/nee): ")
        if volgende_berekening == "nee":
          break
    
    else:
        print("Invalid Input")