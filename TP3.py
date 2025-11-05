mon_tuple = 0
mon_tuple = (1, 2, 3)
print(tuple[0])

for element in mon_tuple:
    print(element)

if 2 in mon_tuple:
    print("2 est dans le tuple")

print(len(mon_tuple))

mon_tuple += (4, 5)
print(mon_tuple)

del mon_tuple
print(mon_tuple)

#EXO 2
J = int(input("Entrez un numéro de mois (1-12) : "))
num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
mois_tuple = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")
if J in num_tuple:
    index = num_tuple.index(J)
    print("Le mois correspondant est :", mois_tuple[index])
else:
    print("Numéro de mois invalide.")
   #fin de programme
 
   #EXO 3
n = int(input("Entrez un entier : "))   
mon_tuple = 0  
mon_tuple = (10, 20, 30, 40, 50, 30)
while n in mon_tuple:
    index = mon_tuple.index(n)
    print("L'index de", n, "est :", index)
    break   
else:
    print("L'entier n'est pas dans le tuple.")
#fin de programme

n = int(input("Entrez un entier : "))   
mon_tuple = 0  
mon_tuple = (10, 20, 30, 40, 50, 30)
while n in mon_tuple:
    count = mon_tuple.count(n)
    print("Le nombre doccurence", n, "est :", count)
    break   
else:
    print("L'entier n'est pas dans le tuple.")
#fin de programme

#EXO 4
liste = [17, 38, 10, 25, 72]
liste.sort()
print("Liste triée :", liste)
liste.append(12)
print("Liste après ajout de 12 :", liste)
liste.reverse()
print("Liste après inversion :", liste)
liste.index(17)
print("Index de 17 dans la liste :", liste.index(17))
liste.remove(38)
print("Liste après suppression de 38 :", liste)
print("Sous-liste des éléments d'index 1 à 3 :", liste[1:3])
print("Sous-liste des éléments d'index du debut à 2 :", liste[:1])
print("Sous-liste des éléments d'index 3 à la fin :", liste[:])

#fin de programme

#EXO 5
L=[1,2,2,1,2,1]
L_unique = list(set(L))
print("Liste sans doublons :", L_unique)
#fin de programme

#EXO 6
liste = [1, 2, 3, 4, 5, 50]
maximum = max(liste)
print("Le maximum de la liste est :", maximum)
#fin de programme

#EXO 7
liste = ["T","O","A","p","t","p","l","o","e","s","t","t","r","s","t","t","t","u","m","m","p"]
liste = [liste[i] for i in range(len(liste)) if i % 2 != 0]
print("Liste après suppression des éléments d'index pair :", liste)
liste = [lettre for lettre in liste if lettre.lower() != 't']
print("Liste après suppression des 't' et 'T' :", liste)




