from shapely import Polygon


class Poly(Polygon):
    def __init__(self, num_of_nodes, population):
        # Динамические поля (переменные объекта)
        Polygon.__init__(self)
        self.num_of_nodes = num_of_nodes
        self.population = population
