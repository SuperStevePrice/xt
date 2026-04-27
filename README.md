# Project xt

This repository contains programs to launch dashboards that enable rapid xterm
window generation using the user's preferences.

## Scripts

### Perl: xt.pl
`xt.pl` can be executed directly, or launched via `xt.ksh`, a ksh script that
sets the environment and launches `xt.pl`. `~/bin/xt` is a symbolic link to
`~/bin/xt.ksh`.

### Python: xt.py
`xt.py` can be executed directly, or launched via `xtpy`, a ksh script that
sets the environment and launches `xt.py`.

### Screenshots

Perl `xt.pl`:
![xt perl](assets/xt%20perl.png)

Python `xt.py`:
![xt python](assets/xt%20python.png)

---

## Python Requirements (macOS)

`xt.py` uses Tkinter for its GUI. On macOS this requires **Tk 8.6 or later**,
which is not provided by Apple's system Python (`/usr/bin/python3` ships with
Tk 8.5, incompatible with modern XQuartz and will cause an immediate abort).

**Suitable Python installations for macOS:**
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) — recommended, carries Tk 8.6.15
- [Anaconda](https://www.anaconda.com/) — also carries Tk 8.6
- [Homebrew](https://brew.sh/) Python with `brew install python-tk`

The shebang in `xt.py` is hardcoded to Miniconda:
```
#!/Users/steve/miniconda3/bin/python3
```

If you use a different Python installation, update this line accordingly. See
the comments at the top of `xt.py` for a full explanation.

**Linux:** `#!/usr/bin/env python3` works correctly — use your system or
preferred Python 3 with `python3-tk` installed.

---

## Installation

The `setup.ksh` script in the
[ShellSetup](https://github.com/SuperStevePrice/ShellSetup) project handles
installation and permission management for all components of this repository.

---

## Viewing the Documentation

To correctly view images embedded in this documentation, use one of the
following Markdown editors:

1. **Typora** — Cross-platform, real-time preview, excellent image support.
   OS: Linux, macOS, Windows
   [Typora Website](https://typora.io/)

2. **Visual Studio Code** — Highly customizable, use "Markdown All in One" or
   "Markdown Preview Enhanced" extensions.
   OS: Linux, macOS, Windows
   [Visual Studio Code Website](https://code.visualstudio.com/)

3. **Remarkable** — Simple and lightweight with image embedding.
   OS: Linux
   [Remarkable GitHub Repository](https://remarkableapp.github.io/linux.html)

4. **Ghostwriter** — Distraction-free writing environment with image support.
   OS: Linux, Windows
   [Ghostwriter GitHub Repository](https://github.com/wereturtle/ghostwriter)

5. **Haroopad** — Live preview and image support.
   OS: Linux, macOS, Windows
   [Haroopad Website](http://pad.haroopress.com/)

If you encounter any issues with image display, ensure the image files are in
the same directory as this documentation, or refer to the installation
instructions for your chosen editor.
