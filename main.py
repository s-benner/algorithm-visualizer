import tkinter as tk # for gui
from tkinter import ttk # for advanced gui styling
import config # for config variables

"""Application class definition"""
"""----------------------------"""
class Application(tk.Tk):
    """This class holds the application itself, so it inherits from Tk class. It basically contains the frame
    for the display and the problem and solver objects, that are active """

    # attributes
    mainframe = None # frame that holds everything else
    titleframe = None # frame or the program title
    menuframe = None # frame sor the selection of the problem and the solver method
    appframe = None # frame for the actual animation
    logframe = None # frame for simulation settings
    logoframe = None # frame for the simulation log
    problem = None # class that contains the problem to be solved
    solver = None # class that contains the algorithm logic

    """constructor method"""
    def __init__(self, *args, **kwargs):
        # call the Tk constructor from tkinter and set the window title
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, config.WINDOW_TITLE)
        # create a tkinter frame object that will be holding all contents (mainframe)
        self.mainframe = tk.Frame(self, background=config.COLOR_BG2)
        self.mainframe.grid(row=1, column=1)
        self.mainframe.grid_rowconfigure(0, weight=1)
        self.mainframe.grid_columnconfigure(0, weight=1)
        # create the title frame
        self.titleframe = TitleFrame(self.mainframe, self)
        self.titleframe.grid_propagate(0)
        self.titleframe.grid(row=1, column=1, columnspan=2)
        self.titleframe.display_contents()
        # create the menu frame
        self.menuframe = MenuFrame(self.mainframe, self)
        self.menuframe.grid_propagate(0)
        self.menuframe.grid(row=2, column=1, columnspan=2)
        self.menuframe.display_contents()
        # create the appframe by a method, because the method is needed to reset the frame for a new problem
        self.recreate_apframe()
        #create the logframe
        self.logframe = LogFrame(self.mainframe, self)
        self.logframe.grid(row=3, column=2)
        self.logframe.grid_propagate(0)
        self.logframe.display_contents()
        # create the log frame, where the simulation log is presented
        self.logoframe = LogoFrame(self.mainframe, self)
        self.logoframe.grid (row=4, column=2)
        self.logoframe.grid_propagate(0)

    """method that sets up a new problem and solver"""
    def setup_workspace(self, algotype, algoid):
        # clear the appframe
        self.recreate_apframe()
        # create the problem and solver objects
        p = config.ALGO_PROBLEM_CLASSES[algotype]
        self.problem = p(self.appframe, self.logframe, self)
        s = config.ALGO_SOLVER_CLASSES[algotype][algoid]
        self.solver = s(self, self.problem)
        # create the control buttons in the logframe
        self.logframe.init_step_button(self.solver)

    """method to reset and recreate the appframe for a new problem"""
    def recreate_apframe(self):
        # destroy the current appframe
        if self.appframe: self.appframe.destroy()
        # create the appframe
        self.appframe = AppFrame(self.mainframe, self)
        self.appframe.grid(row=3, column=1, rowspan=2)
        self.appframe.grid_propagate(0)
        self.appframe.display_contents()

"""end of class definition"""

"""title frame class definition"""
"""----------------------------"""
class TitleFrame(tk.Frame):

    label_text = None
    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH, height=config.TITLE_HEIGHT, background=config.COLOR_BG1,padx=0,pady=0)
        self.label_text = tk.StringVar()
        self.update_contents(0,0)
        self.display_objects.append(tk.Label(self, textvariable=self.label_text, background=config.COLOR_BG1, foreground=config.COLOR_TEXT1, font="Calibri 9 bold"))

    def display_contents(self):
        for do in self.display_objects:
            do.place(relx=.5, rely=.5, anchor="center")

    def update_contents(self, algotype, algoname):
        temp=""
        if algotype == 0 and algoname == 0: temp ="Welcome to "
        temp += "Algorithm Visualizer"
        if algotype == 0 and algoname == 0: temp += " - please select the algorithm you wish to visualize below!"
        if not algotype == 0: temp += " - "+config.ALGO_TYPES[algotype]
        if not algoname == 0: temp += " - "+config.ALGO_NAMES[algotype][algoname]
        self.label_text.set(temp)

"""end of class definition"""

