class Node:
    def __init__(self, x: int, y: int, evaluation_function=0):
        self._x = x
        self._y = y
        self._parent = None
        self._evaluation_function = evaluation_function

    def __str__(self):
        return f'X -> {self._x} | Y -> {self._y} | EvaluationFunction -> {self._evaluation_function}'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def evaluation_function(self):
        return self._evaluation_function

    @property
    def parent(self):
        return self._parent

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    @evaluation_function.setter
    def evaluation_function(self, evaluation_function):
        self._evaluation_function = evaluation_function

    @parent.setter
    def parent(self, parent):
        self._parent = parent
