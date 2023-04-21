# SWDV 610: Data Structures and Algorithms

from random_int_list import random_int_list
from b_search_tree import BinarySearchTree
from b_heap_tree import BinaryHeapTree

def main():
    int_list = random_int_list()

    b_heap_tree = BinaryHeapTree(int_list)

    b_search_tree = BinarySearchTree(int_list)


if __name__ == '__main__': main()