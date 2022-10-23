#Algorytm Zachłanny jako optymalizacja Problemu Komiwojażera
import sys

def Explore(actuall,index,M,Visited,Distance):
     min_value = sys.maxsize
     min_vertex = -1
     for i in range(len(M)):
          if M[actuall][i]<min_value and actuall!=i and Visited[i]==False :
               min_value = M[actuall][i]
               min_vertex = i
     if min_value!=sys.maxsize and min_vertex!=-1:
          Visited[min_vertex] = True
          Distance[0][index] = min_vertex
          Distance[1][index] = M[actuall][min_vertex]
          actuall = min_vertex
          index+=1
          Explore(actuall,index,M,Visited,Distance)
def TSP(M):
     Visited = len(M)*[False]
     Visited[0] = True
     Distance = [len(M)*[0],len(M)*[0]]
     actuall = 0
     index = 1
     Explore(actuall,index,M,Visited,Distance)
     #wypisywanie wyniku
     wynik = "Optymalna Ścieżka: "
     droga = 0
     for i in range(len(Distance[0])):
          wynik += f"{Distance[0][i]+1}[{Distance[1][i]}], "
          droga += Distance[1][i]
     print(wynik)
     print(f"Długość drogi: {droga}")

M = [[0,2,2,1,4],
     [2,0,3,2,3],
     [2,3,0,2,2],
     [1,2,2,0,4],
     [4,3,2,4,0]]
TSP(M)