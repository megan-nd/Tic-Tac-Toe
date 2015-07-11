from tkinter import *
tk=Tk()
tk.title = ("Tic Tac Toe")
tk.resizable(0,0)
line_length = 300
canvas_width = 500
canvas_height = 500
canvas = Canvas(tk,width=canvas_width,height=canvas_height,bd=0,highlightthickness=0)
canvas.pack()


def get_x1_x2():
    x1 = canvas_width/2-line_length/2
    x2 = x1+line_length
    return x1,x2

def horizontal_line(y):
    x1,x2 = get_x1_x2()
    canvas.create_line(x1,y,x2,y)

def get_y1_y2():
    y1 = canvas_height/2-line_length/2
    y2 = y1+line_length
    return y1,y2

def vertical_line(x):
    y1,y2 = get_y1_y2()
    canvas.create_line(x,y1,x,y2)

class Cursor:
    def __init__(self,canvas,color):
        self.id = canvas.create_rectangle(20,20,40,40, fill=color, outline='white')
        self.row = 2
        self.column = 2
        self.width = segment_length-2
        self.height = segment_length-2
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-Left>',self.move_left)
        self.canvas.bind_all('<KeyPress-Right>',self.move_right)
        self.canvas.bind_all('<KeyPress-Up>',self.move_up)
        self.canvas.bind_all('<KeyPress-Down>',self.move_down)
        self.draw()

    def draw(self):
        x = self.get_x()
        y = self.get_y()
        self.canvas.coords(self.id,x,y,x+self.width,y+self.height)
        tk.update()

    def move_up(self,evt):
        if self.row == 1:
            return
        self.row = self.row-1
        self.draw()

    def move_down(self,evt):
        if self.row == 3:
            return
        self.row = self.row+1
        self.draw()

    def move_left(self,evt):
        if self.column == 1:
            return
        self.column = self.column-1
        self.draw()

    def move_right(self,evt):
        if self.column == 3:
            return
        self.column = self.column+1
        self.draw()

    def get_x(self):
        x = x1+(self.column-1)*segment_length+(0.5*segment_length)-(self.width/2)
        return x

    def get_y(self):
        y = y1+(self.row-1)*segment_length+(0.5*segment_length)-(self.height/2)
        return y

class XO:
    def __init__ (self,canvas,cursor,color,character):
        x = cursor.get_x()+cursor.width/2
        y = cursor.get_y()+cursor.height/2
        canvas.create_text(x,y,text=character,fill=color,font=('Courier',50))
        
        
def button1_pressed(evt):
    X = XO(canvas,cursor,'red','X')

def button2_pressed(evt):
    O = XO(canvas,cursor,'blue','O')

x1,x2 = get_x1_x2()
y1,y2 = get_y1_y2()
segment_length = line_length/3
horizontal_line(y1+segment_length)
horizontal_line(y1+segment_length*2)
vertical_line(x1+segment_length)
vertical_line(x1+segment_length*2)

cursor = Cursor(canvas,'white')
canvas.bind_all('<KeyPress-X>',button1_pressed)
canvas.bind_all('<KeyPress-x>',button1_pressed)
canvas.bind_all('<KeyPress-O>',button2_pressed)
canvas.bind_all('<KeyPress-o>',button2_pressed)

