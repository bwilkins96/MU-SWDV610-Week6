# SWDV 610: Data Structures and Algorithms

class BinarySearchTree:
    
    class _Node:
        def __init__(self, val, parent=None, left=None, right=None):
            self._val = val
            self._parent = parent
            self._left = left
            self._right = right
        
        def children(self):
            return [self._left, self._right]

    def __init__(self, val=None):
        self._root = None

        if val:
            if type(val) == list:
                self.build_search_tree(val)
            else: 
                self._root = self._Node(val)


    def insert(self, val):
        if self._root:
            self._insert_into_tree(val)
        else:
            self._root = self._Node(val)

    def _insert_into_tree(self, val):
        new_node = self._Node(val)
        current = self._root
        inserted = False

        while not inserted:
            if val < current._val:
                if current._left:
                    current = current._left
                else:
                    current._left = self._Node(val, current)
                    inserted = True
            else:
                if current._right:
                    current = current._right
                else:
                    current._right = self._Node(val, current)
                    inserted = True

    def build_search_tree(self, lst):
        for val in lst:
            self.insert(val)

    def preorder(self, node):
        if node: 
            yield node
            for c in node.children():
                for other in self.preorder(c):
                    yield other

    def __iter__(self):
        for node in self.preorder(self._root):
            yield node


if __name__ == '__main__':
    b = BinarySearchTree(10)
    b.insert(5)
    b.insert(2)
    b.insert(3)
    b.insert(15)

    for node in b:
        print(node._val)                  # -> 10, 5, 2, 3, 15

    print('\n----------------\n')
    b2 = BinarySearchTree([10, 5, 2, 3, 15])

    for node in b2:
        print(node._val)                  # -> 10, 5, 2, 3, 15