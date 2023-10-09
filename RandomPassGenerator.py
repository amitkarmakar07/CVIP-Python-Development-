import tkinter as tk
import random
import string

# function to generate a random password based on user input
def generate_password():
    try:
        password_length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
    except ValueError:
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, "Invalid Length")

root = tk.Tk()
root.title("Password Generator")

password_entry = tk.Entry(root, width=20, font=("Arial", 16))
password_entry.grid(row=0, column=0, columnspan=2)


length_label = tk.Label(root, text="Password Length:", font=("Arial", 14))
length_label.grid(row=1, column=0)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.grid(row=1, column=1)


generate_button = tk.Button(root, text="Generate Password", padx=20, pady=10, font=("Arial", 12), command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
