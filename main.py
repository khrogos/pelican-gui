#!/usr/local/bin/python3.4
#coding: utf-8

import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # <create the rest of your GUI here>
        new_article_button = tk.Button(self, text="new article", command=self.flush)

    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
