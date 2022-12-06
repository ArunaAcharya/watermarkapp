from tkinter import *
from PIL import Image


root = Tk()
root.title("Game")


frame = Frame(root)
frame.pack()


canvas = Canvas(frame, bg="black", width=700, height=400)
canvas.pack()


background = PhotoImage(file="favicon-0.png")
canvas.create_image(20,20,image=background)

character = PhotoImage(file="tkbg.png")
canvas.create_image(30,30,image=character)

root.mainloop()