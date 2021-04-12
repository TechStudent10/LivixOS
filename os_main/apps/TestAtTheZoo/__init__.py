from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()

        Label(self, text="Hi").pack()