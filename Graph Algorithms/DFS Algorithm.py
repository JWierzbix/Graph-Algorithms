M = [[0,1,1,1,0,0],
    [1,0,1,1,0,1],
    [1,1,0,0,1,1],
    [1,1,0,0,1,0],
    [0,0,1,1,0,1],
    [0,1,1,0,1,0]]

def Explore(n,M,Visited,Previsit,Postvisit,indeks):
    Visited[n] = True
    Previsit[n] = indeks
    indeks += 1
    for j in range(len(M)):
        if M[n][j]==1 and Visited[j]!=True :
            indeks = Explore(j,M,Visited,Previsit,Postvisit,indeks)
    Postvisit[n] = indeks
    indeks += 1
    return indeks

def DFS(M):
    Visited = len(M) * [False]
    Previsit = len(M) * [0]
    Postvisit = len(M) * [0]
    indeks = 0
    for i in range(len(Visited)):
        if Visited[i] == False:
            Explore(i,M,Visited,Previsit,Postvisit,indeks)
    print(f"Visited: {Visited}")
    print(f"Previsit: {Previsit}")
    print(f"Postvisit: {Postvisit}")

DFS(M)
