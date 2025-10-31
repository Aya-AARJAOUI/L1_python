
# EXO5
N = int(input("Veuillez saisir un nombre N: "))
for i in range(N, -1, -1):
    print(i, end=' ')
    if (N - i) % 3 == 2:
        print()
 