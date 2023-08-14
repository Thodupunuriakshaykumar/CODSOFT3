import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

def create_button(root, text, row, col, width=20, height=3, bg="light grey", command=None):
    return tk.Button(root, text=text, width=width, height=height, bg=bg, command=command).grid(row=row, column=col)

# Create the main window
root = tk.Tk()
root.title("simpul Calculator")

# Entry widget to display the result
entry = tk.Entry(root, width=25, font=('Arial', 20), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and arithmetic operations
create_button(root, "1", 1, 0, command=lambda: button_click(1))
create_button(root, "2", 1, 1, command=lambda: button_click(2))
create_button(root, "3", 1, 2, command=lambda: button_click(3))
create_button(root, "4", 2, 0, command=lambda: button_click(4))
create_button(root, "5", 2, 1, command=lambda: button_click(5))
create_button(root, "6", 2, 2, command=lambda: button_click(6))
create_button(root, "7", 3, 0, command=lambda: button_click(7))
create_button(root, "8", 3, 1, command=lambda: button_click(8))
create_button(root, "9", 3, 2, command=lambda: button_click(9))
create_button(root, "0", 4, 1, bg="#808080", command=lambda: button_click(0))
create_button(root, "+", 1, 3, bg="#FF6200", command=lambda: button_click('+'))
create_button(root, "-", 2, 3, bg="#FF6200", command=lambda: button_click('-'))
create_button(root, "*", 3, 3, bg="#FF6200", command=lambda: button_click('*'))
create_button(root, "/", 4, 3, bg="#FF6200", command=lambda: button_click('/'))
create_button(root, "=", 4, 2, bg="#808080", command=calculate)
create_button(root, "C", 4, 0, bg="#808080", command=clear)

# Run the main event loop
root.mainloop()
