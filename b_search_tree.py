# SWDV 610: Data Structures and Algorithms
# Binary search tree class

class BinarySearchTree:
    """A binary search tree class designed for Maryville University"""

    class _Node:
        """Node class containing a key, value pair and parent, left, and right node pointers"""
        
        def __init__(self, key, val, parent=None, left=None, right=None):
            self._key = key
            self._val = val
            self._parent = parent
            self._left = left
            self._right = right
        
        def key(self):
            """Returns the key variable of a node"""
            return self._key
        
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

    def __init__(self, key=None, val=None):
        """Initializes a binary search tree based on the val parameter."""
        self._root = None
        self._size = 0

        if key: 
            if type(key) == list:
                self.build_search_tree(key, val)
            else:
                self._root = self._Node(key, val)
    
    def get_root(self):
        """Returns the root node"""
        return self._root

    def put(self, key, val):
        """Inserts a node containing val into the search tree"""
        if self._root:
            self._insert_into_tree(key, val)
        else:
            self._root = self._Node(key, val)
        
        self._size += 1

    def _insert_into_tree(self, key, val):
        """Nonpublic method that handles inserting a non-root node"""
        new_node = self._Node(key, val)
        current = self._root
        inserted = False

        while not inserted:
            if key < current._key:
                if current._left:
                    current = current._left
                else:
                    current._left = self._Node(key, val, current)
                    inserted = True
            else:
                if current._right:
                    current = current._right
                else:
                    current._right = self._Node(key, val, current)
                    inserted = True

    def build_search_tree(self, key_lst, val_lst=None):
        """
        Inserts the values of key_lst with corresponding values 
        from val_list into the search tree instance
        """
        if val_lst == None:
            val_lst = [None] * len(key_lst)

        for i in range(len(key_lst)):
            self.put(key_lst[i], val_lst[i])

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

    def __len__(self):
        return self._size
    
    def __setitem__(self, key, val):
        self.put(key, val)

if __name__ == '__main__':
    bst = BinarySearchTree(10, 'a')
    bst.put(5, 'b')
    bst.put(2, 'c')
    bst.put(15, 'e')
    bst.put(3, 'd')

    for node in bst:
        print(node.key(), node.val())                  # -> 10 a, 5 b, 2 c, 3 d, 15 e

    print('\n----------------------\n')
    bst2 = BinarySearchTree([10, 5, 2, 15, 3], ['a', 'b', 'c', 'e', 'd'])

    for node in bst2:
        print(node.key(), node.val())                  # -> 10 a, 5 b, 2 c, 3 d, 15 e