from os import path
import tkinter as tk
from tkinter import ttk, Tk, filedialog
from tkinter import font
from PIL import Image, ImageTk

class BaseWin(Tk):
    def __init__(self):
        super().__init__()
        self.appliedSettings()

    def appliedSettings(self):
        self.title('base')
        self.geometry('600x600')
        self.resizable(600,600) 

class Win_Main(ttk.Frame):

    def __init__(self, container, options={'padx':5,'pady':5}, fonts='Helvetica', size=14):
        super().__init__(container)
        self.container = container
        self.options = options
        self.fonts = {'font': (fonts, size)}
        self.xSize = self.ySize = 100
        self.style = ttk.Style(self)
        self.imported_photos = {}
        self.current_photo_id = 0
        self.showComponents()
        self.pack(fill='both')
        self.after(1000,self.update)

    def update(self):
        
        for key, values in self.imported_photos.items():
            if values == False:
                self.path = ImageTk.PhotoImage(Image.open(key.strip()),size=(300,300))
                self.ImageLabel.configure(image=self.path)

                print('yuklendi',self.path)
                self.imported_photos[key] = True

        print('updated')
        self.after(1000, self.update)

    def file_open(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.imported_photos[file_path] = False

    def showComponents(self):

        self.image = ImageTk.PhotoImage(Image.new('RGB',size=(300,300)))
        self.ImageLabel = ttk.Label(self, width=300,image=self.image)
        self.ImageLabel.pack(anchor='center', **self.options)

        self.add_photo_button = ttk.Button(self, text='resim ekle', command=self.file_open)
        self.add_photo_button.pack(anchor='ne', **self.options)


