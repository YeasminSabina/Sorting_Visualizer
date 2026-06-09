import time

def quick_sort(data, left, right, draw, speed):
    """
    algorithm to visualize quick sort
    :param data: list of integers to sort
    :param left: starting index of the list
    :param right: last index of the list
    :param draw: funciton to draw the integers on the canvas
    :param speed: speed at which the algorithm is run
    :return: None
    """
    if left < right:
        pos = partition(data, left, right)
        quick_sort(data, left, pos - 1, draw, speed)
        quick_sort(data, pos + 1, right, draw, speed)
        draw(data, ["Blue" if x >= left and x < pos else "Red" if x == pos
                    else "Yellow" if x > pos and x <= right else "#a871e3" for x in range(len(data))])
        time.sleep(speed)
        
def partition(data, left, right):
    """
    function to handle sorting by partitioning the list of integers based on a pivot 
    :param data: list of integers to sort
    :param left: starting index of the arry
    :param right: ending index of the array
    :return: partition index to divide the array
    """
    i, j = left, right - 1 
    pivot = data[right]
    
    while i < j:
        while i < right and data[i] < pivot:
            i += 1
        while j > left and data[j] >= pivot:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    if data[i] > pivot:
        data[i], data[right] = data[right], data[i] 
      
    return i