"""menu frame class definition"""
"""---------------------------"""
class MenuFrame(tk.Frame):

    display_objects = []
    appl = None
    lastalgotype = 0
    lastalgoname = 0

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH, height=config.TITLE_HEIGHT, background=config.COLOR_BG1)
        self.appl = application

        self.display_objects.append(tk.Label(self, text="Pick your algorithm category:   ", background=config.COLOR_BG1, foreground=config.COLOR_TEXT1))

        algotypes = config.ALGO_TYPES
        self.selected_algotype = tk.StringVar(application)
        self.selected_algotype.trace("w", lambda *args: self.input_menu_changed())
        self.menu1 = ttk.OptionMenu(self, self.selected_algotype, algotypes[0], *algotypes)
        self.menu1.config(width=config.DROPDOWNMENU_WIDTH)
        self.display_objects.append(self.menu1)

        self.display_objects.append(tk.Label(self, text="   Pick your algorithm:   ", background=config.COLOR_BG1, foreground=config.COLOR_TEXT1))

        self.algonames = tk.StringVar(application)
        self.algonames.set([""])
        self.selected_algoname = tk.StringVar(application)
        self.selected_algoname.trace("w", lambda *args: self.input_menu_changed())
        self.menu2 = ttk.OptionMenu(self, self.selected_algoname, "", "")
        self.menu2.config(width=config.DROPDOWNMENU_WIDTH)
        self.display_objects.append(self.menu2)

        self.display_objects.append(tk.Button(self, text="Set up my workspace!", background=config.COLOR_BG1, foreground=config.COLOR_TEXT1))

    def input_menu_changed(self):
        # get the ids of the selected algorithm type and name
        algotype = int(config.ALGO_TYPES.index(self.selected_algotype.get()))
        # if the algotype has been changed
        if not algotype == self.lastalgotype:
            # clear second menu
            self.menu2['menu'].delete(0, 'end')
            # create new second menu
            menuentries = []
            if not algotype == 0: menuentries = config.ALGO_NAMES[algotype][1:]
            self.menu2['menu'].delete(0, 'end')
            for entry in menuentries:
                self.menu2['menu'].add_command(label=entry, command=lambda arg=entry: self.selected_algoname.set(arg))
            # remove previous selection of the second menu
            algoname = 0
            self.selected_algoname.set("")
            # store last selected algo type
            self.lastalgotype = algotype
        # if the algoname was changed
        else:
            algoname = int(config.ALGO_NAMES[algotype].index(self.selected_algoname.get()))
        # update the titleframe by calling the respective method passing the ids
        self.appl.titleframe.update_contents(algotype, algoname)
        self.display_objects[-1].configure(command=lambda arg1=algotype, arg2=algoname: self.appl.setup_workspace(arg1, arg2))

    def display_contents(self):
        for i,do in enumerate(self.display_objects):
            do.grid(row=1, column=i)

"""end of class definition"""

"""application frame class definition"""
"""----------------------------------"""
class AppFrame(tk.Frame):

    display_objects = []

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.APPLICATION_WIDTH-config.LOG_WIDTH, height=config.APPLICATION_HEIGHT, background=config.COLOR_BG3, padx=0, pady=0)

    def display_contents(self):
        for do in self.display_objects:
            do.grid()

"""end of class definition"""

"""logo frame class definition"""
"""---------------------------"""
class LogoFrame(tk.Frame):

    logtextbox = None
    appl = None

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.LOG_WIDTH, height=config.APPLICATION_HEIGHT-100, background=config.COLOR_BG2, padx=5)
        self.appl = application
        frametitle = tk.Label(self, text="Simulation Log:", font="Calibri 11 bold", background=config.COLOR_BG2, anchor="w", width=config.LOG_LABEL_WIDTH+11)
        self.logtextbox = tk.Text(self, height=34, width=39, font="Calibri 8", background=config.COLOR_BG1, foreground=config.COLOR_BG3)
        frametitle.grid(row=1, column=1)
        self.logtextbox.grid(row=2, column=1)
        self.logtextbox.config(state='disabled')
        for i in range(len(config.ANIM_COLORS)):
            self.logtextbox.tag_configure("col"+str(i), foreground=config.ANIM_COLORS[i])

    def clear_text_widget(self):
        self.logtextbox.config(state='normal')
        self.logtextbox.delete("1.0", "end")
        self.logtextbox.config(state='disabled')

    def update_log_box(self, string, coloring):
        self.logtextbox.config(state='normal')
        self.logtextbox.insert("1.0", (string + "\n"))
        for mark in coloring:
            self.logtextbox.tag_add(mark[0], mark[1], mark[2])
        self.logtextbox.config(state='disabled')
        self.appl.update()

"""end of class definition"""

"""log frame class definition"""
"""--------------------------"""
class LogFrame(tk.Frame):

    display_objects = []
    display_objects_grid_params = []
    appl = None
    logtext = None

    def __init__(self, parent, application):
        tk.Frame.__init__(self, parent, width=config.LOG_WIDTH, height=100, background=config.COLOR_BG2, padx=5)
        self.display_objects.append(tk.Label(self, text="Simulation Settings:", font="Calibri 11 bold", background=config.COLOR_BG2, anchor="w", width=config.LOG_LABEL_WIDTH))
        self.display_objects_grid_params.append((1,1))
        self.display_objects.append(tk.Label(self, text="Simulation Speed:", font="Calibri 9", background=config.COLOR_BG2, anchor="w", width=config.LOG_LABEL_WIDTH))
        self.display_objects_grid_params.append((2, 1))
        #self.display_objects.append(tk.Label(self, text="Simulation Log:", font="Calibri 11 bold", background=config.COLOR_BG2, anchor="w", width=config.LOG_LABEL_WIDTH))
        #self.display_objects_grid_params.append((4, 1))

        self.appl = application

    def init_step_button(self, solver):
        self.display_objects.append(tk.Button(self, text="Step", font="Calibri 9", background=config.COLOR_BG2, anchor="w", width=config.LOG_LABEL_WIDTH-10, command=solver.step))
        self.display_objects_grid_params.append((3, 1))
        self.display_objects[-1].grid(row=self.display_objects_grid_params[-1][0], column=self.display_objects_grid_params[-1][1])

        self.display_objects.append(tk.Button(self, text="Run", font="Calibri 9", background=config.COLOR_BG2, anchor="w",width=config.LOG_LABEL_WIDTH - 10, command=solver.run))
        self.display_objects_grid_params.append((3, 2))
        self.display_objects[-1].grid(row=self.display_objects_grid_params[-1][0],column=self.display_objects_grid_params[-1][1])

    def display_contents(self):
        for i,do in enumerate(self.display_objects):
            do.grid(row=self.display_objects_grid_params[i][0], column=self.display_objects_grid_params[i][1])

"""end of class definition"""

"""Create the application object and run the mainloop"""
root = Application()
root.mainloop()