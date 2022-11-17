from Car import Car
from Goal import Goal
from Node import Node
import time
import math


class Highway:
    iteracion = 0

    def __init__(self, num_rows, num_columns, start_x, start_y, end_x, end_y):
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._matrix = []
        for i in range(self._num_rows):
            aux = []
            for j in range(self._num_columns):
                aux.append('º')
            self._matrix.append(aux)
        self._car = Car(start_x, start_y)
        self._goal = Goal(end_x, end_y)
        self._matrix[start_x][start_y] = self._car
        self._matrix[end_x][end_y] = self._goal
        self._open_array = [Node(self._car.node.x, self._car.node.y, 0)]
        self._close_array = []


    def __str__(self):
        # print(f'carro {self._car.node.x} , {self._car.node.y}')
        if (self._car.node.x - 10 <= 0):
            start_x = 0
        else:
            start_x = self._car.node.x - 10
        if (self._car.node.y - 10 <= 0):
            start_y = 0
        else:
            start_y = self._car.node.y - 10
        if (self._car.node.x + 10 >= self._num_rows):
            end_x = self._num_rows
        else:
            end_x = self._car.node.x + 10
        if (self._car.node.y + 10 >= self._num_columns):
            end_y = self._num_columns
        else:
            end_y = self._car.node.y + 10

        # print(f'x -> ({start_x, end_x}) y -> ({start_y, end_y})')
        result = f'Iteración Nº {Highway.iteracion}\n'
        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                result += str(self._matrix[i][j].__str__()).center(3, ' ')
                # result += ('(' + str(i) + ',' + str(j) + ')').center(8,' ')
                # result += '[' + ('(' + str(i) + ',' + str(j) + ')').center(8,' ') + str(self._matrix[i][j].__str__()).center(3, ' ') + '] '
            result += '\n'
        return result

    @property
    def open_array(self):
        return self._open_array

    @property
    def close_array(self):
        return self._close_array

    def draw_car(self, go_x, go_y):
        self._car.node.x = go_x
        self._car.node.y = go_y
        self._matrix[self._car.node.x][self._car.node.y] = self._car
        Highway.iteracion += 1

    def distance_from_euclídea(self, node: Node):
        return math.sqrt(pow((node.x - self._goal.node.x), 2) + pow((node.y - self._goal.node.y), 2))

    def distance_from_manhattan(self, node: Node):
        return abs(node.x - self._goal.node.x) + abs(node.y - self._goal.node.y)

    def calculate_evaluation_function(self, node, option):
        g = 1
        if option == 1:
            heuristics = self.distance_from_manhattan(node)
        else:
            heuristics = self.distance_from_euclídea(node)
        return g + heuristics

    def a_estrella(self, time_to_wait, option):
        if self._car.node.x == self._goal.node.x and self._car.node.y == self._goal.node.y:
            return self._car
        else:
            self._close_array.append(self._car.node)

            stop = False
            while not stop:
                time.sleep(time_to_wait)
                actual = self._close_array.pop(0)

                north = Node(actual.x, actual.y - 1)
                south = Node(actual.x, actual.y + 1)
                east = Node(actual.x + 1, actual.y)
                west = Node(actual.x - 1, actual.y)
                aux = [east, west, north, south]
                neighbours = []
                for a in aux:
                    if not(a in self._close_array):
                        neighbours.append(a)
                aux.clear()

                for n in neighbours:
                    n.parent = actual
                    n.evaluation_function = self.calculate_evaluation_function(n, option)

                for n in neighbours:
                    if not(n in self._close_array) and not(n in self._open_array):
                        self._open_array.append(n)
                neighbours.clear()
                self._open_array = sorted(self._open_array, key=lambda obj: obj.evaluation_function)
                aux2 = self._open_array.pop(0)
                self.draw_car(aux2.x, aux2.y)
                self._close_array.append(aux2)
                if self._car.node.x == self._goal.node.x and self._car.node.y == self._goal.node.y:
                    stop = True
                print(f'Iteración -> {Highway.iteracion}')
                print(self)
            return actual

if __name__ == '__main__':
    tam_fil = int(input('Indique el tamaño de las filas:\n>'))
    tam_col = int(input('Indique el tamaño de las columnas:\n>'))
    car_x = int(input('Indique la posición x de arranque:\n>'))
    car_y = int(input('Indique la posición y de arranque:\n>'))
    objetivo_x = int(input('Indique la posición x de objetivo:\n>'))
    objetivo_y = int(input('Indique la posición y de objetivo:\n>'))
    time_to_wait = float(input('Indique el tiempo de espera entre transición que desea ver:\n>'))
    option_heuristic = int(input('Indique la función heuristica que desea usar. \n1) Manhattan\n2) Euclides\n>'))

    inicio = time.time()
    carretera = Highway(tam_fil, tam_col, car_x, car_y, objetivo_x, objetivo_y)
    print(carretera)
    carretera.a_estrella(time_to_wait, option_heuristic)
    fin = time.time()
    print(fin - inicio)
    destFile = "resultados.txt"
    str_open_array = ''
    str_close_array = ''
    with open(destFile, 'a') as f:
        if option_heuristic == 1:
            result = 'Manhatann'
        else:
            result = 'Euclides'
        for n in carretera.open_array:
            str_open_array += '[' + n.__str__() + '] '
        for n in carretera.close_array:
            str_close_array += '[' + n.__str__() + '] '
        f.write(f"{result} desde {car_x, car_y} hasta {objetivo_x, objetivo_y} "
                f"a velocidad {time_to_wait}: {fin - inicio}\n"
                f"Vector de abiertos: {str_open_array}\n"
                f"Vector de cerrados: {str_close_array}\n\n")
