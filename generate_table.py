# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 01:12:19 2020

@author: Amudhini
"""


import pickle

from cube_position import cubemoves


cube=['W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R',
      'Y','Y','Y','Y','Y','Y','Y','Y','Y','O','O','O','O','O','O','O','O','O',
      'B','B','B','B','B','B','B','B','B','G','G','G','G','G','G','G','G','G']
table={}
moves=['u','d','l','r','f','b','U','D','L','R','F','B']

table[0]=[''.join(cube)]

allpos=[''.join(cube)]



def newdepth(level):
    table[level]=[]
    
    for p in table[level-1]:
        for m in moves:
            pos=cubemoves(list(p))
            newpos=pos.movenewpos(m)
            
            if(newpos not in allpos):
                table[level].append(newpos)
                allpos.append(newpos)
                
                print(level,m,newpos)
                
                
for i in range(1,7):
    newdepth(i)
    
with open('prune_table.pickle', 'wb') as db:
    pickle.dump(table, db, protocol=pickle.HIGHEST_PROTOCOL)