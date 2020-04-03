from PIL import ImageTk, Image
from tkinter import Button
from tkinter import ttk
import threading
import tkinter
import time


tk = tkinter.Tk()
style = ttk.Style()

sides   =  'bottom'
red     =  'red'
orange  =  'orange'
white   =  'white'
green   =  'green'
yellow  =  'yellow'
blue    =  'blue'

CC   =  []  
cm1  =  []

a = 800
b = 1100
i = int(a/12)
j = int(a/12)
x = int(a/22.5)
y = int(b/30)

timer = tkinter.Text(tk, width=5, height=1)
timer.insert(tkinter.INSERT, "00:00")
timer.pack()
def show_time():
    start = time.time()
    seconds = 0
    while True:
        if time.time() - start > 1:
            seconds += int(time.time() - start)
            start = time.time()
            cur_index = timer.index(tkinter.INSERT)
            cur_index = str(int(cur_index[0]) - 1) + cur_index[1:]
            timer.delete(cur_index, tkinter.INSERT)
            timer.insert(tkinter.INSERT, str(int(seconds / 60)) + ":" + str(seconds % 60))
            tk.update()
thread = threading.Thread(target=show_time)
thread.start()

tk.geometry('1000x600')
fond = tkinter.Canvas(tk, width=b , heigh=a ,bg='#E4E4E4')
fond.pack() 

def CubeResolue() :

    global cr,red,orange,white,green,yellow,blue,CC

    cr  = [[[red,red,red],[red,red,red],[red,red,red]],
          [[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]],
          [[white,white,white],[white,white,white],[white,white,white]],
          [[green,green,green],[green,green,green],[green,green,green]],
          [[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]],
          [[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]]]

    CC  =  cr

