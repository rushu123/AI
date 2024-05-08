def printMST(parent, graph, total_weight):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
    print("Minimum weight of MST:", total_weight)

def prim(graph, numVertices):
    parent = [None] * numVertices
    key = [float('inf')] * numVertices
    mstSet = [False] * numVertices

    key[0] = 0
    parent[0] = -1

    for _ in range(numVertices - 1):
        u = min((key[i], i) for i in range(numVertices) if not mstSet[i])[1]
        mstSet[u] = True

        for v in range(numVertices):
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    total_weight = sum(key)
    printMST(parent, graph, total_weight)

n = int(input("Enter the size of the graph: "))
graph = [[int(input(f"Enter the weight {i}->{j} of the graph: ")) for j in range(n)] for i in range(n)]

prim(graph, n)
