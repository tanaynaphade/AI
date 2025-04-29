def add_edge(graph, u, v):
    graph[u][v] = graph[v][u] = 1

def is_safe(node, color, graph, c):
    return all(graph[node][i] == 0 or color[i] != c for i in range(len(graph)))

def solve(graph, m, color, v):
    if v == len(graph):
        return True
    for c in range(m):
        if is_safe(v, color, graph, c):
            color[v] = c
            if solve(graph, m, color, v+1): return True
            color[v] = -1
    return False

def graph_coloring(graph, m):
    color = [-1] * len(graph)
    return solve(graph, m, color, 0)

g = [[0]*6 for _ in range(6)]
edges = [(0,1), (0,2), (0,3), (2,4), (2,5), (3,5)]
for u, v in edges: add_edge(g, u, v)

print(graph_coloring(g, 3))  # True or False
