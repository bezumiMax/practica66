def to_edge_list(graph, graph_type):
    edges = []

    if graph_type == "список дуг":
        return graph.copy()

    elif graph_type == "упорядоченный список дуг":
        return graph.copy()

    elif graph_type == "список смежности":
        for u in graph:
            for v in graph[u]:
                edges.append((u, v))

    elif graph_type == "матрица смежности":
        n = len(graph)
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    edges.append((i + 1, j + 1))

    elif graph_type == "матрица инцидентности":
        rows = len(graph)
        cols = len(graph[0])

        for col in range(cols):
            start = end = None
            for row in range(rows):
                if graph[row][col] == -1:
                    start = row + 1
                elif graph[row][col] == 1:
                    end = row + 1
            edges.append((start, end))

    return edges


def convert_graph(graph, from_type, to_type):
    edges = to_edge_list(graph, from_type)

    if to_type == "список дуг":
        return edges

    elif to_type == "список смежности":
        result = {}
        for u, v in edges:
            if u not in result:
                result[u] = []
            result[u].append(v)
        return result

    elif to_type == "матрица смежности":
        n = max(max(u, v) for u, v in edges)
        matrix = [[0] * n for _ in range(n)]

        for u, v in edges:
            matrix[u - 1][v - 1] = 1

        return matrix

    elif to_type == "матрица инцидентности":
        n = max(max(u, v) for u, v in edges)
        m = len(edges)

        matrix = [[0] * m for _ in range(n)]

        for col, (u, v) in enumerate(edges):
            matrix[u - 1][col] = -1
            matrix[v - 1][col] = 1

        return matrix
