import time

def selection_sort(data, draw, speed):
    """
    algorithm to visualize selection sort
    :param data: list of integers to sort
    :param draw: funciton to draw the integers on the canvas
    :param speed: speed at which the algorithm is run
    :return: None
    """
    for i in range(len(data)-1):
        min_index = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i] 

        draw(data, ["Orange" if x == i or x == min_index else "#a871e3" for x in range(len(data))])
        time.sleep(speed)
                   