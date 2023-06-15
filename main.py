import tkinter as tk
import random

def generate_password():
    length = length_scale.get()
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()

    characters = ""

    if include_uppercase:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_lowercase:
        characters += "abcdefghijklmnopqrstuvwxyz"
    if include_digits:
        characters += "0123456789"
    if include_special_chars:
        characters += "!@#$%^&*()"

    if not characters:
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, "Please select at least one character type.")
        return

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create GUI
root = tk.Tk()
root.title("Password Generator")

# Length
length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
length_scale = tk.Scale(root, from_=4, to=30, orient="horizontal")
length_scale.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Character Types
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")
lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")
digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")
special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Password Entry
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
