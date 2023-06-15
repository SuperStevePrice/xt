#!/Users/steve/anaconda3/bin/python3.10

## Linux use: "#!/usr/bin/env python3".
## MacOS use: "#!/Users/steve/anaconda3/bin/python3.10"

#-------------------------------------------------------------------------------
#         Copyright (C) 2023    Steve Price    SuperStevePrice@gmail.com
#
#                       GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# PROGRAM:
#	xt.py
#	
# PURPOSE:
#   This Python program will create a dashboard to toggle rapid xterm creation.
#	
# FILES:
#   xtrc.py
#       Contains handlers for colors, xtrc, and xterm cmd data structures.
#
# USAGE:
#   xt.py
#
# VERSION:
#   MacOSX
#-------------------------------------------------------------------------------

import subprocess
import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkmacosx import Button as TkButton
import xtrc as xt
import locale 

# Get the system's default locale
system_locale = locale.getdefaultlocale()

# Set a fallback default locale if the system locale is None
fallback_locale = ('en_US', 'UTF-8')
if system_locale[0] is None:
    system_locale = fallback_locale

    # Set the locale based on the system's default locale
    locale.setlocale(locale.LC_ALL, system_locale)

    # Set the LC_ALL environment variable
    os.environ['LC_ALL'] = system_locale[0]  # Use only language part of locale

colors = xt.set_colors()
xtrc = xt.set_xtrc()

def on_button_click(bg_color, fg_color, custom_xterm):
    """
    Handle the spawning of xterm windows with desired attributes.

    Parameters
    ----------
    bg_color : TYPE
        DESCRIPTION.
    fg_color : TYPE
        DESCRIPTION.
    custom_xterm : BooleenVar
        True if Create Custom Xterm button pressed

    Returns
    -------
    click : TYPE
        DESCRIPTION.

    """

    def click():
        try:
            # Always use the current font size in entry box:
            xtrc['x_fs'] = entry_font_size.get()

            # If custome button pressed, use entry box color pair:
            if custom_xterm:
                xtrc['x_bg'] = entry_bg.get()
                xtrc['x_fg'] = entry_fg.get()
            else:
                xtrc['x_bg'] = bg_color
                xtrc['x_fg'] = fg_color

            cmd = xt.set_cmd(xtrc)
            
            #print("Button clicked!")
            #print(cmd)
            subprocess.Popen(cmd, shell=True)
        except Exception as exception:
            print("Error occurred while executing the command:", exception)

    return click


def toggle_logging():
    """
    Turn xterm logging on and off.

    Returns
    -------
    None.

    """
    #print("DEBUG: toggle_logging: x_log: ", xtrc['x_log'])
    
    if xtrc['x_log'] == 0:
        xtrc['x_log'] = 1
    else:
        xtrc['x_log'] = 0

    #print("DEBUG: toggle_logging: x_log: ", xtrc['x_log'])




def quit_application():
    """
    Gracefully quit the application and free all resources.
    """
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        if 'spyder' in sys.modules:
            os._exit(0)
        else:
            root.quit()

root = tk.Tk()
root.configure(bg='black')
root.geometry('400x700')
root.title('Color Buttons')


# Create a frame to hold the buttons grid
frame_buttons = tk.Frame(root, bg='black')
frame_buttons.pack(padx=10, pady=10, anchor=tk.CENTER)

# Calculate the number of rows and columns for the buttons grid
# Add 1 for the extra row if there are an odd number of buttons
NUM_ROWS = (len(colors) + 1) // 2
NUM_COLUMNS = 2

# Create the buttons grid
for i, color_pair in enumerate(colors):
    # Calculate the row and column indices
    row = i // NUM_COLUMNS
    column = i % NUM_COLUMNS

    button = TkButton(frame_buttons,
        text=f'Xterm Window {str(i + 1).zfill(2)}',
        bg=color_pair[0], fg=color_pair[1],
        activebackground="DarkGrey")
    button.configure(command=on_button_click(color_pair[0], 
        color_pair[1], False))
    button.grid(row=row, column=column, padx=4, pady=2, sticky=tk.EW)

