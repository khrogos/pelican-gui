#!/usr/local/bin/python3.4
#coding: utf-8

import Tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        tk.Grid.rowconfigure(self.parent, 0, weight=1)
        tk.Grid.columnconfigure(self.parent, 0, weight=1)
        # <create the rest of your GUI here>
        self.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        ## declare elements
        # buttons
        self.new_article_button = tk.Button(self, text="new article", command=self.flush)
        self.open_draft_button = tk.Button(self, text="open Draft", command=self.flush)
        self.open_published_button = tk.Button(self, text="Open published article", command=self.flush)
        self.save_draft_button = tk.Button(self, text="Save to draft", command=self.flush )
        self.save_published_button = tk.Button(self, text="Ready to publish", command=self.flush )
        self.upload_button = tk.Button(self, text="Go online", command=self.flush )
        # labels and entrys
        self.title_label = tk.Label(self, text="Title")
        self.date_label = tk.Label(self, text="Date")
        self.category_label = tk.Label(self, text="Category")
        self.tags_label = tk.Label(self, text="Tags")
        self.summary_label = tk.Label(self, text="summary")
        self.body_label = tk.Label(self, text="Body")
        
        self.title_entry = tk.Entry(self)
        self.date_entry = tk.Entry(self)
        self.category_entry = tk.Entry(self)
        self.tags_entry = tk.Entry(self)
        self.summary_entry = tk.Entry(self)
        self.body_entry = tk.Entry(self)

        ## position elements
        self.new_article_button.grid(column=0, row=0, sticky='NEWS')
        self.open_draft_button.grid(column=1, row=0, sticky='NEWS')
        self.open_published_button.grid(column=2, row=0, sticky='NEWS')
        self.title_label.grid(column=0, row=1, sticky='W')
        self.date_label.grid(column=0, row=2, sticky='W')
        self.category_label.grid(column=0, row=3, sticky='W')
        self.tags_label.grid(column=0, row=4, sticky='W')
        self.summary_label.grid(column=0, row=5, sticky='W')
        self.body_label.grid(column=0, row=6, sticky='W')

        self.title_entry.grid(column=1, row=1, columnspan=2, sticky='E')
        self.date_entry.grid(column=1, row=2, columnspan=2, sticky='E')
        self.category_entry.grid(column=1, row=3, columnspan=2, sticky='E')
        self.tags_entry.grid(column=1, row=4, columnspan=2, sticky='E')
        self.summary_entry.grid(column=1, row=5, columnspan=2, sticky='E')
        self.body_entry.grid(column=1, row=6, columnspan=2, sticky='E')

        self.save_draft_button.grid(column=0, row=7, sticky=tk.W)
        self.save_published_button.grid(column=1, row=7)
        self.upload_button.grid(column=2, row=7)

        self.update()



    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
