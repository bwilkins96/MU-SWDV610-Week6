# SWDV 610: Data Structures and Algorithms
# Binary heap tree class

class BinaryHeapTree:
    def __init__(self, val=None):
        self._heap_list = [0]
        self._size = 0

        if val:
            if type(val == list):
                self.build_heap(val)
            else:
                self.insert(val)

    def _perc_up(self, i):
        while i // 2 > 0:
            if self._heap_list[i] < self._heap_list[i//2]:
                self._heap_list[i], self._heap_list[i//2] = self._heap_list[i//2], self._heap_list[i]
            i = i // 2

    def insert(self, val):
        self._heap_list.append(val)
        self._size += 1
        self._perc_up(self._size)

    def min_child(self, i):
        if i * 2 + 1 > self._size:
            return i*2
        elif self._heap_list[i*2] < self._heap_list[i*2+1]:
            return i*2
        else: 
            return i*2 + 1
    
    def _perc_down(self, i):
        while i*2 <= self._size:
            min_child = self.min_child(i)

            if self._heap_list[i] > self._heap_list[min_child]:
                self._heap_list[i], self._heap_list[min_child] = self._heap_list[min_child], self._heap_list[i]
            
            i = min_child

    def del_min(self):
        original = self._heap_list[1]

        self._heap_list[1] = self._heap_list[self._size]
        self._heap_list.pop()
        self._size -= 1
        self._perc_down(1)

        return original
    
    def build_heap(self, lst):
        self._size += len(lst)
        self._heap_list += lst[:]
        
        i = self._size // 2
        while i > 0:
            self._perc_down(i)
            i -= 1
    
if __name__ == '__main__':
    bht = BinaryHeapTree([9,5,6,2,3])

    print(bht.del_min())         # -> 2
    print(bht.del_min())         # -> 3
    print(bht.del_min())         # -> 5
    print(bht.del_min())         # -> 6
    print(bht.del_min())         # -> 9