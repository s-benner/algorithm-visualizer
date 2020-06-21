import random
import tkinter as tk
import config

"""Sorting problem class definition"""
"""--------------------------------"""

class SortingProblem():

    # attributes
    list_to_sort = [] # contains the values to be sorted
    list_of_status = [] # contains the status flag for each element for the visualization
    logfile = [] # contains all log entries
    problem_size = 0 # number of elements to be sorted
    parent_frame = None # reference to the frame where the visualization is to be placed
    log_frame = None # reference to the frame where the log is to be placed
    canvas = None
    display_objects = []

    def __init__(self, appframe, logframe):
        self.parent_frame = appframe
        self.log_frame = logframe

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
        self.create_random_problem(10)
        self.visualize()



    def visualize(self):
        self.canvas.delete("all")
        self.canvas.create_line(2, 2, config.CANVAS_WIDTH, 2, config.CANVAS_WIDTH, config.CANVAS_HEIGHT, 2,config.CANVAS_HEIGHT, 2, 2)
        interval = (config.CANVAS_WIDTH-40) // self.problem_size
        for i,element in enumerate(self.list_to_sort):
            self.canvas.create_rectangle(20+i*interval,2,20+(i+1)*interval-3,0.95*element*config.CANVAS_HEIGHT/1000, fill=config.ANIM_COLORS[self.list_of_status[i]])

    def update_log(self):
        pass

    def create_random_problem(self, count):
        self.problem_size = min(count,100)
        for i in range(self.problem_size):
            self.list_to_sort.append(int(((random.random()*1000)//1)+50))
            self.list_of_status.append(0)
        self.logfile.append("Array of " + str(self.problem_size) + "elements generated")


"""end of class definition"""

"""Bubble Sort Solver implementation"""
"""---------------------------------"""

class BubbleSolver():
    speed = 10
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
        # step 0: select first element for comparison
        if self.step_id == 0:
            self.element1 = self.problem.list_to_sort[self.pointer]
            self.problem.list_of_status[self.pointer] = 1
        # step 1: select second element for comparison
        if self.step_id == 1:
            self.element2 = self.problem.list_to_sort[self.pointer+1]
            self.problem.list_of_status[self.pointer+1] = 2
        # step 2: do comparison
        if self.step_id == 2:
            if self.element1 > self.element2: self.swap = 1
            else: self.step_id += 1
        # step 3: swap if required
        if self.step_id == 3:
            if self.swap == 1:
                self.problem.list_to_sort[self.pointer], self.problem.list_to_sort[self.pointer+1] = self.problem.list_to_sort[self.pointer+1], self.problem.list_to_sort[self.pointer]
                self.problem.list_of_status[self.pointer], self.problem.list_of_status[self.pointer+1] = self.problem.list_of_status[self.pointer+1], self.problem.list_of_status[self.pointer]
                self.swap = 0
        # step 4: start next iteration
        if self.step_id == 4:
            self.problem.list_of_status[self.pointer], self.problem.list_of_status[self.pointer + 1] = 0, 0
            self.pointer += 1
        # increment step id, call visualization
        self.step_id = (self.step_id + 1) % 5

        if self.pointer == (self.max_index):
            if self.max_index == 1: self.solved = True
            else: self.max_index -= 1
            self.pointer = 0

        self.application.problem.visualize()


    def run(self):
        self.step()
        if self.solved == True: return
        self.application.after(int(1000//self.speed), self.run)

"""end of class definition"""

"""Bubble Sort Solver implementation"""
"""---------------------------------"""

class QuickSolver():
    sublists = []
    active_sublist = None
    current_pivot = -1
    speed = 0.4
    solved = False
    application = None
    step_id = 0
    problem = None
    pointer1 = 0
    pointer2 = 0
    element1 = 0
    element2 = 0
    swap = 0
    max_index = 0

    def __init__(self, application, problem):
        self.application = application
        self.problem = problem
        self.sublists.append((0,problem.problem_size-1))

    def setup_log(self):
        pass

    def step(self):
        # step 0 (not animated) pop sublist from stack
        if self.step_id == 0:
            if self.active_sublist == None: self.active_sublist = self.sublists.pop(0)
            self.step_id += 1
            print(self.active_sublist)
        # step 1: select pivot element
        if self.step_id == 1:
            if self.current_pivot == -1:
                self.current_pivot = random.randint(self.active_sublist[0], self.active_sublist[1])
                self.problem.list_of_status[self.current_pivot] = 3
                self.pointer1 = self.active_sublist[0]
                if self.pointer1 == self.current_pivot: self.pointer1 += 1
                self.pointer2 = self.active_sublist[1]
                if self.pointer2 == self.current_pivot: self.pointer2 -= 1
                print(self.pointer1)
                print(self.pointer2)
            else:
                self.step_id += 1
        # step 2: find element from the left that is bigger than pivot element
        if self.step_id == 2:
            print("Step2 pointer1 ist " + str(self.pointer1))
            # if we are not looking at the first element of the sublist, unmark the last item
            if not self.pointer1 == self.active_sublist[0] and not self.pointer1-1 == self.current_pivot: self.problem.list_of_status[self.pointer1-1] = 0
            if self.pointer1-1 == self.current_pivot: self.problem.list_of_status[self.pointer1-2] = 0
            # find the new element and mark it
            self.element1 = self.problem.list_to_sort[self.pointer1]
            self.problem.list_of_status[self.pointer1] = 1
            # if the element is not valid/smaller than the pivot, we need to keep going
            if self.element1 < self.problem.list_to_sort[self.current_pivot]:
                # check if the next element is the pivot, then advance 2 steps
                if self.pointer1 + 1 == self.current_pivot: self.pointer1 += 2
                else: self.pointer1 += 1
                # make sure that we have not reached pointer2, then go to step 6 otherwise set step id such that step 2 is repeated
                if self.pointer1 == self.pointer2: self.step_id = 6
                else: self.step_id = 1
        # step 3: select second element for comparison
        if self.step_id == 3:
            print("Step3 pointer ist " + str(self.pointer2))
            # if we are not looking at the first element of the sublist, unmark the last item
            if not self.pointer2 == self.active_sublist[1] and not self.pointer2 + 1 == self.current_pivot: self.problem.list_of_status[self.pointer2 + 1] = 0
            if self.pointer2 + 1 == self.current_pivot: self.problem.list_of_status[self.pointer2 + 2] = 0
            # find the new element and mark it
            self.element2 = self.problem.list_to_sort[self.pointer2]
            self.problem.list_of_status[self.pointer2] = 2
            # if the element is not valid/bigger than the pivot, we need to keep going
            if self.element2 > self.problem.list_to_sort[self.current_pivot]:
                # check if the next element is the pivot, then advance 2 steps
                if self.pointer2 - 1 == self.current_pivot: self.pointer2 -= 2
                else: self.pointer2 -= 1
                # make sure that we have not reached pointer1, then go to step 6 otherwise set step id such that step 2 is repeated
                if self.pointer1 == self.pointer2:
                    self.step_id = 6
                else:
                    self.step_id = 2
        # step 4: execute swap
        if self.step_id == 4:
            self.problem.list_to_sort[self.pointer1], self.problem.list_to_sort[self.pointer2] = self.problem.list_to_sort[self.pointer2], self.problem.list_to_sort[self.pointer1]
            self.problem.list_of_status[self.pointer1], self.problem.list_of_status[self.pointer2] = self.problem.list_of_status[self.pointer2], self.problem.list_of_status[self.pointer1]
        # step 5: unmark swap and continue with step 2
        if self.step_id == 5:
            self.problem.list_of_status[self.pointer1], self.problem.list_of_status[self.pointer2] = 0, 0
            # check if the next element is the pivot, then advance 2 steps
            if self.pointer2 - 1 == self.current_pivot: self.pointer2 -= 2
            else: self.pointer2 -= 1
            if self.pointer1 == self.pointer2: self.step_id = 6
            if self.pointer1 + 1 == self.current_pivot: self.pointer1 += 2
            else: self.pointer1 += 1
            if self.pointer1 == self.pointer2: self.step_id = 6
            if not self.step_id == 6: self.step_id = 1
        # step 6: if the pointers have met, swap pivot element in and create new sublists
        if self.step_id == 6:
            if self.current_pivot < self.pointer1 and self.problem.list_to_sort[self.pointer1] < self.problem.list_to_sort[self.current_pivot]:
                self.problem.list_to_sort[self.pointer1], self.problem.list_to_sort[self.current_pivot] = self.problem.list_to_sort[self.current_pivot], self.problem.list_to_sort[self.pointer1]
                self.problem.list_of_status[self.pointer1], self.problem.list_of_status[self.current_pivot] = self.problem.list_of_status[self.current_pivot], self.problem.list_of_status[self.pointer1]
            if self.current_pivot < self.pointer1 and self.problem.list_to_sort[self.pointer1] > self.problem.list_to_sort[self.current_pivot]:
                self.problem.list_to_sort[self.pointer1-1], self.problem.list_to_sort[self.current_pivot] = self.problem.list_to_sort[self.current_pivot], self.problem.list_to_sort[self.pointer1-1]
                self.problem.list_of_status[self.pointer1-1], self.problem.list_of_status[self.current_pivot] = self.problem.list_of_status[self.current_pivot], self.problem.list_of_status[self.pointer1-1]

            print("getroffen pointer 1 " +str(self.pointer1) + "und pointer 2 " + str(self.pointer2))
            self.solved = True
        # increment step id, call visualization
        self.step_id = (self.step_id + 1) % 7


        self.application.problem.visualize()


    def run(self):
        self.step()
        if self.solved == True: return
        self.application.after(int(1000//self.speed), self.run)

"""end of class definition"""