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
        self.container.geometry('1920x1080')
        self.container.title("title")
        self.options = options
        self.fonts = {'font': (fonts, size)}
        self.xSize = self.ySize = 100
        self.style = ttk.Style(self)
        self.imported_photos = {}
        self.current_photo_id = 0
        self.showComponents()
        self.sizeMode = False #ctrl ile resim boyutu düzenlenir
        self.pack(fill='both') #tüm pencere kaplanır
        self.after(2000,self.update) #2 saniyede bir güncelleme
        


    def loadPhoto(self, _path,x,y):
        self.image = ImageTk.PhotoImage(Image.open(_path), size=(x,y))

    def update(self):
        
        for key, values in self.imported_photos.items():
            if values == False:
                self.path = ImageTk.PhotoImage(Image.open(key.strip()),size=(300,300))
                self.ImageLabel.configure(image=self.path)

                print('yuklendi',self.path)
                self.imported_photos[key] = True  #içeri aktarılmış fotoğraflar bir sözlükte tutulur key = yol, value = içeri aktarılmış(True) 

        #print('updated')


        self.after(1000, self.update)

    def file_open(self):
        file_path = filedialog.askopenfilename()
        if file_path.split('.')[-1] in ['jpeg','jpg','png']: #desteklenen dosya türleri

            self.imported_photos[file_path] = False #gelen dosya false işaretlenir ancak ekran gözükürse içer aktarılmış sayılır
            print(self.imported_photos)
            self.showOnScreen()
        
        else:
            print('hatali giris')
            self.ext()



    def keypA(self, event): #size modu açık
        self.sizeMode = True


    def keypD(self, event): #size modu kapalı
        self.sizeMode = False


    def showOnScreen(self):

        for key, value in self.imported_photos.items():
            if self.imported_photos[key] is False:
                self.imported_photos[key] = True
                print('ekranda degil')
                self.loadPhoto(key, 300,300)
                
                self.Labelx = ttk.Label(self.container, image=self.image, name='#2')
                self.Labelx.place(x=300,y=300, width=720, height=600)


                #---
                self.Labelx.bind("<Button-1>", self.start_drag)
                self.Labelx.bind("<B1-Motion>", self.drag)
                self.Labelx.bind("<ButtonRelease-1>", self.drop)
                self.container.bind('<KeyPress>', self.keypA)
                self.container.bind('<KeyRelease>', self.keypD)
                #--- #klavye ve mouse baglama isleri labelX için

                print(self.imported_photos)


    def start_drag(self, event):
        self.start_x = event.x
        self.start_y = event.y

        print(f"x {event.x}, y {event.y}")
    
    def drag(self, event):
        x = self.winfo_x() + event.x
        y = self.winfo_y() + event.y
        if self.sizeMode is False:
            self.Labelx.place(x=event.x, y=event.y)
        

    def drop(self, event):
        self.Labelx.place(x=event.x, y=event.y)
        if self.sizeMode:
            self.change(event)
        self.update()


    def change(self, event):
        change_amount_x = event.x - self.start_x
        change_amount_y = event.y - self.start_y 

        self.Labelx.place(width=self.Labelx.winfo_width()-change_amount_x,height=self.Labelx.winfo_height()-change_amount_y)
        print(self.Labelx.winfo_width())
        print(self.Labelx.winfo_height())


    def ext(self):
        self.container.destroy()


    def showComponents(self):

        #self.image = ImageTk.PhotoImage(Image.new('RGB',size=(300,300)))
        #self.ImageLabel = ttk.Label(self,image=self.image, name='#1')
        #self.ImageLabel.place(x=300,y=300)

        self.add_photo_button = ttk.Button(self, text='resim ekle',command=self.file_open)
        self.add_photo_button.pack(anchor='ne', **self.options)

        self.Canv = ttk.Panedwindow(self)
        self.Canv.pack(anchor='s', **self.options)


