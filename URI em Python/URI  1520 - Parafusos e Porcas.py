from bisect import bisect_left, bisect_right

while True:
    try:
        N = int(input())
    except EOFError:
        break
    except ValueError:
       error = False
       continue

    lista = []
    for i in range(N):
        x, y = list(map(int, input().split()))
        for item in range(x, y+1, 1): 
            lista.append(item)
    lista.sort()
    
    num = int(input())
    if num in lista:
        print("{} found from {} to {}".format(num, bisect_left(lista, num), bisect_right(lista, num) - 1))
    else:
        print("{} not found".format(num))