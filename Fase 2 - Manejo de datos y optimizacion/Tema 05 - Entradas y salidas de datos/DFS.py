# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 22:28:59 2022

@author: Fernando
"""

# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Configurado para realizar un seguimiento de los nodos visitados del gráfico.

def dfs(visited, graph, node):  #funcion para dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Codigo
print("A continuación se muestra el algoritmo DFS")
dfs(visited, graph, '5')

# Aqui inicia el dfs recursivo
def recursive_dfs(graph, source,path = []):

       if source not in path:

           path.append(source)

           if source not in graph:
               # leaf node, backtrack
               return path

           for neighbour in graph[source]:

               path = recursive_dfs(graph, neighbour, path)


       return path
   
graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}


path = recursive_dfs(graph, "A")

print(" ".join(path))
