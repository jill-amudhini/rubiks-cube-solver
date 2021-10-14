# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:47:44 2020

@author: Amudhini
"""


class cubemoves():
    def __init__(self,c):
        self.moves=[];
        self.cube=c;
    
    def returncubestring(self):
        return ''.join(self.cube)
        
    def move_r(self):
        cube=self.cube
        d=[cube[2],cube[5],cube[8]]
        for i in range(3):
            cube[2+i*9]=cube[2+(i+1)*9]
            cube[5+i*9]=cube[5+(i+1)*9]
            cube[8+i*9]=cube[8+(i+1)*9]
        cube[29]=d[0]
        cube[32]=d[1]
        cube[35]=d[2]
    
        d=[cube[36],cube[37],cube[38]]
        cube[36]=cube[42];cube[37]=cube[39];cube[38]=d[0]
        cube[39]=cube[43];cube[42]=cube[44]
        cube[43]=cube[41];cube[44]=d[2]
        cube[41]=d[1]
        
        self.cube=cube
        

    def move_l(self):
        cube=self.cube
        d=[cube[27],cube[30],cube[33]]
        for i in range(3,0,-1):
            cube[0+i*9]=cube[0+(i-1)*9]
            cube[3+i*9]=cube[3+(i-1)*9]
            cube[6+i*9]=cube[6+(i-1)*9]
        cube[0]=d[0]
        cube[3]=d[1]
        cube[6]=d[2]
        
        d=[cube[45],cube[46],cube[47]]
        cube[45]=cube[51];cube[46]=cube[48];cube[47]=d[0]
        cube[48]=cube[52];cube[51]=cube[53]
        cube[52]=cube[50];cube[53]=d[2]
        cube[50]=d[1]
        
        self.cube=cube
    
    
    def move_u(self):
        cube=self.cube
        d=[cube[9],cube[10],cube[11]]
        cube[9]=cube[36]; cube[10]=cube[37]; cube[11]=cube[38];
        cube[36]=cube[35]; cube[37]=cube[34]; cube[38]=cube[33];
        cube[35]=cube[45]; cube[34]=cube[46]; cube[33]=cube[47];
        cube[45]=d[0]; cube[46]=d[1]; cube[47]=d[2];
        
        d=[cube[0],cube[1],cube[2]]
        cube[0]=cube[6];cube[1]=cube[3];cube[2]=d[0]
        cube[3]=cube[7];cube[6]=cube[8]
        cube[7]=cube[5];cube[8]=d[2]
        cube[5]=d[1]
        
        self.cube=cube
        
    
    def move_d(self):
        cube=self.cube
        d=[cube[15],cube[16],cube[17]]
        cube[15]=cube[51]; cube[16]=cube[52]; cube[17]=cube[53];
        cube[51]=cube[29]; cube[52]=cube[28]; cube[53]=cube[27];
        cube[29]=cube[42]; cube[28]=cube[43]; cube[27]=cube[44];
        cube[42]=d[0]; cube[43]=d[1]; cube[44]=d[2];
        
        d=[cube[18],cube[19],cube[20]]
        cube[18]=cube[24];cube[19]=cube[21];cube[20]=d[0]
        cube[21]=cube[25];cube[24]=cube[26]
        cube[25]=cube[23];cube[26]=d[2]
        cube[23]=d[1]
        self.cube=cube
        
    
    def move_f(self):
        cube=self.cube
        d=[cube[53],cube[50],cube[47]]
        cube[53]=cube[20]; cube[50]=cube[19]; cube[47]=cube[18];
        cube[20]=cube[36]; cube[19]=cube[39]; cube[18]=cube[42];
        cube[36]=cube[6]; cube[39]=cube[7]; cube[42]=cube[8];
        cube[6]=d[0]; cube[7]=d[1]; cube[8]=d[2];
    
        d=[cube[9],cube[10],cube[11]]
        cube[9]=cube[15]; cube[10]=cube[12]; cube[11]=d[0]
        cube[15]=cube[17];cube[12]=cube[16]
        cube[16]=cube[14];cube[17]=d[2]
        cube[14]=d[1]
        
        self.cube=cube
        

    def move_b(self):
        cube=self.cube
        d=[cube[2],cube[1],cube[0]]
        cube[2]=cube[44]; cube[1]=cube[41]; cube[0]=cube[38];
        cube[44]=cube[24]; cube[41]=cube[25]; cube[38]=cube[26];
        cube[24]=cube[45]; cube[25]=cube[48]; cube[26]=cube[51];
        cube[45]=d[0]; cube[48]=d[1]; cube[51]=d[2];
    
        d=[cube[35],cube[34],cube[33]]
        cube[35]=cube[29];cube[34]=cube[32];cube[33]=d[0]
        cube[29]=cube[27];cube[32]=cube[28]
        cube[28]=cube[30];cube[27]=d[2]
        cube[30]=d[1]
        
        self.cube=cube


    def move_rp(self):
        self.move_r()
        self.move_r()
        self.move_r()
    
    def move_lp(self):
        self.move_l()
        self.move_l()
        self.move_l()
    
    def move_up(self):
        self.move_u()
        self.move_u()
        self.move_u()

    def move_dp(self):
        self.move_d()
        self.move_d()
        self.move_d()
    
    def move_fp(self):
        self.move_f()
        self.move_f()
        self.move_f()
    
    def move_bp(self):
        self.move_b()
        self.move_b()
        self.move_b()
    
    def movenewpos(self,m):
        if m=='u':
            self.move_up()
        elif m=='d':
            self.move_dp()
        elif m=='l':
            self.move_lp()
        elif m=='r':
            self.move_rp()
        elif m=='f':
            self.move_fp()
        elif m=='b':
            self.move_bp()
        elif m=='U':
            self.move_u()
        elif m=='D':
            self.move_d()
        elif m=='L':
            self.move_l()
        elif m=='R':
            self.move_r()
        elif m=='F':
            self.move_f()
        elif m=='B':
            self.move_b()
        
        return ''.join(self.cube)

    def printcube(self):
        for i in range(4):
            if i!=1:
                for j in range(3):
                    print('     ',' '.join(self.cube[i*9+j*3:i*9+j*3+3]))
            else:
                for j in range(3):
                    print(' '.join(self.cube[45+j*3:48+j*3]),' '.join(self.cube[9+j*3:12+j*3]),' '.join(self.cube[36+j*3:39+j*3]))
                    
                   
                    
c=['W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R',
      'Y','Y','Y','Y','Y','Y','Y','Y','Y','O','O','O','O','O','O','O','O','O',
      'B','B','B','B','B','B','B','B','B','G','G','G','G','G','G','G','G','G']
'''

c=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',
   '21','22','23','24','25','26','27','28','29','30','31','32','33',
   '34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54']'''

#a=cubemoves(c)
#a.printcube()
#print(a.returncubestring())