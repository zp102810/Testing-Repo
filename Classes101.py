#ppa = points per axis
import tkinter as tk
import matplotlib
class Graph:
    def __init__(self,type,minx,maxx,miny,maxy,ppa):
        pass

class EnterBox:
    def __init__(self,window,relx,rely,relwidth,relheight):
        self.window=window
        self.relwidth=relwidth
        self.relheight=relheight
        self.relx=relx
        self.rely=rely
    def construct(self):
        self.InputBox = tk.Entry(self.window)
        self.InputBox.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.relwidth,
            relheight=self.relheight,
            anchor="center"
        )
        def enter_pressed(event):
            if self.InputBox.get() == type(str):
                Warning("Wrong data type!")
            print("You entered " + self.InputBox.get())
        self.InputBox.bind("<Return>",enter_pressed)

class InvisTextLabel:
    Transparent_Color = "white"
    def __init__(self,window,relx,rely,relwidth,relheight,text):
        self.window=window
        self.text=text
        self.relx=relx
        self.rely=rely
        self.relwidth=relwidth
        self.relheight=relheight

    def construct(self):
        self.Label = tk.Label(self.window)
        self.Label.config(text=self.text)
        self.Label.config(bg="#444444")
        self.Label.config(fg="#ffffff")
        self.Label.place(
            relx=self.relx,
            rely=self.rely,
            relwidth=self.relwidth,
            relheight=self.relheight,
            anchor="center"
        )