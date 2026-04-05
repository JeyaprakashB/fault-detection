import customtkinter as ctk
import random
import matplotlib.pyplot as plt

# Theme setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Data for graph
voltage_data = []
current_data = []

# Fault logic
def detect_fault(v, i):
    if v < 50 and i > 15:
        return "⚠ Short Circuit","very low voltage and very high current-> direct connection"
    elif i > 10:
        return "⚠ Overcurrent","current exceeds safe limit->overload condition"
    elif v < 200:
        return "⚠ Undervoltage","voltage is below normal->supply issue or heavy load."
    else:
        return "✅ Normal","system is operating safely within limits."

# Check fault
def check_fault():
    try:
        v = float(voltage_entry.get())
        i = float(current_entry.get())

        voltage_data.append(v)
        current_data.append(i)

        result = detect_fault(v, i)

        if "Normal" in result:
            status_label.configure(text=result, text_color="green")
        else:
            status_label.configure(text=result, text_color="red")

    except:
        status_label.configure(text="Invalid Input", text_color="orange")

# Auto input
def auto_input():
    v = random.randint(30, 250)
    i = random.randint(1, 20)

    voltage_entry.delete(0, "end")
    current_entry.delete(0, "end")

    voltage_entry.insert(0, str(v))
    current_entry.insert(0, str(i))

# Graph
def show_graph():
    if len(voltage_data) == 0:
        return

    plt.plot(voltage_data, label="Voltage")
    plt.plot(current_data, label="Current")
    plt.legend()
    plt.title("System Monitoring")
    plt.show()

# App window
app = ctk.CTk()
app.title("⚡ Fault Detection System")
app.geometry("450x420")

# Title
title = ctk.CTkLabel(app, text="Fault Detection System", font=("Arial", 20, "bold"))
title.pack(pady=15)

# Voltage
voltage_entry = ctk.CTkEntry(app, placeholder_text="Enter Voltage (V)")
voltage_entry.pack(pady=10)

# Current
current_entry = ctk.CTkEntry(app, placeholder_text="Enter Current (A)")
current_entry.pack(pady=10)

# Buttons
check_btn = ctk.CTkButton(app, text="Check Fault", command=check_fault)
check_btn.pack(pady=10)

auto_btn = ctk.CTkButton(app, text="Auto Input", command=auto_input)
auto_btn.pack(pady=5)

graph_btn = ctk.CTkButton(app, text="Show Graph", command=show_graph)
graph_btn.pack(pady=5)

# Status
status_label = ctk.CTkLabel(app, text="Status: ---", font=("Arial", 16))
status_label.pack(pady=20)

# Run
app.mainloop()
