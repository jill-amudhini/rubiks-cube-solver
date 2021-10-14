# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:34:31 2020

@author: Amudhini
"""


import pickle

from cube_position import cubemoves

with open('prune_table.pickle', 'rb') as tbl:
    table = pickle.load(tbl)
    

class solver():
    def __init__(self):
        self.moves=['u','d','l','r','f','b','U','D','L','R','F','B']
        
        self.solution=[]
        self.solstatus=False
        self.curmove=''
        
        self.maxitr=8
        
    def search(self,pos,depth):
        if depth==0:
            if pos=='WWWWWWWWWRRRRRRRRRYYYYYYYYYOOOOOOOOOBBBBBBBBBGGGGGGGGG': #solved state
                if self.curmove!='':
                    self.solution.append(self.curmove)
                    
                self.solstatus=True
            
        elif depth>0:
            for i in range(depth,0,-1):
                if pos in table[i]:
                    if self.curmove!='':
                        self.solution.append(self.curmove)
                
                    for m in self.moves:
                        self.curmove=m
                        p=cubemoves(list(pos))
                        if self.solstatus!=True:
                            self.search(p.movenewpos(m),depth-1)
                        
    def solve(self,scr):
        for d in range(0,self.maxitr):
            self.search(scr,d)
            if self.solstatus==True:
                return self.solution


#s=solver()
#print(s.solve('RRWBWWGGBRRRRROYYOBBGYYOYYGOOROORBBOYGBWBWWBWWWYGGYGGO'))