from tkinter import *
from .internals import *
import os
import importlib

class MainOS(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.app_path = os.path.join('os_main', 'apps')

        self.wm_attributes('-fullscreen', True)
        self.config(bg="orange")

        self.taskbar = Taskbar(self)
        self.taskbar.pack(side='bottom')

        self.run_app("TestAtTheZoo")

    def run_app(self, name):
        if name in self.get_app_names():
            app_module = importlib.import_module(f'os_main.apps.{name}')
            app = app_module.App()
            app.wm_attributes('-topmost', 1)
            app.mainloop()

    def get_app_names(self):
        return os.listdir(self.app_path)
