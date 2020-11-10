class Grafo:
    def __init__(self):
        self.vertex = []
        self.matrix = [[None]*0 for i in range(0)]

    def is_in_vertex(self, v):
        if self.vertex.count(v) == 0:
            return False
        return True

    def add_vertex(self, v):
        if self.is_in_vertex(v):
            return False
        self.vertex.append(v)
        row = column = len(self.matrix)
        aux_matrix = [[None]*(row+1) for i in range(column+1)]

        for j in range(row):
            for k in range(column):
                aux_matrix[j][k] = self.matrix[j][k]
        self.matrix = aux_matrix
        return True

    def add_edge(self, begin, end, value, directed):
        if not (self.is_in_vertex(begin)) or not (self.is_in_vertex(end)):
            return False
        self.matrix[self.vertex.index(begin)][self.vertex.index(end)] = value

        if not directed:
            self.matrix[self.vertex.index(end)][self.vertex.index(begin)] = value
        return True

    def print_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if self.matrix[i][j] is None:
                    pass
                else:
                    print("\t", str(self.vertex[i]), str(self.matrix[i][j]), str(self.vertex[j]))


if __name__ == '__main__':
    g = Grafo()
    g.add_vertex("Perro")
    g.add_vertex("Vaca")
    g.add_vertex("Animal")
    g.add_vertex("Herbivoro")
    g.add_vertex("Carnivoro")
    g.add_vertex("Omnivoro")
    g.add_vertex("Leon")

    g.add_edge("Perro", "Omnivoro", "es un", True)
    g.add_edge("Perro", "Animal", "es un", True)
    g.add_edge("Animal", "Herbivoro", "puede ser", True)
    g.add_edge("Animal", "Carnivoro", "puede ser", True)
    g.add_edge("Animal", "Omnivoro", "puede ser", True)
    g.add_edge("Vaca", "Animal", "es un", True)
    g.add_edge("Vaca", "Herbivoro", "es un", True)
    g.add_edge("Leon", "Animal", "es un", True)
    g.add_edge("Leon", "Carnivoro", "es un", True)
    g.print_matrix(g.matrix)
