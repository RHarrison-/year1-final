from tkinter import *
import random
import tkinter.filedialog as tkfd

class surface():
    def __init__(self):
        self.window = Tk()
        self.canvas = ''
        self.canvas_Tiles = ''
        self.TType = '1'
        self.TNum = '1'
        self.x = 120
        self.y = 75
        self.TileWindow = {}
        self.MapData = {}
        self.MapExport = []
        self.MapName = ''
        self.rotation = 0
        self.screenlocation = (0,0)
        
        self.stoneimage = PhotoImage(file = 'assets\Stone.png')
        self.grassimage1 = PhotoImage(file = 'assets\Grass1.png')
        self.grassimage2 = PhotoImage(file = 'assets\Grass2.png')
        self.waterimage1 = PhotoImage(file = 'assets\Water1.png')
        self.waterimage2 = PhotoImage(file = 'assets\Water2.png')
        self.flowerimage = PhotoImage(file = 'assets\Flower.png')
        self.stumpimage = [[PhotoImage(file = 'assets\TLStump.png'),
                           PhotoImage(file = 'assets\BLStump.png')],
                           [PhotoImage(file = 'assets\TRStump.png'),
                           PhotoImage(file = 'assets\BRStump.png')]]
        self.I1 = PhotoImage(file = 'assets\GrassCliffN.png') #a
        self.i1 = PhotoImage(file = 'assets\TopCliffN.png')#b
        self.I2 = PhotoImage(file = 'assets\TopCliffN.png')#c
        self.I3 = PhotoImage(file = 'assets\WaterCliffN.png')#d
        self.I4 = PhotoImage(file = 'assets\WaterN.png')#e
        self.I5 = PhotoImage(file = 'assets\GrassCliffNE.png')#f
        self.I6 = PhotoImage(file = 'assets\TopCliffNE.png')#g
        self.I7 = PhotoImage(file = 'assets\MiddleCliffNE.png')#h
        self.I8 = PhotoImage(file = 'assets\WaterCliffNE.png')#i
        self.I9 = PhotoImage(file = 'assets\WaterCLiffNtoNE.png')#j
        self.I10 = PhotoImage(file = 'assets\WaterNE.png')#k
        self.I11 = PhotoImage(file = 'assets\WaterOuterNE.png')#l
        self.I12 = PhotoImage(file = 'assets\WaterOuterNE2.png')#m
        self.I13 = PhotoImage(file = 'assets\TopCliffE.png')#n
        self.I14 = PhotoImage(file = 'assets\BottomCliffE.png')#o
        self.I15 = PhotoImage(file = 'assets\WaterCliffE.png')#p
        self.I16 = PhotoImage(file = 'assets\TopCliffNW.png')#q
        self.I17 = PhotoImage(file = 'assets\CliffMiddleNW.png')#r
        self.I18 = PhotoImage(file = 'assets\CliffBottomNW.png')#s
        self.I19 = PhotoImage(file = 'assets\CliffGrassNW.png')#t
        self.I20 = PhotoImage(file = 'assets\WaterCliffNW.png') #u       
        self.I21 = PhotoImage(file = 'assets\CliffTopW.png')#v
        self.I22 = PhotoImage(file = 'assets\MiddleCliffW.png')#w
        self.I23 = PhotoImage(file = 'assets\WaterW.png')#x
        self.I24 = PhotoImage(file = 'assets\GrassCliffSW.png')#y
        self.I25 = PhotoImage(file = 'assets\TopCliffSW.png')  #z
        self.I26 = PhotoImage(file = 'assets\GrassSW.png')      #A
        self.I27 = PhotoImage(file = 'assets\BottomCliffSW.png') #B
        self.I28 = PhotoImage(file = 'assets\WaterSW.png') #C
        self.I29 = PhotoImage(file = 'assets\WaterCornerSW.png') #D
        self.I30 = PhotoImage(file = 'assets\GrassCliffS.png')#E
        self.I31 = PhotoImage(file = 'assets\TopCliffS.png') #F
        self.I32 = PhotoImage(file = 'assets\MiddleCliffS.png')#G
        self.I33 = PhotoImage(file = 'assets\BottomCliffS.png')#H
        self.I34 = PhotoImage(file = 'assets\WaterS.png')#I
        self.I35 = PhotoImage(file = 'assets\GrassSE.png')#J
        self.I36 = PhotoImage(file = 'assets\GrassCliffSE.png')#K
        self.I37 = PhotoImage(file = 'assets\TopCliffSE.png')#L
        self.I38 = PhotoImage(file = 'assets\BottomCliffSE.png')#M
        self.I39 = PhotoImage(file = 'assets\WaterCliffSE.png')#N
        self.I40 = PhotoImage(file = 'assets\CornerWaterSE.png')#O
        self.I41 = PhotoImage(file = 'assets\Tree1.png')#O
        self.I42 = PhotoImage(file = 'assets\Tree2.png')#P
        self.I43 = PhotoImage(file = 'assets\Tree3.png')#Q
        self.I44 = PhotoImage(file = 'assets\Tree4.png')#R
        self.I45 = PhotoImage(file = 'assets\Tree5.png')#S
        self.I46 = PhotoImage(file = 'assets\Tree6.png')#T
        self.I47 = PhotoImage(file = 'assets\Tree7.png')#U
        self.I48 = PhotoImage(file = 'assets\Tree8.png')#V
        self.I49 = PhotoImage(file = 'assets\Tree9.png')#W
        self.I50 = PhotoImage(file = 'assets\Tree10.png')#X
        self.I51 = PhotoImage(file = 'assets\Tree11.png')#Y
        self.I52 = PhotoImage(file = 'assets\Tree12.png')#Z
        self.I53 = PhotoImage(file = 'assets\Tree13.png')#!
        self.I54 = PhotoImage(file = 'assets\Tree14.png')#"
        self.I55 = PhotoImage(file = 'assets\Tree15.png')#£
        self.I56 = PhotoImage(file = 'assets\Tree16.png')#$
        self.I57 = PhotoImage(file = 'assets\Tree17.png')#%
        self.I58 = PhotoImage(file = 'assets\Tree18.png')#^
        self.I59 = PhotoImage(file = 'assets\Tree19.png')#&
        self.I60 = PhotoImage(file = 'assets\Tree20.png')#*
        self.I61 = PhotoImage(file = 'assets\HorozontalFence.png')#(
        self.I62 = PhotoImage(file = 'assets\VerticleFenceLeft.png')#)
        self.I63 = PhotoImage(file = 'assets\VerticleFenceRight.png')#-
        self.I64 = PhotoImage(file = 'assets\BottomGrassCliff.png')#_
        self.I65 = PhotoImage(file = 'assets\GrassGrassCliffSW.png')#=
        self.I66 = PhotoImage(file = 'assets\GrassGrassCliffSE.png')#+
        self.I67 = PhotoImage(file = 'assets\StepsLeft.png')#[
        self.I68 = PhotoImage(file = 'assets\StepsRight.png')#{
        self.I69 = PhotoImage(file = 'assets\Path.png')#~
        self.I70 = PhotoImage(file = 'assets\PinkFlower.png')#,
        self.I71 = PhotoImage(file = 'assets\HorizontalPath1.png')#~
        self.I72 = PhotoImage(file = 'assets\HorizontalPath2.png')#,
        self.I73 = PhotoImage(file = 'assets\ZeldaCage.png')#>
        self.I74 = PhotoImage(file = 'assets\Key.png')#/
        
    def openfile(self):
        
        filename = tkfd.askopenfilename()

        self.create()
         
        y=-1
        
        with open(filename,'r') as f:
            for line in f:
                y += 1
                x=-1
                for character in line:
                    x += 1
                    self.MapData[(x,y)] = character
                    self.width = len(line)
                    self.height = y

        p = self.screenlocation[0] 
        r = self.screenlocation[1]
        
        for s in range (0,self.x):
            for q in range (0,self.y):
                if ( p+s,r+q) in self.MapData: self.drawtile((s,q),self.MapData[( p+s,r+q)],self.canvas)

                         
    def movecamera(self,direction):
        self.canvas.delete(ALL)
        moveam = 0
        if direction == 'right': movam = (40,0)
        if direction == 'left': movam = (-40,0)
        if direction == 'up': movam = (0,-25)
        if direction == 'down': movam = (0,25)

        self.screenlocation = (addcords(self.screenlocation,movam))

        p = self.screenlocation[0] 
        r = self.screenlocation[1]
        
        for s in range (0,40):
            for q in range (0,25):
                if ( p+s,r+q) in self.MapData: self.drawtile((s,q),self.MapData[( p+s,r+q)],self.canvas)
 
        print(self.screenlocation)

    def savemap(self):
        self.MapExport.clear()
        
        for x in range (0,self.y):
            for y in range (0,self.x):
                self.MapExport.append(self.MapData[(y,x)])

        self.MapName = tkfd.asksaveasfile(mode = 'w', defaultextension=".txt")
        
        if self.MapName is None:
            return #stops trying to save the map if user presses cancel
        
        p = 0
        for item in self.MapExport:
            p+=1
            if p == self.x:
                self.MapName.write(str(item) + '\n')
                p = 0
            else:
               self.MapName.write(str(item))
               
    def drawgrid(self):
        
        p = self.screenlocation[0] 
        r = self.screenlocation[1] 

        for s in range (0,40):
            for q in range (0,25):
                if ( p+s,r+q) in self.MapData: self.drawtile((s,q),self.MapData[( p+s,r+q)],self.canvas)

    def drawtile(self,gridid,TType,canvas):
        
        x,y = gridid        
        x = (x*16)+2
        y = (y*16)+2

        if TType == '1':
             rand = random.randint(1, 100)
             if rand <95:
                 canvas.create_image(x,y,anchor="nw",image=self.grassimage1)
             elif rand >=95:
                 canvas.create_image(x,y,anchor="nw",image=self.grassimage2)
 
        if TType == '2':
            rand = random.randint(1, 100)
            if rand <80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage1)
            elif rand  >=80:
                canvas.create_image(x,y,anchor="nw",image=self.waterimage2)      

        if TType == '3': canvas.create_image(x,y,anchor="nw",image=self.stoneimage)
        if TType == '4': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][0])
        if TType == '5': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][0])
        if TType == '6': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[0][1])
        if TType == '7': canvas.create_image(x,y,anchor="nw",image=self.stumpimage[1][1])
        if TType == '8': canvas.create_image(x,y,anchor="nw",image=self.flowerimage)
        if TType == 'a': canvas.create_image(x,y,anchor="nw",image=self.I1)
        if TType == 'b': canvas.create_image(x,y,anchor="nw",image=self.I2)
        if TType == 'c': canvas.create_image(x,y,anchor="nw",image=self.I3)
        if TType == 'd': canvas.create_image(x,y,anchor="nw",image=self.I4)
        if TType == 'e': canvas.create_image(x,y,anchor="nw",image=self.I5)
        if TType == 'f': canvas.create_image(x,y,anchor="nw",image=self.I6)
        if TType == 'g': canvas.create_image(x,y,anchor="nw",image=self.I7)
        if TType == 'h': canvas.create_image(x,y,anchor="nw",image=self.I8)
        if TType == 'i': canvas.create_image(x,y,anchor="nw",image=self.I9)
        if TType == 'j': cavas.create_image(x,y,anchor="nw",image=self.I10)
        if TType == 'k': canvas.create_image(x,y,anchor="nw",image=self.I11)
        if TType == 'l': canvas.create_image(x,y,anchor="nw",image=self.I12)
        if TType == 'm': canvas.create_image(x,y,anchor="nw",image=self.I13)
        if TType == 'n': canvas.create_image(x,y,anchor="nw",image=self.I14)
        if TType == 'o': canvas.create_image(x,y,anchor="nw",image=self.I15)
        if TType == 'p': canvas.create_image(x,y,anchor="nw",image=self.I16)
        if TType == 'q': canvas.create_image(x,y,anchor="nw",image=self.I17)
        if TType == 'r': canvas.create_image(x,y,anchor="nw",image=self.I18)
        if TType == 's': canvas.create_image(x,y,anchor="nw",image=self.I19)
        if TType == 't': canvas.create_image(x,y,anchor="nw",image=self.I20)
        if TType == 'u': canvas.create_image(x,y,anchor="nw",image=self.I21)
        if TType == 'v': canvas.create_image(x,y,anchor="nw",image=self.I22)
        if TType == 'w': canvas.create_image(x,y,anchor="nw",image=self.I23)
        if TType == 'x': canvas.create_image(x,y,anchor="nw",image=self.I24)
        if TType == 'y': canvas.create_image(x,y,anchor="nw",image=self.I25)
        if TType == 'z': canvas.create_image(x,y,anchor="nw",image=self.I26)
        if TType == 'A': canvas.create_image(x,y,anchor="nw",image=self.I27)
        if TType == 'B': canvas.create_image(x,y,anchor="nw",image=self.I28)
        if TType == 'C': canvas.create_image(x,y,anchor="nw",image=self.I29)
        if TType == 'D': canvas.create_image(x,y,anchor="nw",image=self.I30)
        if TType == 'E': canvas.create_image(x,y,anchor="nw",image=self.I31)
        if TType == 'F': canvas.create_image(x,y,anchor="nw",image=self.I32)
        if TType == 'G': canvas.create_image(x,y,anchor="nw",image=self.I33)
        if TType == 'H': canvas.create_image(x,y,anchor="nw",image=self.I34)
        if TType == 'I': canvas.create_image(x,y,anchor="nw",image=self.I35)
        if TType == 'J': canvas.create_image(x,y,anchor="nw",image=self.I36)
        if TType == 'K': canvas.create_image(x,y,anchor="nw",image=self.I37)
        if TType == 'L': canvas.create_image(x,y,anchor="nw",image=self.I38)
        if TType == 'M': canvas.create_image(x,y,anchor="nw",image=self.I39)
        if TType == 'N': canvas.create_image(x,y,anchor="nw",image=self.I40)
        if TType == 'O': canvas.create_image(x,y,anchor="nw",image=self.I41)
        if TType == 'P': canvas.create_image(x,y,anchor="nw",image=self.I42)
        if TType == 'Q': canvas.create_image(x,y,anchor="nw",image=self.I43)
        if TType == 'R': canvas.create_image(x,y,anchor="nw",image=self.I44)
        if TType == 'S': canvas.create_image(x,y,anchor="nw",image=self.I45)
        if TType == 'T': canvas.create_image(x,y,anchor="nw",image=self.I46)
        if TType == 'U': canvas.create_image(x,y,anchor="nw",image=self.I47)
        if TType == 'V': canvas.create_image(x,y,anchor="nw",image=self.I48)
        if TType == 'W': canvas.create_image(x,y,anchor="nw",image=self.I49)
        if TType == 'X': canvas.create_image(x,y,anchor="nw",image=self.I50)
        if TType == 'Y': canvas.create_image(x,y,anchor="nw",image=self.I51)
        if TType == 'Z': canvas.create_image(x,y,anchor="nw",image=self.I52)
        if TType == '!': canvas.create_image(x,y,anchor="nw",image=self.I53)
        if TType == '"': canvas.create_image(x,y,anchor="nw",image=self.I54)
        if TType == '£': canvas.create_image(x,y,anchor="nw",image=self.I55)
        if TType == '$': canvas.create_image(x,y,anchor="nw",image=self.I56)
        if TType == '%': canvas.create_image(x,y,anchor="nw",image=self.I57)
        if TType == '^': canvas.create_image(x,y,anchor="nw",image=self.I58)
        if TType == '&': canvas.create_image(x,y,anchor="nw",image=self.I59)
        if TType == '*': canvas.create_image(x,y,anchor="nw",image=self.I60)
        if TType == '(': canvas.create_image(x,y,anchor="nw",image=self.I61)
        if TType == ')': canvas.create_image(x,y,anchor="nw",image=self.I62)
        if TType == '-': canvas.create_image(x,y,anchor="nw",image=self.I63)
        if TType == '_': canvas.create_image(x,y,anchor="nw",image=self.I64)
        if TType == '=': canvas.create_image(x,y,anchor="nw",image=self.I65)
        if TType == '+': canvas.create_image(x,y,anchor="nw",image=self.I66)
        if TType == '[': canvas.create_image(x,y,anchor="nw",image=self.I67)
        if TType == '{': canvas.create_image(x,y,anchor="nw",image=self.I68)
        if TType == '~': canvas.create_image(x,y,anchor="nw",image=self.I69)
        if TType == ',': canvas.create_image(x,y,anchor="nw",image=self.I70)
        if TType == '<': canvas.create_image(x,y,anchor="nw",image=self.I71)
        if TType == '.': canvas.create_image(x,y,anchor="nw",image=self.I72)
        if TType == '>': canvas.create_image(x,y,anchor="nw",image=self.I73)
        if TType == '/': canvas.create_image(x,y,anchor="nw",image=self.I74)
        
    def Click(self,event):
        x=round_down(event.x,16)
        y=round_down(event.y,16)
        x=x//16
        y=y//16
        self.drawtile((x,y),self.TType,self.canvas)
        self.MapData[x,y] = self.TType
        
    def TClick(self,event):

        x=(round_down(event.x,16))//16
        y=(round_down(event.y,16))//16
        
        Tile = self.TileWindow[(x,y)]

        if not Tile:
            return
       
        self.TType = Tile
        
    def Key(self,event):
        
        if event.char.isdigit() == True:            
            self.TType = event.char
        else:
                
            if event.char == 'p':
                print(self.MapData)
                
            if event.char == 's':
                self.savemap()

            if event.char =='i':
                self.movecamera('up')

            if event.char =='j':
                self.movecamera('left')

            if event.char =='k':
                self.movecamera('down')

            if event.char =='l':
                self.movecamera('right')

            if event.char == 'r':
                self.rotation +=1
                if self.rotation ==2: self.rotation = 0

    def create(self):

        self.height = 800
        self.width = 1280
        
        self.canvas = Canvas(self.window,width=self.width-2, height=self.height-2, bg='black')
        self.canvas_Tiles = Canvas(self.window,width=320, height=self.height, bg='green')

        self.canvas.grid(row = 0,column = 0)
        self.canvas_Tiles.grid(row = 0,column =1,rowspan=2)

        y=-1
        with open('TilesforUse.txt','r') as f:
            for line in f:
                y += 1
                x=-1
                for character in line:
                    x += 1
                    self.TileWindow[(x,y)] = character
                    
        q=-1
        for s in range (0,40):
            for q in range (0,25):
                if (s,q) in self.TileWindow:
                    self.drawtile((s,q),self.TileWindow[(s,q)],self.canvas_Tiles)

        b=-1
        for v in range (0,self.y):
            for b in range (0,self.x):
                self.MapData[(b,v)] = '1'
     


        self.canvas.bind('<Button-1>',self.Click)
        self.canvas.bind('<B1-Motion>',self.Click)
        self.canvas_Tiles.bind('<Button-1>',self.TClick)
        self.window.bind_all('<Key>',self.Key)
        #self.window.bind('<Right>',)
        #self.window.bind('<Left>',)
        #self.window.bind('<Up>',)                         
        #self.window.bind('<Down>',)
               
def round_down(num, divisor):
    return num - (num%divisor)

def addcords(cord1,cord2):
    x1,y1 = cord1
    x2,y2 = cord2
    x3,y3 = (x1+x2,y1+y2)

    return (x3,y3)

def something():
    surface1 = surface()
    #surface1.create()
    surface1.openfile()
    surface1.window.mainloop()
    
something()

