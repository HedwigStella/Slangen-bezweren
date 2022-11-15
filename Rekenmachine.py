def add(x, y):
    return x + y 

def substract (x, y):
    return x - y 

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y 

print ("wat wil je doen")
print (".add")
print (".substract")
print ("multiply")
print ("divide")

keuze = input ("vul uw keuze in (1/2/3/4): ")
if keuze in ('1' , '2' , '3' , '4'):
    nr1 = float(input("vul uw eerste nummer in: "))
     nr2 = float(input("vul uw tweede nummer in: "))

    if keuze == '1' :
        print(nr1 , "+" , nr2 , "=" , add(nr1 , nr2))
    elif keuze == '2' :
        print(nr1 , "-" , nr2 , "=" , substract(nr1 , nr2))
     elif keuze == '3' :
        print(nr1 , "*" , nr2 , "=" , multiply(nr1 , nr2))
      elif keuze == '4' :
        print(nr1 , "/" , nr2 , "=" , divide(nr1 , nr2))

    volgende_berekening = input ("wil je nog een berekening doen (ja/nee): ")
    if volgende_berekening == "nee"
        break

    else : 
        print ("ongeldige invoer")