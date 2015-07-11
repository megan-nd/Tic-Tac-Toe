from tkinter import *
tk=Tk()
tk.title = ("Tic Tac Toe")
tk.resizable(0,0)
canvas = Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()

line_length = 300
canvas_width = 500
canvas_height = 500

def get_x1_x2(canvas_width,line_length):
    x1 = canvas_width/2-line_length/2
    x2 = x1+line_length
    return x1,x2

def horizontal_line(y,canvas_width,line_length):
    x1,x2 = get_x1_x2(canvas_width,line_length)
    canvas.create_line(x1,y,x2,y)

def get_y1_y2(canvas_height,line_length):
    y1 = canvas_height/2-line_length/2
    y2 = y1+line_length
    return y1,y2

def vertical_line(x,canvas_height,line_length):
    y1,y2 = get_y1_y2(canvas_height,line_length)
    canvas.create_line(x,y1,x,y2)

x1,x2 = get_x1_x2(canvas_width,line_length)
y1,y2 = get_y1_y2(canvas_height,line_length)
segment_length = line_length/3
horizontal_line(y1+segment_length,canvas_width,line_length)
horizontal_line(y1+segment_length*2,canvas_width,line_length)
vertical_line(x1+segment_length,canvas_width,line_length)
vertical_line(x1+segment_length*2,canvas_width,line_length)
