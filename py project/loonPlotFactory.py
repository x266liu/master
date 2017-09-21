from tkinter import *
from tkinter import ttk
import l_toplevel
import l_subwin

class loonPlotFactory(Frame) :
    def __init__(self, patent = None):
        selffactory_tclcmd, factory_path, factory_window_title = "loon plot"
    
    

root = Tk()
root.title("loon plot")
factory = ttk.Frame(root)
#ttk.Button(root, text = "Hello World").grid()
root.mainloop()