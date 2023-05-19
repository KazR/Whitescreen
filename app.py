import tkinter as tk


# Create the main application window
window = tk.Tk()
# Set the window title
window.title("Blank Window")
# Set the window size
window.geometry("400x300")
# Set the background color to white
window.configure(bg="white")

def toggle_fullscreen():
    state = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not state)

FullscreenButton = tk.Button(window, text="Toggle Fullscreen", command=toggle_fullscreen)

# Position the button at the bottom right

def packs():
    FullscreenButton.pack(side="bottom", padx=10, pady=10)
# Run the application main loop
packs()
window.mainloop()