def AfficheGraphique3D ():

    c = 2*x
    d = 2*y

    fond.create_polygon(c+4.32*x ,  d+2*y ,     c+2.66*x ,  d+2.66*y , c+1*x ,    d+2*y ,    c+2.66*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [0] [0])
    fond.create_polygon(c+5.98*x ,  d+2.66*y ,  c+4.32*x ,  d+3.33*y , c+2.66*x , d+2.66*y , c+4.32*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [0] [1])
    fond.create_polygon(c+7.66*x ,  d+3.34*y ,  c+6*x ,     d+4*y ,    c+4.32*x , d+3.33*y , c+5.98*x ,    d+2.66*y  ,outline='black' ,  fill=CC [0] [0] [2])
    fond.create_polygon(c+5.98*x ,  d+1.34*y ,  c+4.32*x ,  d+2*y ,    c+2.66*x , d+1.34*y , c+4.32*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [1] [0])
    fond.create_polygon(c+7.66*x ,  d+2*y ,     c+5.98*x ,  d+2.66*y , c+4.32*x , d+2*y ,    c+5.98*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [1] [1])
    fond.create_polygon(c+9.32*x ,  d+2.67*y ,  c+7.66*x ,  d+3.34*y , c+5.98*x , d+2.66*y , c+7.64*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [1] [2])
    fond.create_polygon(c+7.66*x ,  d+0.66*y ,  c+5.98*x ,  d+1.34*y , c+4.32*x , d+0.67*y , c+6*x ,       d+0*y     ,outline='black' ,  fill=CC [0] [2] [0])
    fond.create_polygon(c+9.32*x ,  d+1.33*y ,  c+7.64*x ,  d+2*y ,    c+5.98*x , d+1.34*y , c+7.66*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [2] [1])
    fond.create_polygon(c+11*x ,    d+2*y ,     c+9.32*x ,  d+2.67*y , c+7.64*x , d+2*y ,    c+9.32*x ,    d+1.33*y  ,outline='black' ,  fill=CC [0] [2] [2])

    fond.create_polygon(c+22*x ,    d+2*y ,     c+20.32*x , d+2.67*y , c+18.64*x , d+2*y ,    c+20.32*x ,  d+1.33*y  ,outline='black' ,  fill=CC [1] [0] [0])
    fond.create_polygon(c+20.32*x , d+2.67*y ,  c+18.66*x , d+3.34*y , c+16.98*x , d+2.66*y , c+18.64*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [1] [0])
    fond.create_polygon(c+18.66*x , d+3.34*y ,  c+17*x ,    d+4*y ,    c+15.32*x , d+3.33*y , c+16.98*x ,  d+2.66*y  ,outline='black' ,  fill=CC [1] [2] [0])
    fond.create_polygon(c+20.32*x , d+1.33*y ,  c+18.64*x , d+2*y ,    c+16.98*x , d+1.34*y , c+18.66*x ,  d+0.66*y  ,outline='black' ,  fill=CC [1] [0] [1])
    fond.create_polygon(c+18.66*x , d+2*y ,     c+16.98*x , d+2.66*y , c+15.32*x , d+2*y ,    c+16.98*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [1] [1])
    fond.create_polygon(c+16.98*x , d+2.66*y ,  c+15.32*x , d+3.33*y , c+13.66*x , d+2.66*y , c+15.32*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [2] [1])
    fond.create_polygon(c+18.66*x , d+0.66*y ,  c+16.98*x , d+1.34*y , c+15.32*x , d+0.67*y , c+17*x ,     d+0*y     ,outline='black' ,  fill=CC [1] [0] [2])
    fond.create_polygon(c+16.98*x , d+1.34*y ,  c+15.32*x , d+2*y ,    c+13.66*x , d+1.34*y , c+15.32*x ,  d+0.67*y  ,outline='black' ,  fill=CC [1] [1] [2])
    fond.create_polygon(c+15.32*x , d+2*y ,     c+13.66*x , d+2.66*y , c+12*x ,    d+2*y ,    c+13.66*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [2] [2]) 

    fond.create_polygon(c+2.66*x ,  d+5.03*y ,  c+1*x ,     d+4.36*y ,  c+1*x ,    d+2*y ,    c+2.66*x ,   d+2.66*y  ,outline='black' ,  fill=CC [2] [0] [0])
    fond.create_polygon(c+2.66*x ,  d+7.36*y ,  c+1*x ,     d+6.66*y ,  c+1*x ,    d+4.36*y , c+2.66*x ,   d+5.03*y  ,outline='black' ,  fill=CC [2] [0] [1])
    fond.create_polygon(c+2.66*x ,  d+9.66*y ,  c+1*x ,     d+9*y ,     c+1*x ,    d+6.66*y , c+2.66*x ,   d+7.32*y  ,outline='black' ,  fill=CC [2] [0] [2])
    fond.create_polygon(c+4.32*x ,  d+5.69*y ,  c+2.66*x ,  d+5.03*y ,  c+2.66*x , d+2.66*y , c+4.32*x ,   d+3.33*y  ,outline='black' ,  fill=CC [2] [1] [0])
    fond.create_polygon(c+4.32*x ,  d+8.02*y ,  c+2.66*x ,  d+7.36*y ,  c+2.66*x , d+5.03*y , c+4.32*x ,   d+5.69*y  ,outline='black' ,  fill=CC [2] [1] [1])
    fond.create_polygon(c+4.32*x ,  d+10.33*y , c+2.66*x ,  d+9.66*y ,  c+2.66*x , d+7.36*y , c+4.32*x ,   d+8.02*y  ,outline='black' ,  fill=CC [2] [1] [2])
    fond.create_polygon(c+6*x ,     d+6.33*y ,  c+4.32*x ,  d+5.69*y ,  c+4.32*x , d+3.33*y , c+6*x ,      d+4*y     ,outline='black' ,  fill=CC [2] [2] [0])
    fond.create_polygon(c+6*x ,     d+8.66*y ,  c+4.32*x ,  d+8.02*y ,  c+4.32*x , d+5.69*y , c+6*x ,      d+6.33*y  ,outline='black' ,  fill=CC [2] [2] [1])
    fond.create_polygon(c+6*x ,     d+11*y ,    c+4.32*x ,  d+10.33*y , c+4.32*x , d+8.02*y , c+6*x ,      d+8.66*y  ,outline='black' ,  fill=CC [2] [2] [2])      

    fond.create_polygon(c+7.66*x ,  d+5.69*y ,  c+6*x ,     d+6.33*y ,   c+6*x ,    d+4*y ,    c+7.66*x ,  d+3.33*y  ,outline='black' ,  fill=CC [3] [0] [0])
    fond.create_polygon(c+7.66*x ,  d+8.02*y ,  c+6*x ,     d+8.66*y ,   c+6*x,     d+6.33*y , c+7.66*x,   d+5.69*y  ,outline='black' ,  fill=CC [3] [0] [1])
    fond.create_polygon(c+7.66*x ,  d+10.33*y , c+6*x ,     d+11*y ,     c+6*x ,    d+8.66*y , c+7.66*x ,  d+8.02*y  ,outline='black' ,  fill=CC [3] [0] [2])
    fond.create_polygon(c+9.32*x ,  d+5.04*y ,  c+7.66*x ,  d+5.7*y ,    c+7.66*x , d+3.34*y , c+9.32*x ,  d+2.67*y  ,outline='black' ,  fill=CC [3] [1] [0])
    fond.create_polygon(c+9.32*x ,  d+7.34*y ,  c+7.66*x ,  d+8*y ,      c+7.66*x , d+5.7*y ,  c+9.32*x ,  d+5.04*y  ,outline='black' ,  fill=CC [3] [1] [1])
    fond.create_polygon(c+9.32*x ,  d+9.67*y ,  c+7.66*x ,  d+10.33*y ,  c+7.66*x , d+8*y ,    c+9.32*x ,  d+7.33*y  ,outline='black' ,  fill=CC [3] [1] [2])
    fond.create_polygon(c+11*x ,    d+4.36*y ,  c+9.32*x ,  d+5.04*y ,   c+9.32*x , d+2.67*y , c+11*x ,    d+2*y     ,outline='black' ,  fill=CC [3] [2] [0])
    fond.create_polygon(c+11*x ,    d+6.67*y ,  c+9.32*x ,  d+7.34*y ,   c+9.32*x , d+5.04*y , c+11*x ,    d+4.36*y  ,outline='black' ,  fill=CC [3] [2] [1])
    fond.create_polygon(c+11*x ,    d+9*y ,     c+9.32*x ,  d+9.67*y ,   c+9.32*x , d+7.33*y , c+11*x ,    d+6.66*y  ,outline='black' ,  fill=CC [3] [2] [2])

    fond.create_polygon(c+18.66*x , d+5.66*y ,  c+17*x ,    d+6.33*y ,  c+17*x ,    d+4*y ,    c+18.66*x , d+3.33*y  ,outline='black' ,  fill=CC [5] [0] [0])
    fond.create_polygon(c+18.66*x , d+8*y ,     c+17*x ,    d+8.66*y ,  c+17*x ,    d+6.33*y , c+18.66*x , d+5.66*y  ,outline='black' ,  fill=CC [5] [0] [1])
    fond.create_polygon(c+18.66*x , d+10.33*y , c+17*x ,    d+11*y ,    c+17*x ,    d+8.66*y , c+18.66*x , d+8*y     ,outline='black' ,  fill=CC [5] [0] [2])
    fond.create_polygon(c+20.32*x , d+5*y ,     c+18.66*x , d+5.66*y ,  c+18.66*x , d+3.33*y , c+20.32*x , d+2.66*y  ,outline='black' ,  fill=CC [5] [1] [0])
    fond.create_polygon(c+20.32*x , d+7.33*y ,  c+18.66*x , d+8*y ,     c+18.66*x , d+5.66*y , c+20.32*x , d+5*y     ,outline='black' ,  fill=CC [5] [1] [1])
    fond.create_polygon(c+20.32*x , d+9.66*y ,  c+18.66*x , d+10.33*y , c+18.66*x , d+8*y ,    c+20.32*x , d+7.33*y  ,outline='black' ,  fill=CC [5] [1] [2])
    fond.create_polygon(c+22*x ,    d+4.36*y ,  c+20.32*x , d+5*y ,     c+20.32*x , d+2.66*y , c+22*x ,    d+2*y     ,outline='black' ,  fill=CC [5] [2] [0])
    fond.create_polygon(c+22*x ,    d+6.66*y ,  c+20.32*x , d+7.33*y ,  c+20.32*x , d+5*y ,    c+22*x ,    d+4.36*y  ,outline='black' ,  fill=CC [5] [2] [1])
    fond.create_polygon(c+22*x ,    d+9*y ,     c+20.32*x , d+9.66*y ,  c+20.32*x , d+7.33*y , c+22*x ,    d+6.66*y  ,outline='black' ,  fill=CC [5] [2] [2])

    fond.create_polygon(c+13.66*x , d+5*y ,     c+12*x ,    d+4.36*y ,  c+12*x ,    d+2*y ,    c+13.66*x , d+2.66*y  ,outline='black' ,  fill=CC [4] [2] [0])
    fond.create_polygon(c+13.66*x , d+7.32*y ,  c+12*x ,    d+6.66*y ,  c+12*x ,    d+4.36*y , c+13.66*x , d+5*y     ,outline='black' ,  fill=CC [4] [2] [1]) 
    fond.create_polygon(c+13.66*x , d+9.66*y ,  c+12*x ,    d+9*y ,     c+12*x ,    d+6.66*y , c+13.66*x , d+7.32*y  ,outline='black' ,  fill=CC [4] [2] [2])
    fond.create_polygon(c+15.32*x , d+5.66*y ,  c+13.66*x , d+5*y ,     c+13.66*x , d+2.66*y , c+15.32*x , d+3.33*y  ,outline='black' ,  fill=CC [4] [1] [0])
    fond.create_polygon(c+15.32*x , d+8*y ,     c+13.66*x , d+7.32*y ,  c+13.66*x , d+5*y ,    c+15.32*x , d+5.66*y  ,outline='black' ,  fill=CC [4] [1] [1])  
    fond.create_polygon(c+15.32*x , d+10.33*y , c+13.66*x , d+9.66*y ,  c+13.66*x , d+7.32*y , c+15.32*x , d+8*y     ,outline='black' ,  fill=CC [4] [1] [2])
    fond.create_polygon(c+17*x ,    d+6.33*y ,  c+15.32*x , d+5.66*y ,  c+15.32*x , d+3.33*y , c+17*x ,    d+4*y     ,outline='black' ,  fill=CC [4] [0] [0])
    fond.create_polygon(c+17*x ,    d+8.66*y ,  c+15.32*x , d+8*y ,     c+15.32*x , d+5.66*y , c+17*x ,    d+6.33*y  ,outline='black' ,  fill=CC [4] [0] [1])
    fond.create_polygon(c+17*x ,    d+11*y ,    c+15.32*x , d+10.33*y , c+15.32*x , d+8*y ,    c+17*x ,    d+8.66*y  ,outline='black' ,  fill=CC [4] [0] [2])

