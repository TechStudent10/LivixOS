from tkinter import *

class Taskbar(Frame):
    def __init__(self, master, bg='black', width=None, height="35", *args, **kwargs):
        super().__init__(master, bg=bg, width=width or master.winfo_screenwidth(), height=height, *args, **kwargs)

        self.master = master
        self.bg = bg
        self.width = width or master.winfo_screenwidth()

        self.pack(side='bottom')