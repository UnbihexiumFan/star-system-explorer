from tkinter import *
from math import sin, cos, pi
from random import uniform

import webbrowser
import os

size = 800

tk = Tk()
tk.title("Star System Explorer")
c = Canvas(tk, width=size, height=size, bg="#000000")
c.pack()

# File path
path = os.path.dirname(os.path.realpath(__file__))

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

def music_off():
	webbrowser.open(path+"/silence.wav")

def music_on():
	webbrowser.open(path+"/music.mp3")

sdown = Button(tk, text="Slow Down", command=speeddown)
sdown.place(anchor=NW, x=5, y=5)
sup = Button(tk, text="Speed Up", command=speedup)
sup.place(anchor=NW, x=5, y=35)
clab = Button(tk, text="Toggle Kepler/TRAPPIST Labels", command=change_labels)
clab.place(anchor=NW, x=5, y=65)
tlab = Button(tk, text="Toggle Labels", command=toggle_labels)
tlab.place(anchor=NW, x=5, y=95)

# Music Buttons

musoff = Button(tk, text="Turn Music Off", command=music_off)
musoff.place(anchor=SW, x=5, y=size-35)
muson = Button(tk, text="Turn Music On", command=music_on)
muson.place(anchor=SW, x=5, y=size-5)

# Play Music

webbrowser.open(path+"/music.mp3")

# Help

screenon = False
screentext = None

def help_(event):
	global screenon
	global screentext
	screenon = True
	screentext = "SELECTION:\nHold \"Return\" to select\nArrow keys to cycle\nobjects"

c.bind_all("<KeyPress-h>", help_)

# Selecting Object

selobj = 0

def select(event):
	global screenon
	global screentext
	screenon = True
	if selobj == 0:
		screentext = "TRAPPIST-1 is a red\ndwarf star that can not\nbe seen with the naked\neye."
	elif selobj == 1:
		screentext = "TRAPPIST-1b is a planet\nin the TRAPPIST-1 system.\nIt is likely covered\nwith haze."
	elif selobj == 2:
		screentext = "TRAPPIST-1c is a planet\nin the TRAPPIST-1 system.\nIt is likely covered\nwith haze."
	elif selobj == 3:
		screentext = "TRAPPIST-1d is a planet\nin the TRAPPIST-1 system.\nIt is a waterworld has a\nmildly thick atmosphere."
	elif selobj == 4:
		screentext = "TRAPPIST-1e is a planet\nin the TRAPPIST-1 system.\nIt likely has an\nEarth-like composition\nand a habitable\ntemperature."
	elif selobj == 5:
		screentext = "TRAPPIST-1f is a planet\nin the TRAPPIST-1 system.\nIt is a waterworld which\nis likely very hot with\na mostly steam atmosphere."
	elif selobj == 6:
		screentext = "TRAPPIST-1g is a planet\nin the TRAPPIST-1 system.\nIt is a waterworld which\nis likely very hot with\na thick oxygen atmosphere."
	elif selobj == 7:
		screentext = "TRAPPIST-1h is a planet\nin the TRAPPIST-1 system.\nIt has a thick ice shell\nsurrounding it."

def selnext(event):
	global selobj
	selobj += 1
	if selobj > 7:
		selobj = 0

def selprev(event):
	global selobj
	selobj -= 1
	if selobj < 0:
		selobj = 7

def deselect(event):
	global screenon
	screenon = False

c.bind_all("<KeyPress-Return>", select)
c.bind_all("<KeyRelease-Return>", deselect)
c.bind_all("<KeyRelease-h>", deselect)
c.bind_all("<KeyPress-Left>", selprev)
c.bind_all("<KeyPress-Right>", selnext)

## Simulation

running = True

def run_sim():
	global simspeed
	
	b_ = 0
	c_ = 0
	d_ = 0
	e_ = uniform(0, 2*pi)
	f_ = uniform(0, 2*pi)
	g_ = uniform(0, 2*pi)
	h_ = uniform(0, 2*pi)
	
	simspeed = 1.0
	
	while running:
		c.delete("all")
		if simspeed == 0.00003472:
			c.create_text(size-5, 5, anchor=NE, text="Speed: REAL TIME", fill="#ffffff")
		elif simspeed < 0.5:
			c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{str(round(simspeed, 2)).ljust(4, '0')}", fill="#ffffff")
		elif simspeed < 10:
			c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{round(simspeed, 1)}", fill="#ffffff")
		else:
			c.create_text(size-5, 5, anchor=NE, text=f"Speed: x{round(simspeed, 0)}", fill="#ffffff")
		c.create_text(size-5, 25, anchor=NE, text=f"Hold \"H\" for help", fill="#ffffff")
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
		if selobj == 0:
			c.create_oval(size/2-12, size/2-12, size/2+12, size/2+12, outline = "#ffffff")
		elif selobj == 1:
			c.create_oval(bx-9+(size/2), by-9+(size/2), bx+9+(size/2), by+9+(size/2), outline="#ffffff")
		elif selobj == 2:
			c.create_oval(cx-9+(size/2), cy-9+(size/2), cx+9+(size/2), cy+9+(size/2), outline="#ffffff")
		elif selobj == 3:
			c.create_oval(dx-9+(size/2), dy-9+(size/2), dx+9+(size/2), dy+9+(size/2), outline="#ffffff")
		elif selobj == 4:
			c.create_oval(ex-9+(size/2), ey-9+(size/2), ex+9+(size/2), ey+9+(size/2), outline="#ffffff")
		elif selobj == 5:
			c.create_oval(fx-9+(size/2), fy-9+(size/2), fx+9+(size/2), fy+9+(size/2), outline="#ffffff")
		elif selobj == 6:
			c.create_oval(gx-9+(size/2), gy-9+(size/2), gx+9+(size/2), gy+9+(size/2), outline="#ffffff")
		elif selobj == 7:
			c.create_oval(hx-9+(size/2), hy-9+(size/2), hx+9+(size/2), hy+9+(size/2), outline="#ffffff")
		if screenon:
			c.create_rectangle(size-300, 10, size-10, 200, outline="#ffffff", fill="#000000")
			c.create_text(size-290, 20, anchor=NW, fill="#ffffff", text=screentext)
		tk.update()

run_sim()
