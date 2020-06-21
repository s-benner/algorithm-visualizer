import sortingProblem

WINDOW_TITLE = "Algorithm Visualizer"

APPLICATION_WIDTH = 1200
TITLE_HEIGHT = 40
MENU_HEIGHT = 40
APPLICATION_HEIGHT = 620
LOG_WIDTH = 250
LOG_LABEL_WIDTH = 18
DROPDOWNMENU_WIDTH = 25
CANVAS_WIDTH = 920
CANVAS_HEIGHT = 540

ALGO_TYPES = []
ALGO_TYPES.append("")
ALGO_TYPES.append("Graph algorithms")
ALGO_TYPES.append("Sorting algorithms")
ALGO_TYPES.append("Sampling algorithms")
ALGO_TYPES.append("Pathfinding algorithms")

ALGO_PROBLEM_CLASSES = []
ALGO_PROBLEM_CLASSES.append(None)
ALGO_PROBLEM_CLASSES.append(None)
ALGO_PROBLEM_CLASSES.append(sortingProblem.SortingProblem)
ALGO_PROBLEM_CLASSES.append(None)
ALGO_PROBLEM_CLASSES.append(None)

ALGO_SOLVER_CLASSES = []
ALGO_SOLVER_CLASSES.append(None)
ALGO_SOLVER_CLASSES.append(None)
ALGO_SOLVER_CLASSES.append([None, sortingProblem.BubbleSolver, sortingProblem.QuickSolver])
ALGO_SOLVER_CLASSES.append(None)
ALGO_SOLVER_CLASSES.append(None)

ALGO_SOLVER_CLASSES.append
ALGO_NAMES = []
ALGO_NAMES.append([""])
ALGO_NAMES.append(["","Spanning Tree"])
ALGO_NAMES.append(["","Bubble Sort","Quick Sort"])
ALGO_NAMES.append([""])
ALGO_NAMES.append([""])

COLOR_BG1 = "gray32"
COLOR_BG2 = "gray75"
COLOR_BG3 = "gray91"
COLOR_TEXT1 = "light goldenrod"

ANIM_COLORS = []
ANIM_COLORS.append("RoyalBlue1")
ANIM_COLORS.append("RosyBrown2")
ANIM_COLORS.append("CadetBlue1")
ANIM_COLORS.append("NavajoWhite2")
ANIM_COLORS.append("PaleGreen1")
ANIM_COLORS.append("plum1")
ANIM_COLORS.append("bisque2")
ANIM_COLORS.append("lavender")
