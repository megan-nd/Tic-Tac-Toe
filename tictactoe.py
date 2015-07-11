from tkinter import *
tk=Tk()
tk.title = ("Tic Tac Toe")
tk.resizable(0,0)
canvas = Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()


def horizontal_line(y,canvas_width,line_length):
    x1 = canvas_width/2-line_length/2
    x2 = x1+line_length
    canvas.create_line(x1,y,x2,y)

horizontal_line(150,500,300)
horizontal_line(250,500,300)

