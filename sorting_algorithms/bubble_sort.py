import time
    
def bubble_sort(data, draw, speed):
    """
    algorithm to visualize bubble sort
    :param data: list of integers to sort
    :param draw: funciton to draw the integers on the canvas
    :param speed: speed at which the algorithm is run
    :return: None
    """
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["orange" if x == j or x == j+1 else "#a871e3" for x in range(len(data))])
                time.sleep(speed)  