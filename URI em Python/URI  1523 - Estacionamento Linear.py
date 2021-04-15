while True:
    N, K = [int(x) for x in input().split()]  #motoristas e carros
    if N == K == 0: break
    C = [0] * N
    S = [0] * N
    for i in range(N):
        C[i], S[i] = [int(x) for x in input().split()]
    pilha = []
    resp = 'Sim'
    for i in range(N):
        # O próximo carro vai entrar na hora C[i] 
        # vamos tirar os que já iam sair antes disso
        while len(pilha) > 0 and pilha[-1] <= C[i]:
            pilha.pop()
        # vamos ver se o carro 'i' pode entrar
        # ele pode entrar se houver espaço na pilha
        if len(pilha) == K or (len(pilha) > 0 and pilha[-1] < S[i]):
            resp = 'Nao' 
            break
        else:
        # Agora poder
            pilha.append(S[i])    
    print(resp)