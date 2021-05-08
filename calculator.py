from tkinter import *

# CREATING ROOT WINDOW
root = Tk()

# ROOT WINDOW SETTING
root.title("CALCULATOR")

# WIDGETS
text_input = StringVar()
text_display = Entry(root, font=("arial", 20, "bold"), textvariable=text_input, bd=30, insertwidth=4,
                     bg="powder blue", justify="right").grid(columnspan=4)

# LAUNCHING
root.mainloop()
