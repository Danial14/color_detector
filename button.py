from turtle import Screen
from tkinter import *
from open_file import openFile


screen = Screen()
width, height = (600, 400)
screen.setup(width=width, height=height)

canvas = screen.getcanvas()
button = Button(canvas.master, text="Choose Image", command=openFile)
#button.pack()
button.place(x=width / 2, y=height / 2)  # Place the button anywhere on the screen

screen.exitonclick()