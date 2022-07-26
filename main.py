from tkinter import *
from math import sin, cos

size = 800

tk = Tk()
c = Canvas(tk, width=size, height=size, bg="#000000")
c.pack()

# 24:15:9:6:4:3:2 orbital resonance, starting at b

b_ = 0
c_ = 0
d_ = 0
e_ = 0
f_ = 0
g_ = 0
h_ = 0

simspeed = 1.0

def speeddown():
    global simspeed
    if simspeed == 0.25:
        simspeed = 0.00003472
    elif simspeed == 0.31:
        simspeed = 0.25
    elif simspeed == 0.40:
        simspeed = 0.31
    elif simspeed == 0.50:
        simspeed = 0.40
    elif simspeed == 0.63:
        simspeed = 0.50
    elif simspeed == 0.79:
        simspeed = 0.63
    elif simspeed == 1.00:
        simspeed = 0.79
    elif simspeed == 1.26:
        simspeed = 1.00
    elif simspeed == 1.59:
        simspeed = 1.26
    elif simspeed == 2.00:
        simspeed = 1.59
    elif simspeed == 2.52:
        simspeed = 2.00
    elif simspeed == 3.17:
        simspeed = 2.52
    elif simspeed == 4.00:
        simspeed = 3.17
    elif simspeed == 5.04:
        simspeed = 4.00
    elif simspeed == 6.35:
        simspeed = 5.04
    elif simspeed == 8.00:
        simspeed = 6.35
    elif simspeed == 10.08:
        simspeed = 8.00
    elif simspeed == 12.70:
        simspeed = 10.08
    elif simspeed == 16.00:
        simspeed = 12.70
    elif simspeed == 20.16:
        simspeed = 16.00
    elif simspeed == 25.40:
        simspeed = 20.16
    elif simspeed == 32.00:
        simspeed = 25.40
    elif simspeed == 40.32:
            simspeed = 32.00
    elif simspeed == 50.80:
        simspeed = 40.32
    elif simspeed == 64.00:
        simspeed = 50.80
def speedup():
    global simspeed
    if simspeed == 0.00003472:
        simspeed = 0.25
    elif simspeed == 0.25:
        simspeed = 0.31
    elif simspeed == 0.31:
        simspeed = 0.40
    elif simspeed == 0.40:
        simspeed = 0.50
    elif simspeed == 0.50:
        simspeed = 0.63
    elif simspeed == 0.63:
        simspeed = 0.79
    elif simspeed == 0.79:
        simspeed = 1.00
    elif simspeed == 1.00:
        simspeed = 1.26
    elif simspeed == 1.26:
        simspeed = 1.59
    elif simspeed == 1.59:
        simspeed = 2.00
    elif simspeed == 2.00:
        simspeed = 2.52
    elif simspeed == 2.52:
        simspeed = 3.17
    elif simspeed == 3.17:
        simspeed = 4.00
    elif simspeed == 4.00:
        simspeed = 5.04
    elif simspeed == 5.04:
        simspeed = 6.35
    elif simspeed == 6.35:
        simspeed = 8.00
    elif simspeed == 8.00:
        simspeed = 10.08
    elif simspeed == 10.08:
        simspeed = 12.70
    elif simspeed == 12.70:
        simspeed = 16.00
    elif simspeed == 16.00:
        simspeed = 20.16
    elif simspeed == 20.16:
        simspeed = 25.40
    elif simspeed == 25.40:
        simspeed = 32.00
    elif simspeed == 32.00:
        simspeed = 40.32
    elif simspeed == 40.32:
        simspeed = 50.80
    elif simspeed == 50.80:
        simspeed = 64.00

keplabels = False
labels = True

def change_labels():
    global keplabels
    keplabels = not keplabels

def toggle_labels():
    global labels
    labels = not labels

sdown = Button(tk, text="Slow Down", command=speeddown)
sdown.place(anchor=NW, x=5, y=5)
sup = Button(tk, text="Speed Up", command=speedup)
sup.place(anchor=NW, x=5, y=35)
clab = Button(tk, text="Toggle Kepler/TRAPPIST Labels", command=change_labels)
clab.place(anchor=NW, x=5, y=65)
tlab = Button(tk, text="Toggle Labels", command=toggle_labels)
tlab.place(anchor=NW, x=5, y=95)

