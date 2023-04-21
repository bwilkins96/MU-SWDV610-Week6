# SWDV 610: Data Structures and Algorithms
# Binary search tree class

class BinarySearchTree:
    """A binary search tree class designed for Maryville University"""

    class _Node:
        """Node class containing a value and parent, left, and right node pointers"""
        
        def __init__(self, val, parent=None, left=None, right=None):
            self._val = val
            self._parent = parent
            self._left = left
            self._right = right
        
        def val(self):
            """Returns the value variable of a node"""
            return self._val
        
        def parent(self):
            """Returns the parent node"""
            return self._parent

        def left_child(self):
            """Returns the left child node"""
            return self._left
        
        def right_child(self):
            """Returns the right child node"""
            return self._right
        
        def children(self):
            """Returns a list cotaining the left and right children nodes"""
            return [self._left, self._right]

    def __init__(self, val=None):
        """Initializes a binary search tree based on the val parameter."""
        self._root = None

        if val:
            if type(val) == list:
                self.build_search_tree(val)
            else: 
                self._root = self._Node(val)
    
    def get_root(self):
        """Returns the root node"""
        return self._root

    def insert(self, val):
        """Inserts a node containing val into the search tree"""
        if self._root:
            self._insert_into_tree(val)
        else:
            self._root = self._Node(val)

    def _insert_into_tree(self, val):
        """Nonpublic method that handles inserting a non-root node"""
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
        """Inserts the values of lst into the search tree instance"""
        for val in lst:
            self.insert(val)

    def preorder(self, node):
        """Generates a preorder iteration of nodes"""
        if node: 
            yield node
            for c in node.children():
                for other in self.preorder(c):
                    yield other

    def breadth_first(self, node):
        """Generates a breadth first iteration of nodes"""
        queue = [node]

        while len(queue) > 0:
            current = queue.pop(0)
            yield current

            if current._left: queue.append(current._left)
            if current._right: queue.append(current._right)

    def __iter__(self):
        for node in self.preorder(self._root):
            yield node

if __name__ == '__main__':
    bst = BinarySearchTree(10)
    bst.insert(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(15)

    for node in bst:
        print(node._val)                  # -> 10, 5, 2, 3, 15