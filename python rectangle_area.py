import tkinter as tk

# Function to calculate area
def calculate_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    result_label.config(text="Area: " + str(area))

# Create main window
window = tk.Tk()
window.title("Rectangle Area Calculator")

# Create and place widgets
length_label = tk.Label(window, text="Length:")
length_label.pack()

length_entry = tk.Entry(window)
length_entry.pack()

width_label = tk.Label(window, text="Width:")
width_label.pack()

width_entry = tk.Entry(window)
width_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_area)
calculate_button.pack()

result_label = tk.Label(window, text="Area:")
result_label.pack()

# Start event loop
window.mainloop()