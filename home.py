from tkinter import*
#from tkinter.ttk import * 
import tkinter.font as font
from PIL import ImageTk,Image
import time
import os

from cube_detection import cubedetect
from cube_solve import solver
from cube_colorcalibration import cubecalibrate
import pygame_cube as pc


GUI_BG2='white'

class slider:
    def __init__(self,root):
        self.root=root
        self.root.title("RubiksCube")
        self.root.geometry("1350x700+0+0")

        self.root.configure(background=GUI_BG2)
        self.image1=ImageTk.PhotoImage(file="homepage.png")
        
        Frame_slider=Frame(self.root)
        Frame_slider.place(x=150,y=50,width=1500,height=800)
        
        self.lbl1=Label(Frame_slider,image=self.image1)
        self.lbl1.place(x=0,y=0)
        
        self.x=1100
        
        self.myFont = font.Font(family='Courier new', size=40,weight='bold')
        self.wButton=Button(self.root, text="Scan Cube",height=2,width=10,bg="blue",command=self.solvescan)
        self.wButton['font'] = self.myFont
        self.wButton.place(x=843, y=183)

        self.myFont1 = font.Font(family='Courier New', size=40,weight='bold')
        self.cButton = Button(self.root, text="Calibrate",height=2,width=9,bg="green",command=self.calibrate)
        self.cButton['font'] = self.myFont1
        self.cButton.place(x=1173, y=336)
        
        self.myFont2 = font.Font(family='Courier New', size=40,weight='bold')
        self.rButton = Button(self.root, text="Scramble Cube",height=2,width=14,bg="yellow",command=self.solvescramblecube)
        self.rButton['font'] = self.myFont2
        self.rButton.place(x=420, y=480)
        
        
    def solvescan(self):
        recog=cubedetect()
        recog.video()
        scramble=recog.returncubestring()
        
        s=solver()
        sol=s.solve(scramble)
        self.solution(sol)
        
        pc.playsolution(sol)
    
    def calibrate(self):
        recog=cubecalibrate()
        recog.video()
        
    def solvescramblecube(self):
        scramble=pc.scramblecube()
        
        s=solver()
        sol=s.solve(scramble)
        
        self.solution(sol)
        
        pc.playsolution(sol)
        
        
        
    
    def solution(self,l):
        gui= Tk()
        t=Text(gui)
        GUI_BG2='pink'

        gui.configure(background=GUI_BG2)
        gui.title("SOLUTION")
        gui.geometry("430x150")
        st=''
        move={'u':"U'",'d':"D'",'f':"F'",'b':"B'",'l':"L'",'r':"R'"}
        for i in l:
            if i.islower():
                st+=move[i]+', '
            else:
                st+=i+', '
        
        st=st[:len(st)-2]
        la1=Label(gui, text="Scramble solution:-",bg=GUI_BG2, font=('', 25))
    
        la1.config(anchor=CENTER)
        la1.pack()
        
        la2=Label(gui, text=st,bg=GUI_BG2, font=('', 30))
    
        la2.config(anchor=CENTER)
        la2.pack()
        
        
        
        
    
    def slider_func(self):
        
        self.x-=1
        if self.x==0:
            self.x=1100
            time.sleep(1)
           
    
root=Tk()
obj=slider(root)
root.mainloop()
        