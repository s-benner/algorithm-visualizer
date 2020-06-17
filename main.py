import tkinter as tk
from tkinter import ttk
import config

"""Application class definition"""
"""----------------------------"""
class Application(tk.Tk):

    # attributes
    frames = [] # contains the the frames of the application

    # constructor method
    def __init__(self, *args, **kwargs):
        # call the Tk constructor from tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, config.WINDOW_TITLE)

        # create a tkinter frame object that will be holding all contents (mainframe)
        mainframe = tk.Frame(self)
        mainframe.grid(row=1, column=1)
        mainframe.grid_rowconfigure(0, weight=1)
        mainframe.grid_columnconfigure(0, weight=1)

        # create the program frames
        titleframe = TitleFrame(mainframe, self)
        titleframe.grid_propagate(0)
        titleframe.grid(row=1, column=1, columnspan=2)
        titleframe.display_contents()

        menuframe = MenuFrame(mainframe, self)
        menuframe.grid_propagate(0)
        menuframe.grid(row=2, column=1, columnspan=2)
        menuframe.display_contents()

        appframe = AppFrame(mainframe, self)
        appframe.grid(row=3, column=1)
        appframe.grid_propagate(0)
        appframe.display_contents()

        logframe = LogFrame(mainframe, self)
        logframe.grid(row=3, column=2)
        logframe.grid_propagate(0)
        logframe.display_contents()

"""end of class definition"""

"""title frame class definition"""
"""----------------------------"""
class TitleFrame(tk.Frame):

    label_text = ""
    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH, height=config.TITLE_HEIGHT, background=config.COLOR_BG)
        self.label_text = tk.StringVar()
        self.label_text.set(self.update_contents(0,0))

        self.display_objects.append(tk.Label(self, textvariable=self.label_text, background=config.COLOR_BG, foreground=config.COLOR_TEXT1))

    def display_contents(self):
        for do in self.display_objects:
            do.grid(row=1,column=1)

    def update_contents(self, algotype, algoname):
        temp=""
        if algotype == 0: temp ="Welcome to "
        temp += "Algorithm Visualizer"
        if algotype == 0: temp += " - please select the algorithm you wish to visualize below!"
        if not algotype == 0: temp += " - "+config.ALGO_TYPES[algotype]
        if not algoname == 0: temp += " - "+config.ALGO_NAMES[algotype][algoname]
        return temp

"""end of class definition"""

"""menu frame class definition"""
"""---------------------------"""
class MenuFrame(tk.Frame):

    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH, height=config.TITLE_HEIGHT, background=config.COLOR_BG)

        self.display_objects.append(tk.Label(self, text="Pick your algorithm category:", background=config.COLOR_BG, foreground=config.COLOR_TEXT1))
        self.display_objects.append(tk.Label(self, text="Menü1", background=config.COLOR_BG, foreground=config.COLOR_TEXT1))
        self.display_objects.append(tk.Label(self, text="Pick your algorithm:", background=config.COLOR_BG, foreground=config.COLOR_TEXT1))
        self.display_objects.append(tk.Label(self, text="Menü2", background=config.COLOR_BG, foreground=config.COLOR_TEXT1))
        self.display_objects.append(tk.Label(self, text="Set up my workspace!", background=config.COLOR_BG, foreground=config.COLOR_TEXT1))

    def display_contents(self):
        for i,do in enumerate(self.display_objects):
            do.grid(row=1, column=i)

"""end of class definition"""

"""application frame class definition"""
"""----------------------------"""
class AppFrame(tk.Frame):

    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH-config.LOG_WIDTH, height=config.APPLICATION_HEIGHT)
        self.display_objects.append(tk.Label(self, text="appframe"))

    def display_contents(self):
        for do in self.display_objects:
            do.pack()

"""end of class definition"""

"""application frame class definition"""
"""----------------------------"""
class LogFrame(tk.Frame):

    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.LOG_WIDTH, height=config.APPLICATION_HEIGHT)
        self.display_objects.append(tk.Label(self, text="logframe"))

    def display_contents(self):
        for do in self.display_objects:
            do.pack()

"""end of class definition"""


"""Create the application object and run the mainloop"""
root = Application()
root.mainloop()
