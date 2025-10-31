# EXO1
a = 0
b = 0
c = 0
d = 0

a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))

c = a / b
d = a % b


print("la division de", a, "par", b, "est egale a", c)
print("le reste de la division de", a, "par", b, "est egale a", d)


# EXO2
a = 0
b = 0
a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))

print(a, b)
a, b = b, a
print(a, b)

# EXO3
a = 0
b = 0
a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))

if a > b:
    print(a, "est plus grand que", b)
elif a < b:
    print(a, "est plus petit que", b)
else:
    print(a, "est egal a", b) 

# EXO4    
N = 0
N = int(input("entrez un valeur"))
choix = input("entrez un choix (la somme des N premiers nombres entiers/la valeur de factoriel N)")
if choix == "la somme des N premiers nombres entiers":
    somme = 0
    for i in range(1, N + 1):
        somme += i
    print("la somme des", N, "premiers nombres entiers est egale a", somme)
elif choix == "la valeur de factoriel N":
    factoriel = 1
    for i in range(1, N + 1):
        factoriel *= i
    print("la valeur de factoriel", N, "est egale a", factoriel)   
else:
    print("choix invalide")


N = int(input("Veuillez saisir un nombre N: "))
for i in range(N, -1, -1):
    print(i, end=' ')
    if (N - i) % 3 == 2:
        print()
            #Fin du programme

