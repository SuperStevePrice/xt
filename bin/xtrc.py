#!/usr/bin/env python

import os

def set_globals():
    global xtrc

    xtrc = {
        'x_rows': "24",
        'x_cols': "80",
        'x_fg': "black",
        'x_bg': "grey",
        'x_fa': "9x15bold",
        'x_fs': "16",
        'x_log': 0,
        'x_sl': 200,
        'x_path': "",
    }

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
    # and update the xtrc dictionary
    for line in config_lines:
        line = line.strip()
        if line.startswith('#'):
            continue

        if line.startswith('x_cols'):
            xtrc['x_cols'] = line.split('=')[1].strip()
        elif line.startswith('x_rows'):
            xtrc['x_rows'] = line.split('=')[1].strip()
        elif line.startswith('x_sl'):
            xtrc['x_sl'] = line.split('=')[1].strip()
        elif line.startswith('x_fa'):
            xtrc['x_fa'] = line.split('=')[1].strip().replace(' ', '')
        elif line.startswith('x_fs'):
            xtrc['x_fs'] = line.split('=')[1].strip()
        elif line.startswith('x_bg'):
            xtrc['x_bg'] = line.split('=')[1].strip()
        elif line.startswith('x_fg'):
            xtrc['x_fg'] = line.split('=')[1].strip()
        elif line.startswith('x_path'):
            xtrc['x_path'] = line.split('=')[1].strip()
        elif line.startswith('x_log'):
            xtrc['x_log'] = int(line.split('=')[1].strip())

    return xtrc

def report():
    for key, value in xtrc.items():
        print(f"{key}:\t{value}")

if __name__ == "__main__":
    xtrc = set_globals()
    report()

