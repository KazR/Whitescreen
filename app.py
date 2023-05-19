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

def change_background_color(color):
    window.configure(bg=color)

FullscreenButton = tk.Button(window, text="Toggle Fullscreen", command=toggle_fullscreen)
FullscreenButton.pack(side="bottom", padx=10, pady=10)

# Create the color selection dropdown menu
color_dropdown = tk.StringVar(window)
color_dropdown.set("White")  # Set the default color

def on_color_selected(*args):
    selected_color = color_dropdown.get()
    if selected_color == "Natural Light":
        change_background_color("#FAF9F6")  # Light creamy white
    elif selected_color == "Soft Glow":
        change_background_color("#FDF7E3")  # Soft yellowish white
    elif selected_color == "Moonlight":
        change_background_color("#F2F3F4")  # Light grayish white
    elif selected_color == "Daybreak":
        change_background_color("#F5F5F5")  # Bright white
    elif selected_color == "Pure White":
        change_background_color("white")
    elif selected_color == "Ivory":
        change_background_color("#FFFFF0")  # Pale yellowish white
    elif selected_color == "Snow":
        change_background_color("#FFFAFA")  # White with a hint of pink
    elif selected_color == "Pearl":
        change_background_color("#FDEEF4")  # Pinkish white

color_options = ["White", "Natural Light", "Soft Glow", "Moonlight", "Daybreak", "Pure White", "Ivory", "Snow", "Pearl"]
color_dropdown_menu = tk.OptionMenu(window, color_dropdown, *color_options, command=on_color_selected)
color_dropdown_menu.config(direction="right")  # Set the dropdown menu to open on the right
color_dropdown_menu.pack(side="bottom", padx=10, pady=10)

# Run the application main loop
window.mainloop()
