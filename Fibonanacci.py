fibonanacci = int(input("Hoeveel getallen wilt u uit de Fibonnacci reeks zien?"))

n1, n2 = 0, 1
count = 0 

if fibonanacci <= 0:
    print("Vul een positief getal in, zonder komma's")
elif fibonanacci == 1:
    print("fibonacci reeks tot" ,fibonanacci,":" )
    print(n1)
else: 
    print("fibonacci reeks:")
    while count < fibonanacci:
        print(n1)
        begin = n1 + n2 

        n1 = n2
        n2 = begin
        count += 1