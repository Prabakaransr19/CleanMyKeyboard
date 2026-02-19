<div align="center">

# ⌨️ CleanMyKeyboard

**Lock your keyboard & mouse in one click — clean safely, unlock instantly.**

[![Download](https://img.shields.io/badge/⬇️%20Download%20for%20Windows-v1.1-e94560?style=for-the-badge)](https://github.com/Prabakaransr19/CleanMyKeyboard/releases/latest)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🧹 What is CleanMyKeyboard?

Ever accidentally opened 10 browser tabs while trying to wipe your keyboard? **CleanMyKeyboard** locks your keyboard and mouse completely so you can clean without chaos.

- 🔒 Blocks all keyboard & mouse input instantly
- ⚙️ Set your own custom unlock key combo
- 🔊 Sound feedback on lock and unlock
- 💡 Animated fullscreen lock screen
- 🖥️ Lives quietly in your system tray

---

## ⬇️ Download

<div align="center">

[![Download Latest Release](https://img.shields.io/badge/⬇️%20Download%20CleanMyKeyboard.exe-v1.1%20for%20Windows-e94560?style=for-the-badge&logoColor=white)](https://github.com/Prabakaransr19/CleanMyKeyboard/releases/latest)

> No installation needed. Just download and run.

</div>

---

## 🚀 How to Use

1. **Run** `CleanMyKeyboard.exe`
2. **Choose** your unlock key combo (e.g. Ctrl + Shift + Q)
3. Click **LOCK KEYBOARD**
4. 🧹 Clean your keyboard safely
5. Press your combo to **unlock**

---

## 🛠️ Built With

- [Python](https://python.org) — core language
- [tkinter](https://docs.python.org/3/library/tkinter.html) — UI / fullscreen lock screen
- [pynput](https://pynput.readthedocs.io/) — keyboard & mouse blocking
- [pystray](https://pystray.readthedocs.io/) — system tray icon
- [PyInstaller](https://pyinstaller.org/) — packaged into `.exe`

---

## 🧑‍💻 Run from Source

```bash
# Clone the repo
git clone https://github.com/Prabakaransr19/CleanMyKeyboard.git
cd CleanMyKeyboard

# Install dependencies
pip install pynput pystray pillow

# Run the app
python app.py
```

---

## 📦 Build the .exe yourself

```bash
pip install pyinstaller
pyinstaller --onefile --windowed app.py
```

The `.exe` will be in the `dist/` folder.

---

## 📄 License

MIT — free to use, modify, and share.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Prabakaransr19">Prabakaransr19</a>
</div>
