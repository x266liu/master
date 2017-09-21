from tkinter import *
from tkinter import ttk
import l_toplevel
import l_subwin

class loonPlotFactory:
    def __init__(self, factory_tclcmd, factory_path, factory_window_title="loon plot", parent = None):
        self.factory_tclcmd = factory_tclcmd
        self.factory_path = factory_path
        self.factory_window_title = "loon plot"
        self.parent = parent
    
    def lpf(self):
        new.toplevel = True
        
        
#Tk.call() tcl() in r


root = Tk()
root.title("loon plot")
factory = ttk.Frame(root)
#ttk.Button(root, text = "Hello World").grid()
root.mainloop()