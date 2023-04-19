# SWDV 610: Data Structures and Algorithms
# A function that returns a list of random integers

from random import randrange

def random_int_list(size=10, min=1, max=1000):
    """Returns a list of random integers between min and max, with a length of size"""
    int_list = []
    for i in range(size): 
        int_list.append(randrange(min, max+1))

    return int_list

if __name__ == '__main__':
    print(random_int_list())
    print(random_int_list())
    print(random_int_list(5))
    print(random_int_list(min=-10, max=50))
