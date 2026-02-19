"""
CleanMyKeyboard - Dynamic Custom Combo & Emergency Eject Edition
"""

import tkinter as tk
import threading
import winsound
from pynput import keyboard, mouse

# --- Globals ---
pressed_keys = set()
UNLOCK = set()          
combo_display = ""      

# The hardcoded emergency exit (Ctrl + Alt + Esc)
KILL_SWITCH = {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.Key.esc}

kb_listener = None
mouse_listener = None
setup_root = None
lock_window = None
lock_label = None
is_unlocking = False
is_big = False


def normalize(key):
    """Treat left and right modifiers the same."""
    mapping = {
        keyboard.Key.ctrl_r:  keyboard.Key.ctrl_l,
        keyboard.Key.shift_r: keyboard.Key.shift_l,
        keyboard.Key.alt_gr:  keyboard.Key.alt_l,
        keyboard.Key.alt_r:   keyboard.Key.alt_l,
    }
    return mapping.get(key, key)


# --- Phase 2: The Vault (Lock Screen Logic) ---
def unlock():
    global is_unlocking
    if is_unlocking: return
    is_unlocking = True
    
    # Happy unlock sound
    threading.Thread(target=lambda: (winsound.Beep(1500, 150), winsound.Beep(2000, 200)), daemon=True).start()
    
    kb_listener.stop()
    mouse_listener.stop()
    
    # Destroy the vault and bring back the Lobby!
    lock_window.destroy()
    setup_root.deiconify()

def emergency_exit():
    # Long, low beep so you know the kill switch worked
    threading.Thread(target=lambda: winsound.Beep(400, 800), daemon=True).start()
    
    kb_listener.stop()
    mouse_listener.stop()
    
    # Safely nuke the entire application
    setup_root.after(0, setup_root.destroy)

def on_press(key):
    try:
        pressed_keys.add(normalize(key))
        
        # 1. Check for the Master Kill Switch FIRST
        if KILL_SWITCH.issubset(pressed_keys):
            emergency_exit()
            return

        # 2. Check for the normal custom unlock
        if UNLOCK.issubset(pressed_keys):
            unlock()
            
    except Exception: pass

def on_release(key):
    try: pressed_keys.discard(normalize(key))
    except KeyError: pass

def on_move(x, y):      pass
def on_click(*args):    pass
def on_scroll(*args):   pass

def start_listeners():
    global kb_listener, mouse_listener
    winsound.Beep(800, 300) # Lock sound
    kb_listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll, suppress=True)
    kb_listener.start()
    mouse_listener.start()

def pulse_animation():
    global is_big, lock_label
    if not lock_window or not lock_window.winfo_exists(): return

    new_size = 90 if is_big else 75
    lock_label.config(font=("Segoe UI Emoji", new_size))
    is_big = not is_big
    lock_window.after(600, pulse_animation)

def launch_vault():
    """Hides the setup menu and launches the lock screen."""
    global lock_window, lock_label, is_unlocking, pressed_keys
    
    is_unlocking = False
    pressed_keys.clear()
    setup_root.withdraw() # Hide the lobby

    threading.Thread(target=start_listeners, daemon=True).start()

    # Build the Lock Screen
    lock_window = tk.Toplevel(setup_root)
    lock_window.title("CleanMyKeyboard - Locked")
    lock_window.attributes("-fullscreen", True)
    lock_window.attributes("-topmost", True)
    lock_window.overrideredirect(True)
    lock_window.configure(bg="#1a1a2e")

    frame = tk.Frame(lock_window, bg="#1a1a2e")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    lock_label = tk.Label(frame, text="🔒", font=("Segoe UI Emoji", 75), bg="#1a1a2e", fg="#e94560")
    lock_label.pack(pady=(0, 20))

    tk.Label(frame, text="Keyboard Locked", font=("Segoe UI", 42, "bold"), fg="#e94560", bg="#1a1a2e").pack()
    tk.Label(frame, text="Clean your keyboard safely 🧹", font=("Segoe UI", 20), fg="#a8a8b3", bg="#1a1a2e").pack(pady=20)

    box = tk.Frame(frame, bg="#16213e", padx=30, pady=20)
    box.pack()

    tk.Label(box, text="To unlock, press:", font=("Segoe UI", 16), fg="#a8a8b3", bg="#16213e").pack()
    tk.Label(box, text=combo_display, font=("Segoe UI", 28, "bold"), fg="#0f3460", bg="#e94560", padx=20, pady=10).pack(pady=(10, 0))

    # The subtle emergency warning at the very bottom
    tk.Label(lock_window, text="Emergency Kill Switch: Ctrl + Alt + Esc", font=("Segoe UI", 10), fg="#3a3a4e", bg="#e94560").pack(side="bottom", pady=20)

    pulse_animation()


