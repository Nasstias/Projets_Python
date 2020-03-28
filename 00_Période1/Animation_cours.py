from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Animation")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
carre= canvas.create_rectangle(10, 10, 60, 60, fill="orange")

for i in range(400):
    canvas.move(ball, 1, 0)
    canvas.move(carre, 0,1 )
    tk.update()
    time.sleep(0.01)
