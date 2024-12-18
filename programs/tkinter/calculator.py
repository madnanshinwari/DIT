import tkinter as tk

# Function to update the input field
def on_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input field
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create buttons and add them to the grid
for text, row, col in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the application
root.mainloop()