# Create a frame to hold the additional elements
frame_additional = tk.Frame(root, bg='black')
frame_additional.pack(padx=10, pady=10, anchor=tk.CENTER)

# A: Foreground and Background entry labels and boxes
label_fg = tk.Label(frame_additional,
            text="Foreground:", foreground="DarkGrey", background="black")
label_fg.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_fg = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_fg']))
entry_fg.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

label_bg = tk.Label(frame_additional, text="Background:",
    foreground="DarkGrey", background="black")
label_bg.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
entry_bg = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_bg']))
entry_bg.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# B: Cols, Rows, Font size labels and inputs
label_cols = tk.Label(frame_additional, text="Cols:",
    foreground="DarkGrey", background="black")
label_cols.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
entry_cols = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_cols']))
entry_cols.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

label_rows = tk.Label(frame_additional, text="Rows:",
    foreground="DarkGrey", background="black")
label_rows.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
entry_rows = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_rows']))
entry_rows.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

label_font_size = tk.Label(frame_additional,
    text="Font Size:", foreground="DarkGrey", background="black")
label_font_size.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
entry_font_size = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_fs']))
entry_font_size.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

# C: Font Name entry box
label_font_name = tk.Label(frame_additional, text="Font Name:",
    foreground="DarkGrey", background="black")
label_font_name.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
entry_font_name = tk.Entry(
    frame_additional, textvariable=tk.StringVar(value=xtrc['x_fa']))
entry_font_name.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)


def populate_entry_boxes():
    """
    Fetch values from ~/.xtrc and populate input boxes.

    Returns
    -------
    None.

    """
    home = os.path.expanduser("~")
    xtrc_path = os.path.join(home, ".xtrc")

    if os.path.isfile(xtrc_path):
        with open(xtrc_path, 'r') as file:
            xtrc_data = file.read()
            xtrc_values = {}
            for item in xtrc_data.split('\n'):
                if item:
                    pair = item.split('=')
                    if len(pair) == 2:
                        xtrc_values[pair[0]] = pair[1]

        entry_fg.delete(0, tk.END)
        entry_fg.insert(0, xtrc_values.get('x_fg', ''))

        entry_bg.delete(0, tk.END)
        entry_bg.insert(0, xtrc_values.get('x_bg', ''))

        entry_cols.delete(0, tk.END)
        entry_cols.insert(0, xtrc_values.get('x_cols', ''))

        entry_rows.delete(0, tk.END)
        entry_rows.insert(0, xtrc_values.get('x_rows', ''))

        entry_font_size.delete(0, tk.END)
        entry_font_size.insert(0, xtrc_values.get('x_fs', ''))

        entry_font_name.delete(0, tk.END)
        entry_font_name.insert(0, xtrc_values.get('x_fa', ''))


# Call the function to populate the entry boxes
populate_entry_boxes()

# E: Enable Logging check box
checkbox_logging = tk.Checkbutton(frame_additional,
    text="Enable Logging", foreground="DarkGrey", background="black",
    command=toggle_logging)
checkbox_logging.grid(row=7, column=0, columnspan=2,
    padx=5, pady=5, sticky=tk.N)


# F: Create Custom Font button
button_create_custom_xterm = TkButton(frame_additional,
    text="Create Custom Xterm",
    command=on_button_click(entry_bg.get(), entry_bg.get(), True),
        background=entry_bg.get(), foreground=entry_fg.get())
button_create_custom_xterm.grid(
    row=8, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W + tk.E)

# Create a frame to hold the Quit button
frame_quit = tk.Frame(root, bg='black')
frame_quit.pack(padx=10, pady=10, anchor=tk.CENTER)

# G: Quit button
button_quit = tk.Button(frame_quit, text="Quit", command=quit_application,
                        bg="lightSteelBlue", fg="red")
button_quit.pack(padx=5, pady=5, anchor=tk.CENTER)

root.mainloop()
