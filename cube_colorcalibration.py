# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:17:46 2020

@author: Amudhini
"""


import numpy as np 
import cv2 
import json


class cubecalibrate():
    def __init__(self):
        self.webcam=cv2.VideoCapture(0)
        self.mainbox=[[170, 220]]
        
        self.colorbox=[[400, 120], [400, 170], [400, 220],
                      [400, 270], [400, 320], [400, 370]]
        
        self.rgbvalues={
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
            }
        
        self.cubevalues={
            'red'    : (0,0,255),
            'orange' : (0,165,255),
            'blue'   : (255,0,0),
            'green'  : (0,255,0),
            'white'  : (255,255,255),
            'yellow' : (0,255,255)
            }
        
        self.hsvvalues={
            'red'    : [155.3679012345679, 107.40592592592593, 171.70271604938273],
            'orange' : [5.545185185185185, 133.27012345679012, 184.3041975308642],
            'blue'   : [93.6953086419753, 231.30617283950616, 165.7274074074074],
            'green'  : [53.88987654320988, 115.29876543209876, 145.60987654320988],
            'white'  : [89.39506172839506, 27.37925925925926, 209.278024691358],
            'yellow' : [25.52, 147.01086419753085, 201.13975308641974]
            }
        
    
        '''
                           [Yellow]
                           [Orange]
                [Green]    [White]    [Blue]
                            [Red]
        '''
        
        
        self.cubecolors=['white', 'red', 'green',
                         'orange', 'blue', 'yellow']
        
        
        self.sentences=["Press space to start","Show white","Show red","Show green",
                        "Show orange","Show blue","Show yellow"]
        self.count=0
        
    def draw_boxes(self):
        for x,y in self.mainbox:
            cv2.rectangle(self.imageFrame, (x,y), (x+50, y+50), (255,255,255), 2)
    
        for index,(x,y) in enumerate(self.colorbox):
            cv2.rectangle(self.imageFrame, (x,y), (x+40, y+40), self.cubevalues[self.cubecolors[index]], -1)
            cv2.putText(self.imageFrame, self.cubecolors[index], (x+50,y+30), cv2.FONT_HERSHEY_TRIPLEX,  
                   0.75, self.rgbvalues[self.cubecolors[index]], 1, cv2.LINE_AA)
                        
        
        
    def detectcolor(self):
        hsv = cv2.cvtColor(self.imageFrame, cv2.COLOR_BGR2HSV)
        
        for index,(x,y) in enumerate(self.mainbox):
            roi= hsv[y:y+45, x:x+45]
            avg_hsv= roi.mean(axis=(1,0))
            rgb=cv2.cvtColor(roi, cv2.COLOR_HSV2BGR)
            avg_rgb=rgb.mean(axis=(1,0))
            #print(avg_hsv)
            #print(avg_rgb)
            
            if self.count>0 and self.count<7:
                self.cubevalues[self.cubecolors[self.count-1]]=tuple(avg_rgb)
                self.hsvvalues[self.cubecolors[self.count-1]]=list(avg_hsv)
    
    
    def video(self):
        
        while(True): 
            # Capture the video frame by frame 
            _, self.imageFrame = self.webcam.read()
            key = cv2.waitKey(10) & 0xff
            
            cv2.putText(self.imageFrame, 'Color Calibration', (50,70), cv2.FONT_HERSHEY_TRIPLEX,  
                   1.5, (255,255,255), 3, cv2.LINE_AA)
            
            cv2.putText(self.imageFrame, self.sentences[self.count], (90,150), cv2.FONT_HERSHEY_TRIPLEX,  
                   0.75, (255,255,255), 1, cv2.LINE_AA)
            
            self.draw_boxes()
            
            self.detectcolor()
            
            if key == 32:
                self.count+=1
                if self.count>6:
                    break
            
            
            # Display the resulting frame 
            cv2.imshow('Color Calibration', self.imageFrame) 
      
            # 'q' button is set as the quitting button 
            if key == ord('q'): 
                break
        
        # After the loop release the cap object and destroy all the windows 
        self.webcam.release() 
        cv2.destroyAllWindows() 
        print(self.hsvvalues)
        with open("hsvvalues.json", "w") as write_file:
            json.dump(self.hsvvalues, write_file)
    

#recog=cubecalibrate()
#recog.video()