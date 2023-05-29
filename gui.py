import tkinter as tk
import subprocess

def run_main():
    subprocess.call(['python', 'main.py'])

root = tk.Tk()
root.title("Drowsiness Detection")
root.geometry("400x150")
root.configure(bg='#f0f0f0')

label = tk.Label(root, text="Press Start to detect drowsiness", font=('Helvetica', 16), fg='#333', bg='#f0f0f0')
label.pack(pady=20)

button = tk.Button(root, text="Start", command=run_main, font=('Helvetica', 14), bg='#4CAF50', fg='white', activebackground='#3e8e41', activeforeground='white')
button.pack(pady=10)

root.mainloop()
