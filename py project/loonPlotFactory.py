from tkinter import *
from tkinter import ttk
import l_toplevel
import l_subwin


root = Tk()

class loonPlotFactory:
    def __init__(self, factory_tclcmd, factory_path, factory_window_title="loon plot", parent = None, *therest):
        self.factory_tclcmd = factory_tclcmd
        self.factory_path = factory_path
        self.factory_window_title = "loon plot"
        self.parent = parent
    
    def lpf(self):
        new.toplevel = True
        if parent is None:
            new.toplevel = False
            parent = l_toplevel
        
        child = l_subwin(parent, factory_path)
        try:
            plot = root.tk.call(factory_tclcmd, child, *lst)
        except:   
            if new.toplevel:
                parent.destroy()    
            
                
                
        
#Tk.call() tcl() in r


#root = Tk()
root.title("loon plot")
factory = ttk.Frame(root)
#ttk.Button(root, text = "Hello World").grid()
root.mainloop()