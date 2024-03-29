from tkinter import Tk, Button, Entry

def button_click(number):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert('end', str(current) + str(number))

def button_clear():
    entry.delete(0, 'end')

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, 'end')
        entry.insert('end', str(result))
    except:
        entry.delete(0, 'end')
        entry.insert('end', "Error")

# Create the main window
root = Tk()
root.title("Calculator")

# Create an entry widget to display the numbers and results
entry = Entry(root, width=25, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))

# Create the operation buttons
button_add = Button(root, text="+", padx=19, pady=10, command=lambda: button_click("+"))
button_subtract = Button(root, text="-", padx=20, pady=10, command=lambda: button_click("-"))
button_multiply = Button(root, text="*", padx=20, pady=10, command=lambda: button_click("*"))
button_divide = Button(root, text="/", padx=20, pady=10, command=lambda: button_click("/"))

# Create the special buttons
button_clear = Button(root, text="C", padx=19, pady=10, command=button_clear)
button_equal = Button(root, text="=", padx=20, pady=10, command=button_equal)

# Arrange the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

# Run the main loop
root.mainloop()
