#!/usr/bin/env python

import time
import subprocess
import os
import tkinter as tk


def set_globals():
    global x_cols
    global x_rows
    global x_sl
    global x_bg
    global x_fg
    global x_fa
    global x_fs
    global x_log
    global entry_cols
    global frame
    global frame_types
    global top
    global entry_font
    global entry_font_size

    entry_cols = define_entries()

    # Read the .xtrc or ~/.xtrc file
    try:
        with open('.xtrc', 'r') as file:
            config_lines = file.readlines()
        except FileNotFoundError:
            try:
                with open(os.path.expanduser('~/.xtrc'), 'r') as file:
                    config_lines = file.readlines()
                except FileNotFoundError:
                    print("No .xtrc or ~/.xtrc file found.")
                    return

                # Parse the configuration lines
                for line in config_lines:
                    line = line.strip()
                    if line.startswith('#'):
                        continue
                    if line.startswith('x_cols'):
                        x_cols = line.split( '=')[1].strip()
                        elif line.startswith('x_rows'):
                            x_rows = line.split( '=')[1].strip()
                        elif line.startswith('x_sl'):
                            x_sl = line.split( '=')[1].strip()
                        elif line.startswith('x_fa'):
                            x_fa = line.split( '=')[1].strip().replace(' ', '')
                        elif line.startswith('x_fs'):
                            x_fs = line.split( '=')[1].strip()
                        elif line.startswith('x_log'):
                            x_log = int( line.split('=')[1].strip())

                    # Update the entry fields with the parsed values
                    try:
                        entry_cols.delete( 0, tk.END)
                        entry_cols.insert( 0, x_cols)
                        entry_rows.delete( 0, tk.END)
                        entry_rows.insert( 0, x_rows)
                        entry_font_size.delete( 0, tk.END)
                        entry_font_size.insert( 0, x_sl)
                        entry_font.delete( 0, tk.END)
                        entry_font.insert( 0, x_fa)

                        var_log.set( x_log) except NameError as e:
                            print( "Error:", e)


    def Xterm(x_bg, x_fg):
    # Snatch the date from the scalar localtime():
    date = time.strftime('%c')

    # Create a window title from $env(LOGNAME), $host, and date:
    title = f"{os.environ['LOGNAME']}@{'HOST'}   {date}"

    # Create a geometry setting from columns and rows:
    x_geo = f"{x_cols}x{x_rows}"

        cmd = f"nohup /usr/bin/env xterm -ls -sb -sl {x_sl}"

        if x_fa:
            cmd += f" -fa \"{x_fa}\""

        if x_fs:
            cmd += f" -fs \"{x_fs}\""

        if not x_fa:
            # Parsing failed. Use fallback font.
            cmd += " -fa \"9x15bold\""

        if not x_fs:
            # Parsing failed. Use fallback font.
            cmd += " -fa 16"

        cmd += f" -geometry {x_geo} -fg {x_fg} -bg {x_bg} -title \"{title}\""
        cmd += " -l" if x_log else ""

# Uncomment the line below to debug the cmd:
# print(f"DEBUG: cmd={cmd}")

subprocess.Popen(cmd, shell=True)


def create_specific_Xterm_buttons():
colors = [
    ("grey", "black"),
    ("LightSteelBlue", "navy"),
    ("CadetBlue", "white"),
    ("CadetBlue", "black"),
    ("blue", "white"),
    ("navy", "white"),
    ("navy", "orange"),
    ("navy", "yellow"),
    ("DarkGreen", "white"),
        ("DarkSeaGreen", "black"),
        ("DarkRed", "white"),
        ("salmon", "black"),
        ("SaddleBrown", "white"),
        ("tan", "black"),
        ("LightYellow", "black"),
        ("black", "lightSteelBlue")
    ]

    frame_idx = 0
    button_idx = 0
    last_frame_idx = 0
    button = []

    for idx, (bg, fg) in enumerate(colors):
        leading_zero = "0" if idx + 1 <= 9 else ""
        button_text = f"Xterm Window {leading_zero}{idx + 1}"

        if idx % 2 == 0:
            frame_idx += 1

        if last_frame_idx < frame_idx:
            frame[frame_idx] = tk.Frame()
            frame[frame_idx].pack(side="top", fill="y")
            frame[frame_idx].configure(borderwidth=2, background="black")
            last_frame_idx = frame_idx

        button.append(tk.Button(frame[frame_idx], text=button_text, command=lambda bg=bg, fg=fg: Xterm(
            bg, fg), borderwidth=5, padx=5, pady=5, background=bg, foreground=fg))
        button[button_idx].pack(side="left")
        button_idx += 1


