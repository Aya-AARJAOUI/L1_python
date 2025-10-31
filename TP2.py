#EXO1
prenom = str(input("entrez votre prenom: "))
nom = str(input("entrez votre nom: "))
print(" Hello", prenom, nom)

                 #Fin du programme

a = 0
b = 0
a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))
c = a + b
print("la somme de", a, "et", b, "est egale a", c)

                 #Fin du programme

a = 0
b = 0
c = 0

a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))
c = int(input("entrez un valeur"))

d = a + b + c
print("la somme de", a, ",", b, "et", c, "est egale a", d)

                    #Fin du programme

a = 0
b = 0
c = 0

a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))
c = int(input("entrez un valeur"))

moyenne = (a + b + c) / 3
print("la moyenne de", a, ",", b, "et", c, "est egale a", moyenne)
                     #Fin du programme
 

#EXO2
a = 0
b = 0

a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))

if a==b:
    print(a, "est egal a", b)
else:
    print(a, "n'est pas egal a", b)

                     #Fin du programme

a = 0
a = int(input("entrez un valeur"))
if a % 2 == 0:
    print(a, "est un nombre pair")  
else:
    print(a, "est un nombre impair")
                     #Fin du programme  

a = 0
b = 0
c = 0

a = int(input("entrez un valeur"))
b = int(input("entrez un valeur"))
c = int(input("entrez un valeur"))
if a >= b and a >= c:
    print(a, "est le maximum des trois nombres")    
elif b >= a and b >= c:
    print(b, "est le maximum des trois nombres")        
else:
    print(c, "est le maximum des trois nombres")  
                     #Fin du programme                        

#EXO3
N = 0   
N = int(input("entrez un valeur"))
for i in range(N):
     nombre = input("entrez le nmbre " + str(i+1) + ": ")
     somme += int(nombre)
moyenne = somme / N
print("la moyenne des", N, "nombres est egale a", moyenne)
                        #Fin du programme     

N = 0   
N = int(input("entrez un valeur"))
minimum = float('inf')
for i in range(N):
     nombre = input("entrez le nmbre " + str(i+1) + ": ")
if nombre  <  minimum:
        minimum = nombre 
print("le minimum des", N, "nombres est egale a", minimum)
                        #Fin du programme

for i in range(2000, 3201):
     if i % 7 ==0 and i % 5 !=0:
          print(i,end=(','))  
                        #Fin du programme

N = 0   
N = int(input("entrez un valeur"))
# Initialisation d'un compteur de diviseurs
compteur_diviseurs = 0

# Boucle pour vérifier les diviseurs
for i in range(1, N + 1):
    if N % i == 0:
        compteur_diviseurs += 1

# Vérification si le nombre est premier
if compteur_diviseurs == 2:
    print(f"{N} est un nombre premier.")
else:
    print(f"{N} n'est pas un nombre premier.")
          
           #Fin du programme


for n in range(2, 1000):      # On parcourt les nombres de 2 à 999
    est_premier = True        # On suppose que le nombre est premier

    for i in range(2, n):     # On teste tous les diviseurs possibles
        if n % i == 0:        # Si le nombre est divisible par i
            est_premier = False
            break             # Pas la peine de continuer

    if est_premier:           # Si aucun diviseur trouvé, c'est un nombre premier
        print(n,end=(',')) 

