from tkinter import Tk, BOTH, Canvas, Label

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__root.title("Maze Solver, by Babycake")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack()

        self.run = False

    def redraw(self):
       self.__root.update_idletasks()
       self.__root.update()

    def wait_for_close(self):
        self.run = True
        while self.run:
            self.redraw()

    def close(self):
        self.run = False