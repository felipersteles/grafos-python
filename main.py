from grafo import Grafo


def __main__():
    qVertices, qArestas, primeiro_vertice = input().split(" ")

    grafo = Grafo(int(qVertices), int(qArestas))
    for i in range(grafo.qtd_arestas):
        v1, v2, peso = input().split(" ")
        grafo.add_aresta(int(v1), int(v2), int(peso))

    grafo.print_a()


__main__()
