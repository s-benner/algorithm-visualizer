pass
"""Algorithm Visualizer"""
"""--------------------"""


"""INTRO"""
"""
This tool is a private and recreational software development project of mine, that serves 3 main purposes:

1. The overall goal is to create an application, that allows the user to interactively explore different basic algorithms by making it
   possible for the user to interact with the software in creating the problems to be solved and by visualizing how the algorthms solve
   the problems.
   I want any user of this program to find joy in using it and also take away algorithm knowledge. I am trying to visualize the algorithms
   in such a way that it is very instructive, while not spending too much effort on design, since I am no designer.
2. To reach this goal I am creating an application, that has a good underlying design. I am not a professional software engineer, so I am
   trying to teach myself something about application design in the process. The goal is to show, that I can develop an application that can
   be modified and expanded in a methodological way, which will definitely be useful for further projects.
3. By implementing this I am hoping to also improve my understanding of algorithms and data structures. I will try to all the algorithms and
   also the advanced data structures by myself. This is likely more effort than necessary, but the goal here is to teach myself something 
"""

"""DESIGN"""
"""
The application has a 3-layer design.

The top level contains the user interface created with tkinter. Also the limited menu is located here. This level is basically only the framework
and is not specific to the algorithm visualizer. So everything that belongs to the first layer could be reused for other applications. The first
layer should need to changes if new second or third level classes are to be added except listing the new functionality in the config file.

The second level consists of data structure classes for the different problem types. These classes contain the data structures itself including
functions that visualize the data structure on the screen. It is important for these classes to be designed in such a way, that additional
third level classes (new algorithms) can be added without modifications to the second level.

The third level consists of the algorithm classes. They do the actual algorithmic calculations either step by step or in one go and manipulate
the second level data structure object in such a way, that the algorithm progress is visualized properly. 
"""

"""LEVEL 1 DESIGN"""