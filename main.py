#!/usr/bin/python
# coding: utf-8

# TODO :
# delete draft if saved as published
# use pelicanconf to more flexible paramters
# config file with default pelican blog
#

import Tkinter as tk
import ScrolledText
import tkFileDialog
import os
import getpass
import subprocess
import ttk


class MainApplication(tk.Frame):
    path = None
    draft_directory = None
    publish_directory = None

    def choose_pelican_path(self):
        """
        menu option to set the pelican blog folder
        check if this is a pelican folder by trying to find the pelicanconf.py
        file.
        create a draft folder if not existe

        TODO :
            use a config file for persistent saving
        """
        self.path = tkFileDialog.askdirectory()
        self.publish_directory = "/".join([self.path, "content"])
        self.draft_directory = "/".join([self.path, "draft"])
        if os.path.isdir(self.path):
            if not os.path.exists("/".join([self.path, "pelicanconf.py"])):
                # TODO : try to find a ... cleaner way to do that
                print "Not a pelican folder ! "
                exit(1)
            if not os.path.isdir(self.draft_directory):
                # create draft folder
                os.makedirs(self.draft_directory)

    def open_dir(self, path):
        """
        Open a file in path and parse the file to fill
        all fields of the interface
        """
        if path:
            self.draft = tkFileDialog.askopenfilename(initialdir=path)
            if self.draft:
                self.new_article()  # flush the fields before adding values
                with open(self.draft, 'r') as d:
                    for line in d:
                        if "Title:" in line:
                            to_insert = " ".join(line.split(":")[1:]).strip()
                            self.title_entry.insert(0, to_insert)
                        elif "Date:" in line:
                            to_insert = " ".join(line.split(":")[1:]).strip()
                            self.date_entry.insert(0, to_insert)
                        elif "Category:" in line:
                            to_insert = " ".join(line.split(":")[1:]).strip()
                            self.category_entry.delete(0, tk.END)
                            self.category_entry.insert(0, to_insert)
                        elif "Tags:" in line:
                            to_insert = " ".join(line.split(":")[1:]).strip()
                            self.tags_entry.insert(0, to_insert)
                        elif "Summary:" in line:
                            to_insert = " ".join(line.split(":")[1:]).strip()
                            self.summary_entry.insert(0, to_insert)
                        elif "Slug:" in line or "Author:" in line:
                            continue
                        else:
                            self.body_entry.insert(tk.END, line)
                print self.draft
        else:
            print "set pelican home first"

    def open_draft(self):
        """
        open a file in $PELICAN_HOME/draft/ folder
        """
        self.open_dir(self.draft_directory)

    def open_published(self):
        """
        open a file in $PELICAN_HOME/content/ folder
        """
        self.open_dir(self.publish_directory)

    def new_article(self):
        """
        flush all fields in interface
        """
        self.title_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.tags_entry.delete(0, tk.END)
        self.summary_entry.delete(0, tk.END)
        self.body_entry.delete('0.0', tk.END)

    def clean_title(self, title):
        """
        Prepare title for slug
        """
        title = title.strip()
        title = title.replace(" ", "-")
        title = title.replace("'", "-")
        title = title.replace(":", "-")
        return title.lower()

    def save_file(self, path):
        """
        retrieve informations from the GUI to generate the markdown document
        and save it
        """
        title = self.title_entry.get()
        date = self.date_entry.get()
        categories = self.category_entry.get()
        tags = self.tags_entry.get()
        summary = self.summary_entry.get()
        body = self.body_entry.get(1.0, tk.END).strip()
        author = getpass.getuser()
        slug = self.clean_title(title)
        f = tkFileDialog.asksaveasfile(mode='w',
                                       defaultextension=".md",
                                       initialdir=path)
        if f is None:
            return
        text_to_save = u"""Title: {0}
Date: {1}
Category: {2}
Tags: {3}
Author: {4}
Slug: {5}
Summary: {6}
{7}
""".format(title, date, categories, tags, author, slug, summary, body)
        f.write(text_to_save)
        name = f.name
        f.close()
        return name

    def save_draft(self):
        f = self.save_file(self.draft_directory)
        draft_file = f.name
        if os.path.exists(draft_file):
            pub_file = draft_file.replace('draft', 'content')
            os.rename(pub_file, draft_file)

    def save_published(self):
        f = self.save_file(self.publish_directory)
        pub_file = f.name
        # delete draft if needs to be published
        if os.path.exists(pub_file):
            draft_file = pub_file.replace('content', 'draft')
            os.rename(draft_file, pub_file)

    def go_live(self):
        os.chdir(self.path)
        subprocess.call(["make", "publish", "ssh_upload"])

    def __init__(self, parent, *args, **kwargs):
        """
        Creation of the GUI is done here
        """
        s = ttk.Style()
        s.theme_use('classic')
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.resizable(width=False, height=True)
        tk.Grid.rowconfigure(self.parent, 0, weight=1)
        tk.Grid.columnconfigure(self.parent, 0, weight=1)
        # Use grid
        self.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        # menu configuration
        self.menu_bar = tk.Menu(self)
        self.menu_bar.add_command(label="set pelican home",
                                  command=self.choose_pelican_path)
        self.menu_bar.add_command(label="Quit",
                                  command=self.quit)
        self.parent.config(menu=self.menu_bar)

        # declare elements
        # buttons
        self.new_article_button = tk.Button(self,
                                            text="new article",
                                            command=self.new_article)
        self.open_draft_button = tk.Button(self,
                                           text="open Draft",
                                           command=self.open_draft)
        self.open_published_button = tk.Button(self,
                                               text="Open published article",
                                               command=self.open_published)
        self.save_draft_button = tk.Button(self,
                                           text="Save to draft",
                                           command=self.save_draft)
        self.save_published_button = tk.Button(self,
                                               text="Ready to publish",
                                               command=self.save_published)
        self.upload_button = tk.Button(self,
                                       text="Go online",
                                       command=self.go_live)
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
        self.body_entry = ScrolledText.ScrolledText(self, wrap=tk.WORD)

        # position elements on the grid
        self.new_article_button.grid(column=0,
                                     row=0,
                                     sticky='W',
                                     pady=(20, 20),
                                     padx=(20, 0))
        self.open_draft_button.grid(column=1,
                                    row=0,
                                    pady=(20, 20))
        self.open_published_button.grid(column=2,
                                        row=0,
                                        sticky='E',
                                        pady=(20, 20),
                                        padx=(0, 20))
        self.title_label.grid(column=0,
                              row=1,
                              sticky='W')
        self.date_label.grid(column=0,
                             row=2,
                             sticky='W')
        self.category_label.grid(column=0,
                                 row=3,
                                 sticky='W')
        self.tags_label.grid(column=0,
                             row=4,
                             sticky='W')
        self.summary_label.grid(column=0,
                                row=5,
                                sticky='W')
        self.body_label.grid(column=0,
                             row=6,
                             sticky='W')

        self.title_entry.grid(column=1,
                              row=1,
                              sticky='WE')
        self.date_entry.grid(column=1,
                             row=2,
                             sticky='WE')
        self.category_entry.grid(column=1,
                                 row=3,
                                 sticky='WE')
        self.tags_entry.grid(column=1,
                             row=4,
                             sticky='WE')
        self.summary_entry.grid(column=1,
                                row=5,
                                sticky='WE')
        self.body_entry.grid(column=1,
                             row=6,
                             columnspan=2,
                             sticky='NSWE',
                             padx=(0, 50),
                             pady=(0, 50))

        self.save_draft_button.grid(column=0,
                                    row=7,
                                    sticky=tk.W,
                                    pady=(20, 20),
                                    padx=(20, 0))
        self.save_published_button.grid(column=1,
                                        row=7,
                                        pady=(20, 20))
        self.upload_button.grid(column=2,
                                row=7,
                                pady=(20, 20),
                                padx=(0, 20))

        # manage horizontal and vertical resizing
        self.columnconfigure(1, weight=3)
        self.rowconfigure(6, weight=3)

        self.update()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
