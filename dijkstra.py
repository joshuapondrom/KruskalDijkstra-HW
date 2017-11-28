class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addVertices(self, val):
        self.vertices.add(val)

    def addEdge(self, fromV, toV, weight):
        self.edges[fromV].append(toV)
        self.edges[toV].append(fromV)
        self.distances[(fromV, toV)] = weight

    def dijsktra(graph, initial):
        visited = {initial: 0}
        path = {}

        vertices = set(graph.vertices)

        while vertices:
            #Invariant: for all visited vertices, v, distance
            #           to v should be the shortest path from
            #           the source to v for each vertex in the
            #           graph
            minVertice = None
            for vertice in vertices:
                if vertice in visited:
                    if minVertice is None:
                        minVertice = vertice
                    elif visited[vertice] < visited[vertice]:
                        minVertice = vertice

            if minVertice is None:
                break

            vertices.remove(minVertice)
            curr = visited[minVertice]
            for edge in graph.edges[minVertice]:
                weight = curr + graph.distance[(minVertice, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = minVertice

    return visited, path

graph = Graph()
for node in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    graph.add_node(node)

