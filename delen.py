# ik maak delen een optie in python 

def delen(x, y, z):
    return x / y / z

#de gebruiker voert 3 getallen in > user input

nummer1 = float(input("Voer uw eerste nummer in"))
nummer2 = float(input("Voer uw tweede nummer in"))
nummer3 = float(input("Voer uw derde nummer in"))

#het programma deelt de 3 getallen door elkaar en de uitkomst wordt op het scherm getoont, op 4 decimalen afgerond > print functie 

print (nummer1, "/", nummer2, "/", nummer3, "=", delen (nummer1, nummer2, nummer3))