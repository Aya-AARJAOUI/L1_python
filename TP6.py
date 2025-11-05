#EXO1
x, y = map(int, input("Entrez deux nombres entiers séparés par un espace: ").split())
somme = x + y
print("La somme de", x, "et", y, "est:", somme)

#EXO2
j = int(input("Entrez un nombre de jours: "))
semaines = j // 7
annees = j // 365
jours_restants = j % 7
print(j, "jours correspondent à", annees, "années,", semaines, "semaines et", jours_restants, "jours.")

#EXO3
a, b, c = map(int, input("Entrez trois nombres entiers séparés par des espaces: ").split())
if a >= b and a >= c:
    maximum = a 
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c
print("Le maximum des trois nombres est:", maximum)

#EXO4
choix = input("Choisissez une opération (addition, soustraction, multiplication, division): ").strip().lower()
x, y = map(int, input("Entrez deux nombres entiers séparés par un espace: ").split())
if choix == "addition":
    resultat = x + y
    print("Le résultat de l'addition est:", resultat)   
elif choix == "soustraction":
    resultat = x - y
    print("Le résultat de la soustraction est:", resultat)     
elif choix == "multiplication":
    resultat = x * y
    print("Le résultat de la multiplication est:", resultat)
elif choix == "division":
    if y != 0:
        resultat = x / y
        print("Le résultat de la division est:", resultat)
    else:
        print("Erreur: Division par zéro n'est pas permise.")
else:
    print("Opération non reconnue.")

#EXO5
N = int(input("Combien de nombre voulez vous saisir: "))
minimum = float('inf')
for i in range(N):
    nombre = float(input(f"Saisissez le nombre {i + 1}: "))
    if nombre < minimum:
        minimum = nombre
print(f"Le minimum des nombres saisis est : {minimum}")

for i in range(200, 3201):
    if i % 7 == 0 and i % 5 != 0 :
        print(i, end=", ")

n = int(input("Entrez un nombre entier: "))
premmier = True
for i in range(2, n):
    if n % i == 0:
        premmier = False
        break
if premmier:
    print(n, "est un nombre premier.")
else:
    print(n, "n'est pas un nombre premier.")

       