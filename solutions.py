# SWDV 610: Data Structures and Algorithms
# Produces a list of random integers, along with a binary heap and search tree 
# with the values in that list

from random_int_list import random_int_list
from b_search_tree import BinarySearchTree
from b_heap_tree import BinaryHeapTree

def main():
    #int_list = random_int_list()

    # This list is for demonstration
    int_list = [380, 266, 475, 302, 783, 332, 936, 298, 23, 656]
    
    print('List:', int_list)
    input('Press <enter> to continue')

    b_heap_tree = BinaryHeapTree(int_list)
    print('\nBinary Heap Tree: ')
    print(b_heap_tree)
    input('Press <enter> to continue')

    b_search_tree = BinarySearchTree(int_list)
    print('\nBinary Search Tree, Preorder Traversal:')
    for node in b_search_tree: 
        print(node.key(), end=' -> ')

if __name__ == '__main__': main()


# Heap Tree output with demonstation list
# [0, 23, 266, 332, 298, 656, 475, 936, 380, 302, 783]

# Search Tree output with demonstration list 
# 380 -> 266 -> 23 -> 302 -> 298 -> 332 -> 475 -> 783 -> 656 -> 936 ->