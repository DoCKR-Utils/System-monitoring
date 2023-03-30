import psutil
import os
import tkinter as tk
from tkinter import ttk

def show_monitor():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    monitor_output.config(text=f"CPU usage: {cpu_usage}%\n"
                                f"Memory usage: {memory_usage}%\n"
                                f"Disk usage: {disk_usage}%\n")

    io_counters = psutil.net_io_counters(pernic=True)
    io_string = ""
    for interface, counters in io_counters.items():
        io_string += f"Interface {interface}:\n"
        io_string += f"  bytes sent: {counters.bytes_sent}\n"
        io_string += f"  bytes received: {counters.bytes_recv}\n"

    network_output.config(text=io_string)

def show_files():
    files = []

    for file_name in os.listdir(os.getcwd()):
        file_info = {
            "name": file_name,
            "size": os.path.getsize(file_name),
        }
        files.append(file_info)

    # create listbox to display files
    files_listbox = tk.Listbox(folders_frame, height=10, width=40)
    files_listbox.pack()

    # insert file names into listbox
    for file in files:
        files_listbox.insert(tk.END, file['name'])

root = tk.Tk()
root.title("System Monitor")

#configure style
style = ttk.Style()
style.theme_use('clam')

style.configure('Title.TLabel', foreground='white', background='#263238', font=("Arial", 16, "bold"))
style.configure('Main.TFrame', foreground='white', background='#263238')
style.configure('Main.TLabel', foreground='white', background='#546e7a', font=("Arial", 12))
style.configure('Button.TButton', foreground='#263238', background='#eceff1', font=("Arial", 10, "bold"))
style.configure('Output.TLabel', foreground='#263238', background='#eceff1', font=("Arial", 10))

#create title frame
title_frame = ttk.Frame(root, style='Main.TFrame')
title_frame.pack(fill=tk.X, padx=10, pady=10)

title_label = ttk.Label(title_frame, text="System Monitor", style='Title.TLabel')
title_label.pack(fill=tk.X, pady=10)

#create monitor frame
monitor_frame = ttk.Frame(root, style='Main.TFrame')
monitor_frame.pack(side=tk.LEFT, padx=10, pady=10)

monitor_label = ttk.Label(monitor_frame, text="System Resources", style='Main.TLabel')
monitor_label.pack(pady=10)

#create monitor output labels
monitor_output = ttk.Label(monitor_frame, style='Output.TLabel')
monitor_output.pack(pady=10)

network_label = ttk.Label(monitor_frame, text="Network Activity", style='Main.TLabel')
network_label.pack(pady=10)

network_output = ttk.Label(monitor_frame, style='Output.TLabel')
network_output.pack(pady=10)

#create folders frame
folders_frame = ttk.Frame(root, style='Main.TFrame')
folders_frame.pack(side=tk.RIGHT, padx=10, pady=10)

folders_label = ttk.Label(folders_frame, text="Folder Sizes", style='Main.TLabel')
folders_label.pack(pady=10)

#create buttons for showing files
files_button = ttk.Button(folders_frame, text="Show Files", style='Button.TButton', command=show_files)
files_button.pack()

#create label and listbox for displaying folders/files
folders_output = ttk.Label(folders_frame, style='Output.TLabel', font=("Arial", 10), wraplength=200)
folders_output.pack(pady=10)

monitor_button = ttk.Button(root, text="Show System Resources", style='Button.TButton', command=show_monitor)
monitor_button.pack(side=tk.BOTTOM, pady=(0, 10))

#add separator
ttk.Separator(root).pack(fill=tk.X, padx=10, pady=5)

root.mainloop()
