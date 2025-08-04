import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Length should be at least 4")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")


tk.Label(root, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()


tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)


tk.Label(root, text="Generated Password:").pack(pady=5)
result_entry = tk.Entry(root, width=40)
result_entry.pack()


root.mainloop()