def update():
    Bmvt1 = Button(tk, text="Mvt1", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt1 , image = photo)
    fond.create_window(3.5*x, 105, window=Bmvt1)

    Bmvt2 = Button(tk, text="Mvt2", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt2 , image = photo2)
    fond.create_window(23.25*x, 430, window=Bmvt2)

    Bmvt3 = Button(tk, text="Mvt3", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt3 , image = photo)
    fond.create_window(5.25*x, 80, window=Bmvt3)
    
    Bmvt4 = Button(tk, text="Mvt4", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt4 , image = photo2)
    fond.create_window(21.5*x, 455, window=Bmvt4)

    Bmvt5 = Button(tk, text="Mvt5", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt5 , image = photo)
    fond.create_window(7*x, 55 , window=Bmvt5)
    
    Bmvt6 = Button(tk, text="Mvt6", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt6 , image = photo2)
    fond.create_window(20*x, 475 , window=Bmvt6)

    Bmvt7 = Button(tk, text="Mvt7", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt7 , image = photo3)
    fond.create_window(2*x, 180, window=Bmvt7)

    Bmvt8 = Button(tk, text="Mvt8", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt8 , image = photo1)
    fond.create_window(25*x, 180 , window=Bmvt8)

    Bmvt9 = Button(tk, text="Mvt9", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt9 , image = photo3)
    fond.create_window(2*x, 265, window=Bmvt9)

    Bmvt10 = Button(tk, text="Mvt10", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt10 , image = photo1)
    fond.create_window(25*x, 265, window=Bmvt10)

    Bmvt11 = Button(tk, text="Mvt11", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt11 , image = photo3)
    fond.create_window(2*x, 350, window=Bmvt11)

    Bmvt12 = Button(tk, text="Mvt12", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt12 , image = photo1)
    fond.create_window(25*x , 350, window=Bmvt12)

    Bmvt13 = Button(tk, text="Mvt13", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt13 , image = photo2)
    fond.create_window(3.5*x , 460, window=Bmvt13)

    Bmvt14 = Button(tk, text="Mvt14", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt14 , image = photo)
    fond.create_window(20*x, 65 , window=Bmvt14)

    Bmvt15 = Button(tk, text="Mvt15", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt15 , image = photo2)
    fond.create_window(5.25*x , 480, window=Bmvt15)

    Bmvt16 = Button(tk, text="Mvt16", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt16 , image = photo)
    fond.create_window(21.5*x , 85, window=Bmvt16)

    Bmvt17 = Button(tk, text="Mvt17", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt17 , image = photo2)
    fond.create_window(7*x , 500, window=Bmvt17)

    Bmvt18 = Button(tk, text="Mvt18", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt18 , image = photo)
    fond.create_window(23.25*x , 108, window=Bmvt18) 

