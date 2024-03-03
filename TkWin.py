import tkinter as tk
from tkinter import ttk, Tk
from tkinter import font


class BaseWin(Tk):
    def __init__(self):
        super().__init__()
        self.appliedSettings()

    def appliedSettings(self):
        self.title('base')
        self.geometry('600x600')
        self.resizable(120,120) 

class Win_Main(ttk.Frame):

    def __init__(self, container, options={'padx':5,'pady':5}, fonts='Helvetica', size=14, title='Win_Main'):
        super().__init__(container)
        self.container = container
        self.options = options
        self.fonts = {'font': (fonts, size)}
        self.xSize = self.ySize = 100
        self.style = ttk.Style(self)


    def showMainMenu(self):
        ...


