from bisect import bisect_left

def achar(num, l):
    indice = (bisect_left(l, num))

    if indice < len(l) and l[indice] == num:
        return indice + 1
    else:
        return -1

caso = 1

while True:
    n, q = list(map(int, input().split()))
    if n == 0 and q == 0:
        break

    print("CASE# %d:" % caso)
    caso += 1
    lista = []
    for i in range(n + q): 
        if i < n: 
            lista.append(int(input()))

        if i == (n - 1):
            lista.sort()

        if i >= n:
            pesquisa = int(input())
            indice = achar(pesquisa, lista) 

            if indice == -1:
                print(str(pesquisa) + " not found")
            else:
                print(str(pesquisa) + " found at " + str(indice))