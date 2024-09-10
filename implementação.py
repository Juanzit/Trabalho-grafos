import numpy as np
from collections import deque

class BipartiteGraph:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, match, dist):
        queue = deque()
        for u in range(self.size // 2):
            if match[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[-1] = float('inf')
        while queue:
            u = queue.popleft()
            if dist[u] < dist[-1]:
                for v in self.graph[u]:
                    match_v = match[v]
                    if dist[match_v] == float('inf'):
                        dist[match_v] = dist[u] + 1
                        queue.append(match_v)
        
        return dist[-1] != float('inf')

    def dfs(self, match, dist, u):
        while u != -1:
            for v in self.graph[u]:
                match_v = match[v]
                if dist[match_v] == dist[u] + 1 and self.dfs(match, dist, match_v):
                    match[v] = u
                    match[u] = v
                    return True
            dist[u] = float('inf')
            return False
        return True

    def hopcroft_karp(self):
        match = np.full(self.size, -1, dtype=int)
        dist = np.full(self.size, -1, dtype=float)
        matching = 0
        while self.bfs(match, dist):
            for u in range(self.size // 2):
                if match[u] == -1 and self.dfs(match, dist, u):
                    matching += 1
        return match, matching

def directed_to_bipartite(directed_graph):
    n = len(directed_graph)
    bipartite = BipartiteGraph(2 * n)
    for u in range(n):
        for v in range(n):
            if directed_graph[u][v] > 0:
                bipartite.add_edge(u, n + v)
    return bipartite

def find_possible_input_nodes(directed_graph):
    bipartite_graph = directed_to_bipartite(directed_graph)
    match, _ = bipartite_graph.hopcroft_karp()

    possible_input_nodes = []
    for u in range(len(directed_graph)):
        if match[u] == -1:
            possible_input_nodes.append(u)
    
    return possible_input_nodes

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de rede direcionada
    directed_graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 9, 14, 0],
        [0, 0, 0, 0, 7, 20],
        [0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]

    possible_input_nodes = find_possible_input_nodes(directed_graph)
    print("Nós de entrada possíveis:", possible_input_nodes)
