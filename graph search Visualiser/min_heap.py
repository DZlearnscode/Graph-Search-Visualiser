from random import randint

class Heap():
    def __init__(self):
        self.heap = [None]
        self.count = 0

    # helper functions to find parent child relationship

    def parent(self,indx):
        #return parent index
        return indx // 2
    
    def left_child(self, indx):
        #return left_child index
        return indx * 2

    def right_child(self,indx):
        #return right_child index
        return (indx * 2 )+ 1

    def clear_heap(self):
        self.heap = [None]

    def push(self,element):
        self.heap.append(element)
        self.count += 1
        self.heapify()

    def pop(self):
        if self.count < 1:
            print('empty')
            return None
        self.count -= 1
        node = self.heap.pop(1)
        self.heapify()
        return node

    def heapify(self):
        indx = self.count
        while self.parent(indx) > 0:
            parent = self.heap[self.parent(indx)]
            child = self.heap[indx]
            if parent.heuristic > child.heuristic:
                self.heap[indx] = parent
                self.heap[self.parent(indx)] = child
            indx = self.parent(indx)
        




