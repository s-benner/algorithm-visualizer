import random
import tkinter as tk
import config

"""Sorting problem class definition"""
"""--------------------------------"""

class SortingProblem():

    # attributes
    list_to_sort = [] # contains the values to be sorted
    list_of_status = [] # contains the status flag for each element for the visualization
    logfile = "" # contains all log entries
    problem_size = 0 # number of elements to be sorted
    parent_frame = None # reference to the frame where the visualization is to be placed
    log_frame = None # reference to the frame where the log is to be placed
    canvas = None
    display_objects = []
    appl = None

    def __init__(self, appframe, logframe, application):
        self.parent_frame = appframe
        self.log_frame = logframe
        self.list_to_sort = []
        self.list_of_status = []
        self.problem_size = 0
        self.display_objects = []
        self.logfile = tk.Text(self.log_frame)
        self.appl = application

        # print the instructions

        inst_lines = []
        inst_lines.append("Instructions:")
        inst_lines.append("1. Select the number of elements you wish to sort in the menu on the right and hit the create Problem button. Your list to sort will be created automatically.")
        inst_lines.append("2. In the log section to the right, select the simulation speed and hit run. If you hit step, the algorithm will only perform a single step.")

        for line in inst_lines:
            temp = tk.Label(self.parent_frame, text=line, font="Calibri 9", background=config.COLOR_BG3, anchor="w")
            temp.pack()

        # create the canvas for the actual animation
        self.canvas=tk.Canvas(appframe, width=config.CANVAS_WIDTH, height=config.CANVAS_HEIGHT, background=config.COLOR_BG3)
        self.canvas.pack()

        # create a problem, this will be later replaced by the button
        self.create_random_problem(6)
        self.visualize()



    def visualize(self):
        self.canvas.delete("all")
        self.canvas.create_line(2, 2, config.CANVAS_WIDTH, 2, config.CANVAS_WIDTH, config.CANVAS_HEIGHT, 2,config.CANVAS_HEIGHT, 2, 2)
        interval = (config.CANVAS_WIDTH-40) // self.problem_size
        for i,element in enumerate(self.list_to_sort):
            self.canvas.create_rectangle(20+i*interval,2,20+(i+1)*interval-3,0.95*element*config.CANVAS_HEIGHT/1000, fill=config.ANIM_COLORS[self.list_of_status[i]])

    def create_random_problem(self, count):
        self.problem_size = min(count,100)
        for i in range(self.problem_size):
            self.list_to_sort.append(int(((random.random()*1000)//1)+50))
            self.list_of_status.append(0)
        logtext = "Problem with " + str(self.problem_size) + " elements created!"
        self.appl.logoframe.update_log_box(logtext, [])


"""end of class definition"""

"""Bubble Sort Solver implementation"""
"""---------------------------------"""

class BubbleSolver():
    speed = 100
    solved = False
    application = None
    step_id = 0
    problem = None
    pointer = 0
    element1 = 0
    element2 = 0
    swap = 0
    max_index = 0

    def __init__(self, application, problem):
        self.application = application
        self.problem = problem
        self.max_index = problem.problem_size - 1

    def setup_log(self):
        pass

    def step(self):
        if self.solved: return
        logtext = ""
        logcoloring = []
        # step 0: select first element for comparison
        if self.step_id == 0:
            self.element1 = self.problem.list_to_sort[self.pointer]
            self.problem.list_of_status[self.pointer] = 1
            logtext = "Pick element "
            l1 = "1."+str(len(logtext))
            logtext += str(self.element1)
            l2 = "1."+str(len(logtext))
            logtext += " for comparison"
            logcoloring.append(["col1",l1,l2])
        # step 1: select second element for comparison
        if self.step_id == 1:
            self.element2 = self.problem.list_to_sort[self.pointer+1]
            self.problem.list_of_status[self.pointer+1] = 2
            logtext = "Pick element "
            l1 = "1."+str(len(logtext))
            logtext += str(self.element2)
            l2 = "1."+str(len(logtext))
            logtext+= " for comparison"
            logcoloring.append(["col2",l1,l2])
        # step 2: do comparison
        if self.step_id == 2:
            l1 = "1.0"
            logtext = str(self.element1)
            l2 = "1."+str(len(logtext))
            if self.element1 > self.element2:
                self.swap = 1
                logtext += " < "
            else:
                self.step_id += 1
                logtext += " < "
            l3 = "1."+str(len(logtext))
            logtext += str(self.element2)
            l4 = "1."+str(len(logtext))
            logtext += " -> swap" if self.element1 > self.element2 else " -> no swap"
            logcoloring.append(["col1",l1,l2])
            logcoloring.append(["col2",l3,l4])
        # step 3: swap if required
        if self.step_id == 3:
            if self.swap == 1:
                self.problem.list_to_sort[self.pointer], self.problem.list_to_sort[self.pointer+1] = self.problem.list_to_sort[self.pointer+1], self.problem.list_to_sort[self.pointer]
                self.problem.list_of_status[self.pointer], self.problem.list_of_status[self.pointer+1] = self.problem.list_of_status[self.pointer+1], self.problem.list_of_status[self.pointer]
                self.swap = 0
                logtext = "Swapped "
                l1 = "1."+str(len(logtext))
                logtext += str(self.element2)
                l2 = "1."+str(len(logtext))
                logtext += " and "
                l3 = "1."+str(len(logtext))
                logtext += str(self.element1)
                l4 = "1."+str(len(logtext))
                logcoloring.append(["col2",l1,l2])
                logcoloring.append(["col1",l3,l4])
        # step 4: start next iteration
        if self.step_id == 4:
            self.problem.list_of_status[self.pointer], self.problem.list_of_status[self.pointer + 1] = 0, 0
            self.pointer += 1
            logtext = "Start next iteration"
        # increment step id, call visualization
        self.step_id = (self.step_id + 1) % 5

        if self.pointer == (self.max_index):
            if self.max_index == 1:
                self.problem.list_of_status[1], self.problem.list_of_status[0] = 3, 3
                self.solved = True
                logtext = "Elements "
                l1 = "2."+str(len(logtext))
                logtext += str(self.problem.list_to_sort[1])
                l2 = "2."+str(len(logtext))
                logtext += ", "
                l3 = "2."+str(len(logtext))
                logtext += str(self.problem.list_to_sort[0])
                l4 = "2."+str(len(logtext))
                logtext += " have reached correct position"
                logtext = "Sorting complete!\n" + logtext
                logcoloring.append(["col3",l1,l2])
                logcoloring.append(["col3",l3,l4])
            else:
                self.problem.list_of_status[self.max_index] = 3
                self.max_index -= 1
                logtext = "Element "
                l1 = "1."+str(len(logtext))
                logtext += str(self.problem.list_to_sort[self.pointer])
                l2 = "1."+str(len(logtext))
                logtext += " in correct position"
                logcoloring.append(["col3",l1,l2])
            self.pointer = 0

        self.application.problem.visualize()
        self.application.logoframe.update_log_box(logtext, logcoloring)

    def run(self):
        self.step()
        if self.solved == True: return
        self.application.after(int(1000//self.speed), self.run)

"""end of class definition"""

"""Quick Sort Solver implementation"""
"""---------------------------------"""

class QuickSolver():
    sublists = []
    active_sublist = None
    current_pivot = -1
    speed = 10
    solved = False
    application = None
    step_id = 0
    problem = None
    pointer1 = 0
    pointer2 = 0
    swapin = -1
    sublistshow = 0
    max_index = 0

    def __init__(self, application, problem):
        self.application = application
        self.problem = problem
        self.sublists.append((0,problem.problem_size-1))

    def setup_log(self):
        pass

    def step(self):
        logtext = ""
        logcoloring = []
        # step 0 pop sublist from stack and show the selected sublist
        if self.step_id == 0:
            if not self.swapin == -1:
                self.problem.list_of_status[self.current_pivot], self.problem.list_of_status[self.swapin] = 0,0
                if not self.pointer1 == -1: self.problem.list_of_status[self.pointer1] = 0
                self.problem.list_of_status[self.swapin] = 3
                self.swapin = -1
            if not self.sublists:
                self.solved = True
                return
            if self.active_sublist == None: self.active_sublist = self.sublists.pop(0)
            for i in range(self.active_sublist[0],self.active_sublist[1]+1):
                self.problem.list_of_status[i] = 4
            self.sublistshow = 1
            self.current_pivot = -1
        # step 1: select pivot element
        if self.step_id == 1:
            # unshow the selected sublist
            if self.sublistshow == 1:
                for i in range(self.active_sublist[0], self.active_sublist[1] + 1):
                    self.problem.list_of_status[i] = 0
                self.sublistshow = 0
            # select pivot element and show it
            if self.current_pivot == -1:
                self.pointer1, self.pointer2 = -1,-1
                self.current_pivot = random.randint(self.active_sublist[0], self.active_sublist[1])
                self.problem.list_of_status[self.current_pivot] = 6
                # check if the length is only 1
                if self.active_sublist[0] - self.active_sublist[1] == 0:
                    self.swapin = self.current_pivot
                    self.step_id = 9
                else:
                    # set the pointers to the outmost element, unless its the pivot
                    self.pointer1 = self.active_sublist[0] if not self.active_sublist[0] == self.current_pivot else self.active_sublist[0] + 1
                    self.pointer2 = self.active_sublist[1] if not self.active_sublist[1] == self.current_pivot else self.active_sublist[1] - 1
            else:
                self.step_id += 1
        # step 2: mark both pointers
        if self.step_id == 2:
            self.problem.list_of_status[self.pointer1] = 1
            self.problem.list_of_status[self.pointer2] = 2
            if self.pointer1 == self.pointer2: self.step_id = 7
        # step 3: find element from the left that is bigger than pivot element
        if self.step_id == 3:
            # check the initial/last selection, if not, we have to keep going
            if not self.problem.list_to_sort[self.pointer1] > self.problem.list_to_sort[self.current_pivot]:
                # unmark the current selection
                self.problem.list_of_status[self.pointer1] = 0
                # advance the pointer
                self.pointer1 = self.pointer1 + 1 if not self.pointer1 +1 == self.current_pivot else self.pointer1 +2
                # mark the new element
                self.problem.list_of_status[self.pointer1] = 1
                # if the pointer have met, go directly to step 7
                if self.pointer1 == self.pointer2: self.step_id = 7
                elif not self.problem.list_to_sort[self.pointer1] > self.problem.list_to_sort[self.current_pivot]: self.step_id = 2
        # step 4: find element from the right that is smaller than the pivot
        if self.step_id == 4:
            # check the initial/last selection, if not, we have to keep going
            if not self.problem.list_to_sort[self.pointer2] < self.problem.list_to_sort[self.current_pivot]:
                # unmark the current selection
                self.problem.list_of_status[self.pointer2] = 0
                # advance the pointer
                self.pointer2 = self.pointer2 - 1 if not self.pointer2 - 1 == self.current_pivot else self.pointer2 - 2
                # mark the new element
                self.problem.list_of_status[self.pointer2] = 2
                # if the pointer have met, go directly to step 7
                if self.pointer1 == self.pointer2: self.step_id = 7
                elif not self.problem.list_to_sort[self.pointer2] < self.problem.list_to_sort[self.current_pivot]: self.step_id = 3
        # step 5: execute swap
        if self.step_id == 5:
            self.problem.list_to_sort[self.pointer1], self.problem.list_to_sort[self.pointer2] = self.problem.list_to_sort[self.pointer2], self.problem.list_to_sort[self.pointer1]
            self.problem.list_of_status[self.pointer1], self.problem.list_of_status[self.pointer2] = self.problem.list_of_status[self.pointer2], self.problem.list_of_status[self.pointer1]
        # step 6: unmark swap, advance pointers, mark new starting positions and continue with step 3
        if self.step_id == 6:
            self.problem.list_of_status[self.pointer1], self.problem.list_of_status[self.pointer2] = 0, 0
            self.step_id = 2
            # check if the next element is the pivot, then advance 2 steps
            self.pointer1 = self.pointer1 + 1 if not self.pointer1 + 1 == self.current_pivot else self.pointer1 + 2
            self.problem.list_of_status[self.pointer1] = 1
            if self.pointer1 == self.pointer2: self.step_id = 7
            self.pointer2 = self.pointer2 - 1 if not self.pointer2 - 1 == self.current_pivot else self.pointer2 - 2
            self.problem.list_of_status[self.pointer2] = 2
            if self.pointer1 == self.pointer2: self.step_id = 7
        # step 7: if the pointers have met, show where they met
        if self.step_id == 7:
            self.problem.list_of_status[self.pointer2], self.problem.list_of_status[self.pointer1] = 0,0
            self.problem.list_of_status[self.pointer1] = 5
        # step 8: identify the swap in partner for the pivot element and mark it
        if self.step_id == 8:
            # cases where the pivot element and the meet element need to be switched:
            if (self.current_pivot > self.pointer1 and self.problem.list_to_sort[self.pointer1] > self.problem.list_to_sort[self.current_pivot]) or (self.current_pivot < self.pointer1 and self.problem.list_to_sort[self.pointer1] <self.problem.list_to_sort[self.current_pivot]):
                self.swapin = self.pointer1
            if (self.current_pivot < self.pointer1 and self.problem.list_to_sort[self.pointer1] > self.problem.list_to_sort[self.current_pivot]):
                self.swapin = self.pointer1 -1
            if (self.current_pivot > self.pointer1 and self.problem.list_to_sort[self.pointer1] < self.problem.list_to_sort[self.current_pivot]):
                self.swapin = self.pointer1 +1
            if self.problem.list_to_sort[self.pointer1] == self.problem.list_to_sort[self.current_pivot]: self.swapin = self.current_pivot
        #step 9: execute the swapin of the pivot
        if self.step_id == 9:
            if self.swapin == -1:
                self.solved = True
                return
            self.problem.list_to_sort[self.swapin], self.problem.list_to_sort[self.current_pivot] = self.problem.list_to_sort[self.current_pivot], self.problem.list_to_sort[self.swapin]
            self.problem.list_of_status[self.swapin], self.problem.list_of_status[self.current_pivot] = self.problem.list_of_status[self.current_pivot], self.problem.list_of_status[self.swapin]
            if self.swapin+1 <= self.active_sublist[1]:
                self.sublists.insert(0, (self.swapin+1,self.active_sublist[1]))
            if self.swapin - 1 >= self.active_sublist[0]:
                self.sublists.insert(0, (self.active_sublist[0], self.swapin - 1))
            self.active_sublist = None

        # increment step id, call visualization
        self.step_id = (self.step_id + 1) % 10
        self.application.problem.visualize()
        self.application.logoframe.update_log_box(logtext, logcoloring)

    def run(self):
        self.step()
        if self.solved == True:
            self.problem.list_of_status[self.current_pivot] = 3
            self.application.problem.visualize()
            return
        self.application.after(int(1000//self.speed), self.run)

"""end of class definition"""