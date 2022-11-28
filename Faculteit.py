# ik maak vermenigvuldigen een optie in python 

def vermenigvuldigen(x, y, z):
    return x * y * z

#de gebruiker voert 3 getallen in > user input

nummer1 = float(input("Voer uw eerste nummer in"))
nummer2 = float(input("Voer uw tweede nummer in"))
nummer3 = float(input("Voer uw derde nummer in"))

#het programma vermenigvuldigd de 3 getallen en de uitkomst wordt op het scherm getoont > print functie 

print (nummer1, "*", nummer2, "*", nummer3, "=", vermenigvuldigen (nummer1, nummer2, nummer3))