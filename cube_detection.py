# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 02:13:55 2020

@author: Amudhini
"""


import numpy as np 
import cv2 

import json

class cubedetect():
    def __init__(self):
        self.webcam=cv2.VideoCapture(0)
        
        
        self.mainbox=[[100, 120], [200, 120], [300, 120], 
                      [100, 220], [200, 220], [300, 220],
                      [100, 320], [200, 320], [300, 320]]
        
        self.sidebox=[[470, 30], [504, 30], [538, 30],
                      [470, 64], [504, 64], [538, 64],
                      [470, 98], [504, 98], [538, 98]]
        self.rgbvalues={
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
            }
        
    
        '''
                           [Yellow]
                           [Orange]
                [Green]    [White]    [Blue]
                            [Red]
        '''
        
        self.sides={
            'orange':[[478, 172], [502, 172], [526, 172],
                      [478, 196], [502, 196], [526, 196],
                      [478, 220], [502, 220], [526, 220]] ,
            
            'white':[[478, 247], [502, 247], [526, 247],
                      [478, 271], [502, 271], [526, 271],
                      [478, 295], [502, 295], [526, 295]] ,
            
            'red':[[478, 322], [502, 322], [526, 322],
                     [478, 346], [502, 346], [526, 346],
                     [478, 370], [502, 370], [526, 370]] ,
            
            'green': [[403, 322], [427, 322], [451, 322],
                     [403, 346], [427, 346], [451, 346],
                     [403, 370], [427, 370], [451, 370]] ,
            
            'blue': [[553, 322], [577, 322], [601, 322],
                     [553, 346], [577, 346], [601, 346],
                     [553, 370], [577, 370], [601, 370]] , 
            
            'yellow':[[478, 397], [502, 397], [526, 397],
                   [478, 421], [502, 421], [526, 421],
                   [478, 445], [502, 445], [526, 445]]
            
            }
        
        self.sidecolors=['white', 'white', 'white',
                         'white', 'white', 'white',
                         'white', 'white', 'white']
        
        self.cubecolors={
            'yellow':['yellow', 'yellow', 'yellow',
                      'yellow', 'yellow', 'yellow',
                      'yellow', 'yellow', 'yellow'] ,
            
            'orange':['orange', 'orange', 'orange',
                      'orange', 'orange', 'orange',
                      'orange', 'orange', 'orange'] ,
            
            'white':['white', 'white', 'white',
                     'white', 'white', 'white',
                     'white', 'white', 'white'] ,
            
            'green': ['green', 'green', 'green',
                      'green', 'green', 'green',
                      'green', 'green', 'green'] ,
            
            'blue': ['blue', 'blue', 'blue',
                     'blue', 'blue', 'blue',
                     'blue', 'blue', 'blue'] , 
            
            'red':['red', 'red', 'red',
                   'red', 'red', 'red',
                   'red', 'red', 'red']
            }
        
        
        
    def draw_boxes(self):
        for x,y in self.mainbox:
            cv2.rectangle(self.imageFrame, (x,y), (x+30, y+30), (255,255,255), 2)
    
        for index,(x,y) in enumerate(self.sidebox):
            cv2.rectangle(self.imageFrame, (x,y), (x+30, y+30), self.rgbvalues[self.sidecolors[index]], -1)
                        
        for i in self.sides:
            for index,(x,y) in enumerate(self.sides[i]):
                cv2.rectangle(self.imageFrame, (x,y), (x+20, y+20), self.rgbvalues[self.cubecolors[i][index]], -1)
        
    def colorrange(self,h):
        with open("hsvvalues.json", "r") as read_file:
            hsv = json.load(read_file)
        if h>115 and h<125:
            return 'red'
        elif h>50 and h<65:
            return 'white'
        elif h>15 and h<25:
            return 'yellow'
        elif h>0 and h<15:
            return 'orange'
        elif h>70 and h<80:
            return 'blue'
        elif h>35 and h<45:
            return 'green'
    
        
    def detectcolor(self):
        hsv = cv2.cvtColor(self.imageFrame, cv2.COLOR_BGR2HSV)
        
        for index,(x,y) in enumerate(self.mainbox):
            roi= hsv[y:y+32, x:x+32]
            avg_hsv= roi.mean(axis=(1,0))
            color_name= self.colorrange(avg_hsv[0])
            if color_name!=None:
                self.sidecolors[index]= color_name
    
    def returncubestring(self):
        order=['white','red','yellow','orange','blue','green']
        s=''
        for i in order:
            for j in self.cubecolors[i]:
                s+=j[0].upper()
                
        return s
            
    
    def video(self):
        while(True): 
            # Capture the video frame by frame 
            _, self.imageFrame = self.webcam.read()
            key = cv2.waitKey(10) & 0xff
            self.draw_boxes()
            
            self.detectcolor()
            
            cv2.putText(self.imageFrame, 'Scan Cube', (70,70), cv2.FONT_HERSHEY_TRIPLEX,  
                   2, (255,255,255), 3, cv2.LINE_AA)
            
            if key == 32:
                c=self.sidecolors[4]
                for i in range(9):
                    self.cubecolors[c][i]=self.sidecolors[i]
            
            # Display the resulting frame 
            cv2.imshow('frame', self.imageFrame) 
      
            # 'q' button is set as the quitting button 
            if key == ord('q'): 
                break
        
        # After the loop release the cap object and destroy all the windows 
        self.webcam.release() 
        cv2.destroyAllWindows()     
    

#recog=cubedetect()
#recog.video()
#print(recog.returncubestring())