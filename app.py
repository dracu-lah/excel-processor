import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def process_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

    if not file_path:
        return

    df = pd.read_excel(file_path)

    # Display column options
    column_names = list(df.columns)

    # Check duplicates based on user input (example: email or phone)
    selected_columns = ["email", "phone"]  # Modify based on user selection

    duplicated_rows = df[df.duplicated(subset=selected_columns, keep=False)]
    unique_rows = df.drop(duplicated_rows.index)

    # Save results
    output_dir = os.path.join(os.path.dirname(file_path), "output")
    os.makedirs(output_dir, exist_ok=True)

    duplicated_rows.to_excel(
        os.path.join(output_dir, "duplicated_rows.xlsx"), index=False
    )
    unique_rows.to_excel(os.path.join(output_dir, "unique_rows.xlsx"), index=False)

    messagebox.showinfo("Success", f"Files saved in {output_dir}")


# GUI Setup
root = tk.Tk()
root.title("Excel Processor")

button = tk.Button(root, text="Select Excel File", command=process_excel)
button.pack(pady=20)

root.mainloop()
