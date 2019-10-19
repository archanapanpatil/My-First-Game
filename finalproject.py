from tkinter import *
from winsound import *
import winsound

trace = 0
# circle
class CanvasEventsDemoCircle:
    def __init__(self, parent=None):
        canvas = Canvas(width=400, height=400, bg='beige')
        canvas.place(x=10, y=100)
        #canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_oval]  # , canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print
        objectId
        self.drawn = objectId

    def onClear(self, event):
        event.widget.delete('all')

    def onMove(self, event):
        if self.drawn:
            if trace: print
            self.drawn
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

# Rectangle
class CanvasEventsDemoRectangle:
    def __init__(self, parent=None):
        canvas = Canvas(width=400, height=400, bg='beige')
        canvas.place(x=10, y=100)
        #canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_rectangle]  # , canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print
        objectId
        self.drawn = objectId

    def onClear(self, event):
        event.widget.delete('all')

    def onMove(self, event):
        if self.drawn:
            if trace: print
            self.drawn
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

# square
class CanvasEventsDemoSquare:
    def __init__(self, parent=None):
        canvas = Canvas(width=400, height=400, bg='beige')
        canvas.place(x=10, y=100)
        #canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_rectangle]  # , canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print
        objectId
        self.drawn = objectId

    def onClear(self, event):
        event.widget.delete('all')

    def onMove(self, event):
        if self.drawn:
            if trace: print
            self.drawn
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

# Triangle
class CanvasEventsDemoTriangle:
    def __init__(self, parent=None):
        canvas = Canvas(width=400, height=400, bg='beige')
        canvas.place(x=10, y=100)
        #canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart)
        canvas.bind('<B1-Motion>', self.onGrow)
        canvas.bind('<Double-1>', self.onClear)
        canvas.bind('<ButtonPress-3>', self.onMove)
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_line]  # , canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]
        self.start = event
        self.drawn = None

    def onGrow(self, event):
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print
        objectId
        self.drawn = objectId

    def onClear(self, event):
        event.widget.delete('all')

    def onMove(self, event):
        if self.drawn:
            if trace: print
            self.drawn
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

def say_hello():
    name_of_shape = entry_1.get()
    string_to_display = "Draw a " + name_of_shape
    label_2 = Label(root)
    button8["text"] = string_to_display
    button8["bg"] = "red"
    label_2.grid(row=1, column=1)
def draw_line(event):
    global x1, y1
    python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas1.create_oval(x1, y1, x2, y2, fill=python_green)
    canvas1.bind("<B1-Motion>", draw_line)

winsound.PlaySound("game_.wav", winsound.SND_ASYNC)
winsound.PlaySound("game_head.wav", winsound.SND_ASYNC)
root = Tk()
mycanvas = Canvas(root, width=1500, height=1500, background='pink')
mycanvas.place(x=410, y=0)
label_1 = Label(root, text="Shape name:", font="15", relief="solid")
label_1.place(x=10, y=20)
label_2 = Label(root, text="Drawing section are above:", font="20", relief="solid")
label_2.place(x=90, y=620)
entry_1 = Entry(root, font="15", relief="solid")
entry_1.place(x=110, y=20)
button_1 = Button(root, text="click me", font="15", height=0, width=6, relief="solid", command=say_hello)
button_1.place(x=10, y=50)
button8 = Button(root, text="Clear ", font="25", height=4, width=25, relief="solid")
button8.place(x=70, y=520)
canvas1 = Canvas(root, width=400, height=400, background='white')
canvas1.place(x=10, y=100)
canvas1.bind('<Button-1>', draw_line)
click_number = 0
root.geometry("1500x1500")
root.title("welcome to GameZone")

# Triangle Code
img = PhotoImage(file="triangle.png")
#lable = Label(image=img)
#lable.place(x=1000, y=430)
play = lambda: PlaySound('triangle.wav', SND_FILENAME)
button1_t = Button(root, text='Triangle',image=img, width=235, height=205, command=play )
button1_t.place(x=1000, y=430)
button = Button(root, text='Triangle', width=25, command=CanvasEventsDemoTriangle)
button.place(x=1030, y=650)

# Rectangle Code
img1 = PhotoImage(file="rectangle1.png")
#lable1 = Label(image=img1)
#lable1.place(x=500, y=20)
play1 = lambda: PlaySound('Rectangle.wav', SND_FILENAME)
button1_R = Button(root, text='Rectangle',image=img1, width=205, height=205, command=play1 )
button1_R.place(x=500, y=20)
button1 = Button(root, text='Rectangle', width=25, command=CanvasEventsDemoRectangle )
button1.place(x=520, y=240)

# Circle Code
img2 = PhotoImage(file="circle1.png")
play2 = lambda: PlaySound('circle.wav', SND_FILENAME)
#lable2 = Label(image=img2 )
#lable2.place(x=550, y=430)
button2_c = Button(root, text='Circle',image=img2 , width=250, height=200, command=play2)
button2_c.place(x=500, y=410)
button2 = Button(root, text='Circle', width=25, command=CanvasEventsDemoCircle)
button2.place(x=540, y=625)

# square Code
img3 = PhotoImage(file="square1.png")
#lable3 = Label(image=img3)
#lable3.place(x=1000, y=20)
play3 = lambda: PlaySound('square.wav', SND_FILENAME)
button1_s = Button(root, text='suare',image=img3, width=205, height=205, command=play3 )
button1_s.place(x=1000, y=20)
button3 = Button(root, text='Square', width=25, command=CanvasEventsDemoSquare)
button3.place(x=1020, y=240)

root.mainloop()
