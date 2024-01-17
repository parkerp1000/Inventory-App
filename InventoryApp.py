import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import csv
import os

csv_file_path = None

def submit_data(event=None):
    global csv_file_path  # Declare as global to remember the file path between function calls

    model = model_entry.get()
    serial_number = serial_number_entry.get()
    device_type = type_entry.get()
    quantity = quantity_entry.get()

    if not model or not serial_number or not device_type or not quantity:
        error_label.config(text="All fields are mandatory")
        return

    if csv_file_path is None:
        # Ask for file location only the first time
        csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

        if not csv_file_path:
            error_label.config(text="Save path not selected")
            return

        # Create the CSV file with header if it doesn't exist
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Model", "Serial Number", "Type", "Quantity"])

    with open(csv_file_path, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([model, serial_number, device_type, quantity])

    model_entry.delete(0, tk.END)
    serial_number_entry.delete(0, tk.END)
    type_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    error_label.config(text="Data added successfully")

# Create main window
root = tk.Tk()
root.title("CSV Data Entry")

# Create and place widgets
model_label = ttk.Label(root, text="Model:")
model_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

model_entry = ttk.Entry(root)
model_entry.grid(row=0, column=1, padx=10, pady=10)
model_entry.bind("<Return>", submit_data)  # Bind Enter key to submit_data

serial_number_label = ttk.Label(root, text="Serial Number:")
serial_number_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

serial_number_entry = ttk.Entry(root)
serial_number_entry.grid(row=1, column=1, padx=10, pady=10)
serial_number_entry.bind("<Return>", submit_data)  # Bind Enter key to submit_data

type_label = ttk.Label(root, text="Type:")
type_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

type_entry = ttk.Entry(root)
type_entry.grid(row=2, column=1, padx=10, pady=10)
type_entry.bind("<Return>", submit_data)  # Bind Enter key to submit_data

quantity_label = ttk.Label(root, text="Quantity:")
quantity_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=3, column=1, padx=10, pady=10)
quantity_entry.bind("<Return>", submit_data)  # Bind Enter key to submit_data

submit_button = ttk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

error_label = ttk.Label(root, text="", foreground="red")
error_label.grid(row=5, column=0, columnspan=2)

# Run the main loop
root.mainloop()
