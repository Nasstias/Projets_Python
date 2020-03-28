from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=400)

tk.title("Dessin")
canvas.pack()

canvas.create_line(0, 0, 500, 400)
canvas.create_rectangle( 100, 100, 300, 300, fill="blue")
canvas.create_rectangle( 150, 150, 300, 300, fill="dark blue")
canvas.create_rectangle( 200, 200, 300, 300, fill="light blue")
canvas.create_oval( 200, 300, 300,400, fill="yellow")
canvas.create_polygon( 400, 10, 300, 300, 400, 300, fill="#7FFF00")
canvas.mainloop()