def define_frames():
    global frame
    frame_types = ["colors", "sizes", "font", "font_button",
                   "log", "custom_button", "quit_button"]
    frame = {}

    for frame_type in frame_types:
        frame[frame_type] = tk.Frame()
        frame[frame_type].pack(side="top", fill="y")
        frame[frame_type].configure(borderwidth=5, background="black")


def define_entries():

    # Foreground Entry
    global entry_fg
    entry_fg = tk.Entry(frame["colors"], width=10)
    entry_fg.insert(0, "black")
    entry_fg.pack(side="left")

    # Background Entry
    global entry_bg
    entry_bg = tk.Entry(frame["colors"], width=10)
    entry_bg.insert(0, "grey")
    entry_bg.pack(side="left")

    # Font Entry
    global entry_font
    entry_font = tk.Entry(frame["font"], width=30)
    entry_font.insert(0, "9x15bold")
    entry_font.pack(side="left")

    # Font Size Entry
    global entry_font_size
    entry_font_size = tk.Entry(frame["sizes"], width=5)
    entry_font_size.insert(0, "16")
    entry_font_size.pack(side="left")


def set_geometry():
    global x_rows
    global x_cols

    x_rows = entry_rows.get()
    x_cols = entry_cols.get()


def set_font_attributes():
    global x_fa
    global x_fs

    x_fa = entry_font.get()
    x_fs = entry_font_size.get()


def set_log_var():
    global x_log

    x_log = var_log.get()


def destroy_window():
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("XTerm Command Central")
    define_frames()
    define_entries()

    # Rows
    frame_rows = tk.Frame()
    frame_rows.pack(side="top", fill="y")
    frame_rows.configure(borderwidth=5, background="black")

    label_rows = tk.Label(frame_rows, text="Rows:")
    label_rows.pack(side="left")

    global entry_rows
    entry_rows = tk.Entry(frame_rows, width=5)
    entry_rows.insert(0, "24")
    entry_rows.pack(side="left")

    # Columns
    frame_cols = tk.Frame()
    frame_cols.pack(side="top", fill="y")
    frame_cols.configure(borderwidth=5, background="black")

    label_cols = tk.Label(frame_cols, text="Columns:")
    label_cols.pack(side="left")

    global entry_cols
    entry_cols = tk.Entry(frame_cols, width=5)
    entry_cols.insert(0, "80")
    entry_cols.pack(side="left")

    # Font Button
    button_font = tk.Button(frame["font_button"], text="Set Font",
                            command=set_font_attributes, padx=5, pady=5)
    button_font.pack(side="left")

    # Log Checkbox
    global var_log
    var_log = tk.IntVar()
    checkbox_log = tk.Checkbutton(
        frame["log"], text="Log Session", variable=var_log, command=set_log_var)
    checkbox_log.pack(side="left")

    # Custom Button
    button_custom = tk.Button(frame["custom_button"], text="Create Custom Xterm", command=lambda: Xterm(
        entry_bg.get(), entry_fg.get()), borderwidth=5, padx=5, pady=5)
    button_custom.pack(side="left")

    # Quit Button
    button_quit = tk.Button(frame["quit_button"], text="Quit",
                            command=destroy_window, borderwidth=5, padx=5, pady=5)
    button_quit.pack(side="left")

    create_specific_Xterm_buttons()

root.mainloop()
