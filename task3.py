def outgoing_edges(graph, graph_type, vertex):
    result = []

    if graph_type == "матрица смежности":
        row = graph[vertex - 1]
        for j in range(len(row)):
            if row[j] != 0:
                result.append((vertex, j + 1))

    elif graph_type == "матрица инцидентности":
        rows = len(graph)
        cols = len(graph[0])

        for col in range(cols):
            if graph[vertex - 1][col] == -1:
                for i in range(rows):
                    if graph[i][col] == 1:
                        result.append((vertex, i + 1))

    elif graph_type == "список смежности":
        for to_v in graph.get(vertex, []):
            result.append((vertex, to_v))

    elif graph_type == "список дуг":
        for u, v in graph:
            if u == vertex:
                result.append((u, v))

    elif graph_type == "упорядоченный список дуг":
        for u, v in graph:
            if u == vertex:
                result.append((u, v))

    return result
