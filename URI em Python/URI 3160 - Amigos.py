L = input().split()
N = input().split()
S = input()
if S == "nao":
    L = L + N
elif S in L:
    for e in N:
        L.insert(L.index(S), e)
L = ' '.join(tuple(L))
print(L)