def Opt_Affichage () :

        AfficheGraphique3D ()

# Cette fonction effectue un mouvement vers l'avant de la première colonne.
def Mvt1():
    global CC,cm1
    cm1=[[[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[5][2][2],CC[5][2][1],CC[5][2][0]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][2][0],CC[2][1][0],CC[2][0][0]],[CC[2][2][1],CC[2][1][1],CC[2][0][1]],[CC[2][2][2],CC[2][1][2],CC[2][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][0][2],CC[0][0][1],CC[0][0][0]]]]

    CC=cm1

    Opt_Affichage ()
    

# Cette fonction effectue un mouvement vers l'arrière de la première colonne.
def Mvt2():
    global CC,cm2
    
    cm2=[[[CC[5][2][0],CC[5][2][1],CC[5][2][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][2],CC[2][1][2],CC[2][2][2]],[CC[2][0][1],CC[2][1][1],CC[2][2][1]],[CC[2][0][0],CC[2][1][0],CC[2][2][0]]],
         [[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[1][0][0],CC[1][0][1],CC[1][0][2]]]]
    CC=cm2

    Opt_Affichage ()
        
# Mvt3 correspond au mouvement vers l'avant de la 2ème colonne.
def Mvt3():
    global CC,cm3
    cm3=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[5][1][2],CC[5][1][1],CC[5][1][0]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[0][1][2],CC[0][1][1],CC[0][1][0]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm3

    Opt_Affichage ()
        
