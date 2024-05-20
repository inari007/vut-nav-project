import tkinter as tk
from tkinter import ttk

class UserInterface:
    def __init__(self, songs, youtube_bot):
        self.youtubeBot = youtube_bot

        self.root = tk.Tk()
        self.root.geometry("250x200")
        self.root.title("Song selector")

        self.canvas = tk.Canvas(self.root)

        self.style = ttk.Style()

        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#f542ce', font=('calibri', 14, 'bold'), foreground='red')

        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.frame = ttk.Frame(self.canvas, style='TFrame')

        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame.bind_all("<MouseWheel>", self.on_mousewheel)

        i = 0
        for key, value in songs.items():
            button = ttk.Button(self.frame, text=key, style='TButton', command=lambda val=value: self.ClickButton(val))
            button.pack(pady=5)
            i = i + 1

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.root.mainloop()

    def ClickButton(self, link):
        self.youtubeBot.OpenLink(link)

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
