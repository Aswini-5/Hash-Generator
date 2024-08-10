import tkinter as tk
from tkinter import ttk, messagebox
import hashlib

def hash_string(input_string, algorithm):
    try:
        hash_object = hashlib.new(algorithm)
        hash_object.update(input_string.encode())
        return hash_object.hexdigest()
    except ValueError:
        return "Invalid algorithm"

def generate_hash():
    target_string = hash_entry.get()
    algorithm = algorithm_combobox.get()
    if not target_string:
        messagebox.showwarning("Input Error", "Please enter a string to hash.")
        return
    result = hash_string(target_string, algorithm)
    result_label.config(text=f"Generated hash: {result}")

def clear_fields():
    hash_entry.delete(0, tk.END)
    result_label.config(text="")

def copy_to_clipboard():
    result = result_label.cget("text")
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Hash value copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Hash Cracker")
root.geometry("400x250")

# Create UI elements
tk.Label(root, text="Enter string to hash:").pack(pady=10)
hash_entry = tk.Entry(root, width=50)
hash_entry.pack()

tk.Label(root, text="Choose hashing algorithm:").pack(pady=10)
algorithm_combobox = ttk.Combobox(root, values=[
    "md5", "sha1", "sha224", "sha256", "sha384", "sha512"
])
algorithm_combobox.pack()
algorithm_combobox.set("md5")

generate_button = tk.Button(root, text="Generate Hash", command=generate_hash)
generate_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

result_label = tk.Label(root, text="", wraplength=350)
result_label.pack(pady=20)

# Run the application
root.mainloop()
