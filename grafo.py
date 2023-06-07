class Grafo:
    def __init__(self, vertices, arestas):
        self.qtd_vertices = vertices
        self.qtd_arestas = arestas
        self.vertices = []
        for i in range(vertices):
            novo_vertice = Vertice(i + 1)
            self.vertices.append(novo_vertice)

        self.arestas = []

    def get_vertice(self, valor):
        for i in self.vertices:
            if valor == i.valor:
                return i

    def add_aresta(self, v1, v2, peso):
        nova_aresta = Aresta(self.get_vertice(v1), self.get_vertice(v2), peso)
        self.arestas.append(nova_aresta)
        self.get_vertice(v1).add_vizinho(self.get_vertice(v2))
        self.get_vertice(v2).add_vizinho(self.get_vertice(v1))

    def print_v(self):
        for i in self.vertices:
            print(i)

    def print_a(self):
        for i in self.arestas:
            print(i.v1, i.v2, i.peso)


class Vertice:
    def __init__(self, valor):
        self.visitado = False
        self.valor = valor
        self.vizinhos = []

    def add_vizinho(self, v):
        if len(self.vizinhos) == 0:
            self.vizinhos.append(v)
        else:
            flag = False
            for i in self.vizinhos:
                if v == i:
                    flag = True
            if flag == False:
                self.vizinhos.append(v)

    def __str__(self):
        s = ''
        s += 'valor: ' + str(self.valor)
        s += '\nvizinhos: '
        for i in self.vizinhos:
            s += str(i.valor) + ' '

        return s


class Aresta:
    def __init__(self, v1, v2, peso):
        self.v1 = v1
        self.v2 = v2
        self.peso = peso

    def __str__(self):
        s = ''
        s += str([self.v1.valor, self.v2.valor]) + ": " + str(self.peso)

        return s
