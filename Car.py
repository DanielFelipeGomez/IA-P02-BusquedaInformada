from Node import Node

class Car:
    def __init__(self, x: int, y: int):
        self._node = Node(x, y)

    def __str__(self):
        return '\033[1;36m $ \033[0;m'

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, node):
        self._node = node

# \033[1;33m
# \033[0;m'