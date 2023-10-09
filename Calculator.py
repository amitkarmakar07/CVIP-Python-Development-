import tkinter as tk

# function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# function to clear the input field
def clear():
    entry.delete(0, tk.END)

# function to perform arithmetic operations
def perform_operation():
    try:
        current = entry.get()
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 20),
                  command=lambda b=button: button_click(b) if b != '=' else perform_operation()).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
