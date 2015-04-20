#!/usr/local/bin/python3.4
#coding: utf-8

import Tkinter as tk
import ScrolledText
import tkFileDialog

class MainApplication(tk.Frame):
    # TODO method:
    # save pelicanpath
    path=None

    def choose_pelican_path(self):
        self.path = tkFileDialog.askdirectory()
        print(self.path)
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.resizable(width=False, height=True)
        tk.Grid.rowconfigure(self.parent, 0, weight=1)
        tk.Grid.columnconfigure(self.parent, 0, weight=1)
        # <create the rest of your GUI here>
        self.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        # menu configuration
        self.menu_bar = tk.Menu(self)
        self.menu_bar.add_command(label="set pelican home", command=self.choose_pelican_path)
        self.menu_bar.add_command(label="Quit", command=self.quit)
        self.parent.config(menu=self.menu_bar)

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
        self.body_entry = ScrolledText.ScrolledText(self,wrap=tk.WORD)

        ## position elements on the grid
        self.new_article_button.grid(column=0, row=0, sticky='W', pady=(20,20))
        self.open_draft_button.grid(column=1, row=0 , pady=(20,20))
        self.open_published_button.grid(column=2, row=0, sticky='E', pady=(20,20))
        self.title_label.grid(column=0, row=1, sticky='W')
        self.date_label.grid(column=0, row=2, sticky='W')
        self.category_label.grid(column=0, row=3, sticky='W')
        self.tags_label.grid(column=0, row=4, sticky='W')
        self.summary_label.grid(column=0, row=5, sticky='W')
        self.body_label.grid(column=0, row=6, sticky='W')

        self.title_entry.grid(column=1, row=1, sticky='WE')
        self.date_entry.grid(column=1, row=2, sticky='WE')
        self.category_entry.grid(column=1, row=3, sticky='WE')
        self.tags_entry.grid(column=1, row=4, sticky='WE')
        self.summary_entry.grid(column=1, row=5, sticky='WE')
        self.body_entry.grid(column=1, row=6, columnspan=2, sticky='NSWE', padx=(0,50), pady=(0,50))

        self.save_draft_button.grid(column=0, row=7, sticky=tk.W, pady=(20,20))
        self.save_published_button.grid(column=1, row=7, pady=(20,20))
        self.upload_button.grid(column=2, row=7, pady=(20,20))

        # manage horizontal and vertical resizing
        self.columnconfigure(1, weight=3)
        self.rowconfigure(6, weight=3)

        self.update()



    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