# Mvt4 correspond au mouvement vers l'arrière de la 2ème colonne.

def Mvt4():
    global CC,cm4

    cm4=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm4

    Opt_Affichage ()
        

# Mvt5 correspond au mouvement vers l'avant de la 3ème colonne.
def Mvt5 ():
    global CC ,cm5
    cm5=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[4][0][2],CC[4][1][2],CC[4][2][2]],[CC[4][0][1],CC[4][1][1],CC[4][2][1]],[CC[4][0][0],CC[4][1][0],CC[4][2][0]]],
         [[CC[0][2][2],CC[0][2][1],CC[0][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm5

    Opt_Affichage ()
        

# Mvt6 correspond au mouvement vers l'arrière de la 3ème colonne.
def Mvt6():
   global CC,cm6
   cm6=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
        [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
        [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
        [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
        [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
        [[CC[1][2][2],CC[1][2][1],CC[1][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
   CC=cm6

   Opt_Affichage ()
    
# Mvt7 correspond au mouvement vers la gauche de la 1ère ligne.
def Mvt7():
    global CC ,cm7
    cm7=[[[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[3][0][0],CC[2][0][1],CC[2][0][2]],[CC[3][1][0],CC[2][1][1],CC[2][1][2]],[CC[3][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[4][0][0],CC[3][0][1],CC[3][0][2]],[CC[4][1][0],CC[3][1][1],CC[3][1][2]],[CC[4][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[5][0][0],CC[4][0][1],CC[4][0][2]],[CC[5][1][0],CC[4][1][1],CC[4][1][2]],[CC[5][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[2][0][0],CC[5][0][1],CC[5][0][2]],[CC[2][1][0],CC[5][1][1],CC[5][1][2]],[CC[2][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm7

    Opt_Affichage ()


# Mvt8 correspond au mouvement vers la droite de la 1ère ligne.
def Mvt8():
    global CC ,cm8
    cm8=[[[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[2][0][2]],[CC[5][1][0],CC[2][1][1],CC[2][1][2]],[CC[5][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[3][0][2]],[CC[2][1][0],CC[3][1][1],CC[3][1][2]],[CC[2][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[4][0][2]],[CC[3][1][0],CC[4][1][1],CC[4][1][2]],[CC[3][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[5][0][2]],[CC[4][1][0],CC[5][1][1],CC[5][1][2]],[CC[4][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm8

    Opt_Affichage ()
        

 #Mvt9 correspond au mouvement vers la gauche de la 2ème ligne.
def Mvt9():
    global CC ,cm9
    cm9=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[2][0][2]],[CC[2][1][0],CC[3][1][1],CC[2][1][2]],[CC[2][2][0],CC[3][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[3][0][2]],[CC[3][1][0],CC[4][1][1],CC[3][1][2]],[CC[3][2][0],CC[4][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[4][0][2]],[CC[4][1][0],CC[5][1][1],CC[4][1][2]],[CC[4][2][0],CC[5][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[5][0][2]],[CC[5][1][0],CC[2][1][1],CC[5][1][2]],[CC[5][2][0],CC[2][2][1],CC[5][2][2]]]]
    CC=cm9

    Opt_Affichage ()
        

# Mvt 10 correspond au mouvement vers la droite de la 2ème ligne.
def Mvt10():
    global CC ,cm10
    cm10=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[5][0][1],CC[2][0][2]],[CC[2][1][0],CC[5][1][1],CC[2][1][2]],[CC[2][2][0],CC[5][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[2][0][1],CC[3][0][2]],[CC[3][1][0],CC[2][1][1],CC[3][1][2]],[CC[3][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[3][0][1],CC[4][0][2]],[CC[4][1][0],CC[3][1][1],CC[4][1][2]],[CC[4][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[4][0][1],CC[5][0][2]],[CC[5][1][0],CC[4][1][1],CC[5][1][2]],[CC[5][2][0],CC[4][2][1],CC[5][2][2]]]]
    CC=cm10

    Opt_Affichage ()
    

# Mvt 11 correspond au mouvement vers la gauche de la 3ème ligne.
def Mvt11():
    global CC ,cm11
    cm11=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[3][0][2]],[CC[2][1][0],CC[2][1][1],CC[3][1][2]],[CC[2][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[4][0][2]],[CC[3][1][0],CC[3][1][1],CC[4][1][2]],[CC[3][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[5][0][2]],[CC[4][1][0],CC[4][1][1],CC[5][1][2]],[CC[4][2][0],CC[4][2][1],CC[5][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[2][0][2]],[CC[5][1][0],CC[5][1][1],CC[2][1][2]],[CC[5][2][0],CC[5][2][1],CC[2][2][2]]]]
    CC=cm11

    Opt_Affichage ()
      

# Mvt 12 correspond au mouvement vers la droite de la 3ème ligne.
def Mvt12():
    global CC ,cm12
    cm12=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[2][0][0],CC[2][0][1],CC[5][0][2]],[CC[2][1][0],CC[2][1][1],CC[5][1][2]],[CC[2][2][0],CC[2][2][1],CC[5][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[2][0][2]],[CC[3][1][0],CC[3][1][1],CC[2][1][2]],[CC[3][2][0],CC[3][2][1],CC[2][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[3][0][2]],[CC[4][1][0],CC[4][1][1],CC[3][1][2]],[CC[4][2][0],CC[4][2][1],CC[3][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[4][0][2]],[CC[5][1][0],CC[5][1][1],CC[4][1][2]],[CC[5][2][0],CC[5][2][1],CC[4][2][2]]]]
    CC=cm12

    Opt_Affichage ()
     

def Mvt13():
    global CC,cm13
    cm13=[[[CC[4][2][0],CC[0][0][1],CC[0][0][2]],[CC[4][2][1],CC[0][1][1],CC[0][1][2]],[CC[4][2][2],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[2][0][0]],[CC[1][1][0],CC[1][1][1],CC[2][0][1]],[CC[1][2][0],CC[1][2][1],CC[2][0][2]]],
          [[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[5][0][2],CC[5][1][2],CC[5][2][2]],[CC[5][0][1],CC[5][1][1],CC[5][2][1]],[CC[5][0][0],CC[5][1][0],CC[5][2][0]]]]
    CC=cm13

    Opt_Affichage ()     
        
def Mvt14():
    global CC,cm14
    cm14=[[[CC[2][0][2],CC[0][0][1],CC[0][0][2]],[CC[2][0][1],CC[0][1][1],CC[0][1][2]],[CC[2][0][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[4][2][2]],[CC[1][1][0],CC[1][1][1],CC[4][2][1]],[CC[1][2][0],CC[1][2][1],CC[4][2][0]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
          [[CC[5][2][0],CC[5][1][0],CC[5][0][0]],[CC[5][2][1],CC[5][1][1],CC[5][0][1]],[CC[5][2][2],CC[5][1][2],CC[5][0][2]]]]
    CC=cm14

    Opt_Affichage ()
  
        
def Mvt15():
    global CC,cm15
    cm15=[[[CC[0][0][0],CC[4][1][0],CC[0][0][2]],[CC[0][1][0],CC[4][1][1],CC[0][1][2]],[CC[0][2][0],CC[4][1][2],CC[0][2][2]]],
          [[CC[1][0][0],CC[2][1][0],CC[1][0][2]],[CC[1][1][0],CC[2][1][1],CC[1][1][2]],[CC[1][2][0],CC[2][1][2],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm15

    Opt_Affichage ()    
        

def Mvt16():
    global CC,cm16
    cm16=[[[CC[0][0][0],CC[2][1][2],CC[0][0][2]],[CC[0][1][0],CC[2][1][1],CC[0][1][2]],[CC[0][2][0],CC[2][1][0],CC[0][2][2]]],
          [[CC[1][0][0],CC[4][1][2],CC[1][0][2]],[CC[1][1][0],CC[4][1][1],CC[1][1][2]],[CC[1][2][0],CC[4][1][0],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm16

    Opt_Affichage ()
    

def Mvt17():
    global CC,cm17
    cm17=[[[CC[0][0][0],CC[0][0][1],CC[4][0][0]],[CC[0][1][0],CC[0][1][1],CC[4][0][1]],[CC[0][2][0],CC[0][2][1],CC[4][0][2]]],
          [[CC[2][2][0],CC[1][0][1],CC[1][0][2]],[CC[2][2][1],CC[1][1][1],CC[1][1][2]],[CC[2][2][2],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
          [[CC[3][2][0],CC[3][1][0],CC[3][0][0]],[CC[3][2][1],CC[3][1][1],CC[3][0][1]],[CC[3][2][2],CC[3][1][2],CC[3][0][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm17

    Opt_Affichage ()


def Mvt18():

    global CC,cm18
    
    cm18=[[[CC[0][0][0],CC[0][0][1],CC[2][2][2]],[CC[0][1][0],CC[0][1][1],CC[2][2][1]],[CC[0][2][0],CC[0][2][1],CC[2][2][0]]],
          [[CC[4][0][2],CC[1][0][1],CC[1][0][2]],[CC[4][0][1],CC[1][1][1],CC[1][1][2]],[CC[4][0][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[3][0][2],CC[3][1][2],CC[3][2][2]],[CC[3][0][1],CC[3][1][1],CC[3][2][1]],[CC[3][0][0],CC[3][1][0],CC[3][2][0]]],
          [[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm18

    Opt_Affichage ()

canv = tkinter.Canvas(tk, width=80, height=80, bg='white')

photo = ImageTk.PhotoImage(Image.open("arrow1.png"))
photo2 = ImageTk.PhotoImage(Image.open("arrow2.png"))
photo1 = ImageTk.PhotoImage(Image.open("arrow3.png"))
photo3 = ImageTk.PhotoImage(Image.open("arrow4.png"))

canv.create_image(20,20, image=photo) 


CubeResolue ()
update()
AfficheGraphique3D ()
tk.mainloop()