parent = dict()
rank = dict()

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(verticeA, verticeB):
    rootA = find(verticeA)
    rootB = find(verticeB)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
        if rank[rootA] == rank[rootB]:
            rank[rootB] = rank[rootB] + 1

def dijsktra(graph, initial):
    visited = {initial: 0}
    path= {}

    vertices = set(graph['vertices'])

    while vertices:
        minVertice = None
        for vertice in vertices:
            if vertice in visited:
                if minVertice is None:
                    minVertice = vertice
                elif visited[vertice] < visited[minVertice]:
                    minVertice = vertice

        if minVertice is None:
            break

        vertices.remove(minVertice)
        curr = visited[minVertice]

        for edge in list(graph['edges']):
            weight = curr + graph.distance[(minVertice, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = minVertice

    return visited, path

def kruskal(graph):
    #This loop is to initialize and set up our graph
    for vertice in graph['vertices']:
        parent[vertice] = vertice
        rank[vertice] = 0
        minTree = set()
        edges = list(graph['edges'])
        #The edges will be sorted because the algorithm is greedy
        edges.sort()

    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            #Invariant: minTree is a subset of graph
            minTree.add(edge)

    return(minTree)

graph = {
        'vertices': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        'edges': set([
            (4, 'a', 'b'),
            (8, 'b', 'c'),
            (7, 'c', 'd'),
            (9, 'd', 'e'),
            (8, 'a', 'h'),
            (1, 'h', 'g'),
            (11, 'b', 'h'),
            (7, 'h', 'i'),
            (6, 'g', 'i'),
            (2, 'i', 'c'),
            (4, 'c', 'f'),
            (14, 'd', 'f'),
            (10, 'f', 'e'),
            (2, 'g', 'f'),

            (4, 'b', 'b'),
            (8, 'c', 'c'),
            (7, 'd', 'd'),
            (9, 'e', 'e'),
            (8, 'h', 'h'),
            (1, 'g', 'g'),
            (11, 'h', 'h'),
            (7, 'i', 'i'),
            (6, 'i', 'i'),
            (2, 'c', 'c'),
            (4, 'f', 'f'),
            (14, 'f', 'f'),
            (10, 'e', 'e'),
            (2, 'f', 'g'),
            ])
        }

print(kruskal(graph))