# --- Phase 1: The Lobby (Setup UI logic) ---
def save_combo_and_lock():
    global UNLOCK, combo_display
    UNLOCK.clear()
    display_parts = []

    if var_ctrl.get():
        UNLOCK.add(keyboard.Key.ctrl_l)
        display_parts.append("Ctrl")
    if var_shift.get():
        UNLOCK.add(keyboard.Key.shift_l)
        display_parts.append("Shift")
    if var_alt.get():
        UNLOCK.add(keyboard.Key.alt_l)
        display_parts.append("Alt")

    char = char_entry.get().strip().lower()
    if not char: char = 'q'
    
    UNLOCK.add(keyboard.KeyCode.from_char(char))
    display_parts.append(char.upper())

    combo_display = "  +  ".join(display_parts)
    launch_vault()


# --- Build Phase 1 UI ---
setup_root = tk.Tk()
setup_root.title("CleanMyKeyboard - Setup")
# Made the lobby a fixed, centered size without borders for a sleek look
setup_root.attributes("-fullscreen", True)
setup_root.overrideredirect(True) 
setup_root.configure(bg="#1a1a2e")

# The Emergency Exit Button for the Lobby (Top Right)
exit_btn = tk.Button(setup_root, text="✖", font=("Segoe UI", 14, "bold"), bg="#1a1a2e", fg="#e94560", bd=0, activebackground="#e94560", activeforeground="white", command=setup_root.destroy)
exit_btn.place(relx=0.98, rely=0.02, anchor="ne")

# Center content inside a frame so it doesn't collide with the absolute-placed 'X'
content_frame = tk.Frame(setup_root, bg="#1a1a2e")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(content_frame, text="⚙️ Setup Unlock Key", font=("Segoe UI", 20, "bold"), fg="#e94560", bg="#1a1a2e").pack(pady=(0, 20))

var_ctrl = tk.BooleanVar(value=True)
var_shift = tk.BooleanVar(value=True)
var_alt = tk.BooleanVar(value=False)

checks_frame = tk.Frame(content_frame, bg="#1a1a2e")
checks_frame.pack(pady=10)
tk.Checkbutton(checks_frame, text="Ctrl", variable=var_ctrl, font=("Segoe UI", 14), bg="#1a1a2e", fg="#a8a8b3", selectcolor="#16213e").pack(side="left", padx=10)
tk.Checkbutton(checks_frame, text="Shift", variable=var_shift, font=("Segoe UI", 14), bg="#1a1a2e", fg="#a8a8b3", selectcolor="#16213e").pack(side="left", padx=10)
tk.Checkbutton(checks_frame, text="Alt", variable=var_alt, font=("Segoe UI", 14), bg="#1a1a2e", fg="#a8a8b3", selectcolor="#16213e").pack(side="left", padx=10)

tk.Label(content_frame, text="Letter:", font=("Segoe UI", 14), fg="#a8a8b3", bg="#1a1a2e").pack(pady=(20, 5))
char_entry = tk.Entry(content_frame, font=("Segoe UI", 24, "bold"), width=3, justify="center", bg="#16213e", fg="#e94560", insertbackground="white")
char_entry.insert(0, "q")  
char_entry.pack()

lock_btn = tk.Button(content_frame, text="LOCK KEYBOARD", font=("Segoe UI", 16, "bold"), bg="#e94560", fg="#0f3460", padx=20, pady=10, command=save_combo_and_lock)
lock_btn.pack(pady=40)

setup_root.mainloop()