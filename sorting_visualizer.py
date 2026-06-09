import random
import tkinter as tk
from tkinter import ttk

from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.heap_sort import Heap_Sort
from sorting_algorithms.insertion_sort import insertion_sort

class SortingVisualizer():
    """
    used to create and run the gui for sorting visualization
    """
    alg_list = ["Bubble Sort", "Merge Sort", "Selection Sort", "Insertion Sort", "Quick Sort", "Heap Sort"]
    def __init__(self, window):
        """
        used to initialize a gui window of constant width and height
        :param window: window
        """
        self.window = window
        self.window.title("Sorting Algorithm Visualizer")
        self.window.geometry("800x450")
        self.window.minsize(800, 450)
        self.window.maxsize(800, 450)
        self.window.config(bg = "#152e57")
    
    def draw_ui(self): 
        """
        draws the ui for the program 
        """
        self.frame = tk.Frame(self.window, width = 770, height = 100, bg = "#bbace8")
        self.frame.grid(row = 0, column = 0, padx = 15, pady = 15)
        self.canvas = tk.Canvas(self.window, width = 770, height = 300, highlightthickness=0, bg = "white")
        self.canvas.grid(row=1, column=0, padx = 15, pady = 15)
        
        self.label = tk.Label(self.frame, text = "Algorithms: ", width = 25)
        self.label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "E")
        
        self.select = tk.StringVar()
        self.alg_dropdown = ttk.Combobox(self.frame, textvariable = self.select,
                                  values = self.alg_list, state = "readonly")
        self.alg_dropdown.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.alg_dropdown.current(0)
        
        self.min_size = tk.Label(self.frame, text = "Min", width = 10)
        self.min_size.grid(row = 0, column = 2, padx = 5, pady = 5)
        
        self.min_entry = tk.Entry(self.frame, width = 10)
        self.min_entry.grid(row = 0, column = 3, padx = 5, pady = 5)
        
        self.max_size = tk.Label(self.frame, text = "Max", width = 10)
        self.max_size.grid(row = 0, column = 4, padx = 5, pady = 5)
        
        self.max_entry = tk.Entry(self.frame, width = 10)
        self.max_entry.grid(row = 0, column = 5, padx = 5, pady = 5)
        
        self.sim_label = tk.Label(self.frame, text = "Sorting Speed: ", width = 25)
        self.sim_label.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        self.sim_speed = tk.Scale(self.frame, from_ = 0, to = .5, length = 100, digits = 1, 
                              resolution = 0.25, width = 10, orient = "horizontal", 
                              sliderlength = 5, troughcolor = "#bbace8")
        self.sim_speed.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        self.generate_btn = tk.Button(self.frame, text = "Generate New Array", 
                           width = 20, bg = "#99cfff", command = self.generate_list)
        self.generate_btn.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5) 
    
        self.sort_btn = tk.Button(self.frame, text = "Sort Array", width = 20, bg = "#99cfff", command = self.sort)
        self.sort_btn.grid(row = 1, column = 4, columnspan = 2, padx = 5, pady = 5)
        
    def generate_list(self):
        """
        generates a list of 100 random integers
        """
        try:
            self.min_val = int(self.min_entry.get())    
        except ValueError:
            self.min_val = 10
        try:    
            self.max_val = int(self.max_entry.get())
        except:
            self.max_val = 10000
        self.speed = int(self.sim_speed.get())
        self.data = []
        for i in range(100):
            self.data.append(random.randint(self.min_val, self.max_val))
       
        self.draw(self.data, ["#a871e3" for x in range(len(self.data))])
        
    def draw(self, data, color):
        """
        draws normalized bars on the canvas
        :param data: list containing the 100 randomly generated integers
        :param color: hex color to color the data bars
        :return: None
        """
        self.canvas.delete("all")
        self.c_width = 770
        self.c_height = 300
        self.bar_width = self.c_width / (len(data)+1)
        self.offset = 5
        self.space = 2
        
        data_normalized = [i / max(data) for i in data]
        
        for i, height in enumerate(data_normalized):
            x0 = i * self.bar_width + self.offset + self.space
            y0 = self.c_height - height * 280
            x1 = (i+1) * self.bar_width + self.offset
            y1 = self.c_height
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill = color[i])
        self.window.update_idletasks()
    
    def sort(self):
        """
        visulaizes the selected sorting algorithm
        """
        if self.alg_dropdown.get() == "Bubble Sort":
            bubble_sort(self.data, self.draw, self.sim_speed.get())
        elif self.alg_dropdown.get() == "Merge Sort":
            merge_sort(self.data,0, len(self.data)-1, self.draw, self.sim_speed.get())
        elif self.alg_dropdown.get() == "Insertion Sort":
            insertion_sort(self.data, self.draw, self.sim_speed.get())
        elif self.alg_dropdown.get() == "Selection Sort":
            selection_sort(self.data, self.draw, self.sim_speed.get())
        elif self.alg_dropdown.get() == "Quick Sort":
            quick_sort( self.data, 0, len(self.data)-1, self.draw, self.sim_speed.get())
        elif self.alg_dropdown.get() == "Heap Sort":
            Heap_Sort(self.data, self.draw, self.sim_speed.get())
        self.draw(self.data, ["#03f0fc" for x in range(len(self.data))])
        
def main():
    """
    used to run the gui
    """
    root = tk.Tk()
    SortingVisualizer(root).draw_ui()
    root.mainloop()
if __name__ == "__main__":
    main()


