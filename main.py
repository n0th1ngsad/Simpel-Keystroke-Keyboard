import tkinter as tk
from tkinter import Label
import keyboard

class KeyVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Key Visualizer")
        self.geometry("300x100")
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.8)
        self.overrideredirect(True)
        self.config(bg='black')  

        self.key_label = Label(self, text='', font=('Arial', 40), bg='black', fg='white')
        self.key_label.pack(expand=True)

        self.update_key()
        
    def update_key(self):
        keys = ['w', 'a', 's', 'd']
        pressed_keys = [key.upper() for key in keys if keyboard.is_pressed(key)]

        if pressed_keys:
            self.key_label.config(text=' '.join(pressed_keys))
        else:
            self.key_label.config(text='')

        self.after(50, self.update_key)  

if __name__ == "__main__":
    app = KeyVisualizer()
    app.mainloop()
