import time

class Heap_Sort():
    """
    sorts an array of integers using heap sort algorithm
    """
    def __init__(self, data, draw, speed):
        """
        initializes heap sort algorithm
        :param data: list of integers to sort
        :draw: function to draw the integers on the canvas
        :speed: speed at which the algorithm is run
        """
        self.heap_sort(data, draw, speed)
    
    def heapify(self, data, n, i):
        """
        builds a max heap to perform heap sort
        :param data: list of integers to sort
        :param n: size of heap
        :param i: root of the heap
        :return: None
        """
        # initialize largest as root
        self.largest = i
        left, right = (2 * i + 1), (2 * i + 2)
        
        # if left child is greater than root
        if left < n and data[self.largest] < data[left]:
            self.largest = left
            
        # if right child is greater than root    
        if right < n and data[self.largest] < data[right]:
            self.largest = right
        
        # if root is not largest, swap with largest and continue heapifying    
        if self.largest != i:
            data[i], data[self.largest] = data[self.largest], data[i]
            self.heapify(data, n, self.largest)
    
    def heap_sort(self, data, draw, speed):
        """
        performs heap sort by building a max heap
        :param data: list of integers to sort
        :draw: function to draw the integers on the canvas
        :speed: speed at which the algorithm is run
        :return: None
        """
        
        # building max-heap
        # first index of a non-leaf node → len(data)//2 - 1 
        for i in range(len(data) // 2 - 1, -1, -1):
            self.heapify(data, len(data), i)
        
        # extract elements (remove root and heapify)
        for i in range(len(data)-1, 0, -1):
            
            # swap root with last element
            data[i], data[0] = data[0], data[i]
            
            # heapify root
            self.heapify(data, i, 0)
            draw(data, ["Orange" if x == i or x == self.largest else "#a871e3" for x in range(len(data))])
            time.sleep(speed)