while True:
    c.delete("all")
    if simspeed == 0.00003472:
        c.create_text(size-5, 5, anchor=NE, text="Speed: REAL TIME", fill="#ffffff")
    elif simspeed < 0.5:
        c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{str(round(simspeed, 2)).ljust(4, '0')}", fill="#ffffff")
    elif simspeed < 10:
        c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{round(simspeed, 1)}", fill="#ffffff")
    else:
        c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{round(simspeed, 0)}", fill="#ffffff")
    c.create_oval(size/2-10, size/2-10, size/2+10, size/2+10, fill="#ff1f00")
    bx = cos(b_)*60
    by = -sin(b_)*60
    c.create_oval(bx-7+(size/2), by-7+(size/2), bx+7+(size/2), by+7+(size/2), fill="#00ff00")
    b_ += 24*(simspeed*0.0001)
    cx = cos(c_)*82.1
    cy = -sin(c_)*82.1
    c.create_oval(cx-7+(size/2), cy-7+(size/2), cx+7+(size/2), cy+7+(size/2), fill="#ffbf00")
    c_ += 15*(simspeed*0.0001)
    dx = cos(d_)*115.8
    dy = -sin(d_)*115.8
    c.create_oval(dx-7+(size/2), dy-7+(size/2), dx+7+(size/2), dy+7+(size/2), fill="#6f4fdf")
    d_ += 9*(simspeed*0.0001)
    ex = cos(e_)*152.1
    ey = -sin(e_)*152.1
    c.create_oval(ex-7+(size/2), ey-7+(size/2), ex+7+(size/2), ey+7+(size/2), fill="#bf7f3f")
    e_ += 6*(simspeed*0.0001)
    fx = cos(f_)*200.1
    fy = -sin(f_)*200.1
    c.create_oval(fx-7+(size/2), fy-7+(size/2), fx+7+(size/2), fy+7+(size/2), fill="#3f9fff")
    f_ += 4*(simspeed*0.0001)
    gx = cos(g_)*243.5
    gy = -sin(g_)*243.5
    c.create_oval(gx-7+(size/2), gy-7+(size/2), gx+7+(size/2), gy+7+(size/2), fill="#afffff")
    g_ += 3*(simspeed*0.0001)
    hx = cos(h_)*321.8
    hy = -sin(h_)*321.8
    c.create_oval(hx-7+(size/2), hy-7+(size/2), hx+7+(size/2), hy+7+(size/2), fill="#ffffff")
    h_ += 2*(simspeed*0.0001)
    if labels:
        if keplabels:
            c.create_text(size/2+10, size/2-10, anchor=SW, fill="#ff1f00", text="K2-112")
            c.create_text(bx+7+(size/2), by-7+(size/2), anchor=SW, fill="#00ff00", text="K2-112b")
            c.create_text(cx+7+(size/2), cy-7+(size/2), anchor=SW, fill="#ffbf00", text="K2-112c")
            c.create_text(dx+7+(size/2), dy-7+(size/2), anchor=SW, fill="#6f4fdf", text="K2-112d")
            c.create_text(ex+7+(size/2), ey-7+(size/2), anchor=SW, fill="#bf7f3f", text="K2-112e")
            c.create_text(fx+7+(size/2), fy-7+(size/2), anchor=SW, fill="#3f9fff", text="K2-112f")
            c.create_text(gx+7+(size/2), gy-7+(size/2), anchor=SW, fill="#afffff", text="K2-112g")
            c.create_text(hx+7+(size/2), hy-7+(size/2), anchor=SW, fill="#ffffff", text="K2-112h")
        else:
            c.create_text(size/2+10, size/2-10, anchor=SW, fill="#ff1f00", text="TRAPPIST-1")
            c.create_text(bx+7+(size/2), by-7+(size/2), anchor=SW, fill="#00ff00", text="TRAPPIST-1b")
            c.create_text(cx+7+(size/2), cy-7+(size/2), anchor=SW, fill="#ffbf00", text="TRAPPIST-1c")
            c.create_text(dx+7+(size/2), dy-7+(size/2), anchor=SW, fill="#6f4fdf", text="TRAPPIST-1d")
            c.create_text(ex+7+(size/2), ey-7+(size/2), anchor=SW, fill="#bf7f3f", text="TRAPPIST-1e")
            c.create_text(fx+7+(size/2), fy-7+(size/2), anchor=SW, fill="#3f9fff", text="TRAPPIST-1f")
            c.create_text(gx+7+(size/2), gy-7+(size/2), anchor=SW, fill="#afffff", text="TRAPPIST-1g")
            c.create_text(hx+7+(size/2), hy-7+(size/2), anchor=SW, fill="#ffffff", text="TRAPPIST-1h")
    tk.update()
