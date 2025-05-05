import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("400x250")
root.configure(bg="#1e1e2f")  # Dark background

# Global variables
running = False
counter = 0

# Header Label
title = tk.Label(root, text="⏱️ Stopwatch Timer", font=("Helvetica", 20, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=10)

# Stopwatch Display Label
label = tk.Label(
    root,
    text="00:00:00",
    font=("Helvetica", 48, "bold"),
    bg="#1e1e2f",
    fg="#00FFCC",  # Neon Cyan
)
label.pack(pady=15)

# Stopwatch logic
def update_stopwatch():
    global counter
    if running:
        minutes, seconds = divmod(counter, 60)
        hours, minutes = divmod(minutes, 60)
        label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        counter += 1
        root.after(1000, update_stopwatch)

def start():
    global running
    if not running:
        running = True
        update_stopwatch()

def stop():
    global running
    running = False

def reset():
    global counter
    counter = 0
    label.config(text="00:00:00")

# Button Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

# Stylish Buttons
style = {
    "font": ("Helvetica", 12, "bold"),
    "width": 10,
    "padx": 5,
    "pady": 5,
    "bd": 0,
}

start_btn = tk.Button(btn_frame, text="▶ Start", command=start, bg="#28a745", fg="white", **style)
stop_btn = tk.Button(btn_frame, text="⏸ Stop", command=stop, bg="#dc3545", fg="white", **style)
reset_btn = tk.Button(btn_frame, text="🔁 Reset", command=reset, bg="#ffc107", fg="black", **style)

# Pack buttons with spacing
start_btn.grid(row=0, column=0, padx=10)
stop_btn.grid(row=0, column=1, padx=10)
reset_btn.grid(row=0, column=2, padx=10)

# Run the app
root.mainloop()
