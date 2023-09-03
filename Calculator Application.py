import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = display_var.get()
    display_var.set(current + str(number))

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to perform calculations
def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
    except:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Create a variable to store the input and display it in a Label
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24))
display.grid(row=0, column=0, columnspan=4)

# Define button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

# Create and place the buttons on the grid
row = 1
col = 0
for button_label in buttons:
    tk.Button(
        root, 
        text=button_label, 
        padx=20, 
        pady=20, 
        font=("Arial", 18),
        bg="lightblue",
        command=lambda label=button_label: button_click(label) if label != '=' else calculate()
    ).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create and place a clear button
tk.Button(
    root, 
    text='C', 
    padx=20, 
    pady=20, 
    font=("Arial", 18),
    bg="red",
    command=clear_display
).grid(row=row, column=col)

# Run the GUI
root.mainloop()
