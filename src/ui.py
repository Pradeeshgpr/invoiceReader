from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image

import os,glob

from main import mainFun


class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        ftypes = [('All files', '*')]
        fname = filedialog.askopenfile(filetypes=ftypes)
        #self.iniopen(fname.name)

        #__f_tmp=glob.glob(pdfImg.PyGs({}).make_img_from_pdf(fname.name)[1])[0]
        self.original = Image.open(fname.name)

        self.image = ImageTk.PhotoImage(self.original)
        #print("enamo")
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

        self.widgets(fname)

    def iniopen(self):
        self.master.title("FirstImager")
        menubar = Menu(root)
        #print("smthng")
        # print(fname.name)
        menubar.add_command(label="Open", command=self.onOpen())
        root.config(menu=menubar)

    def widgets(self,fname):
         self.master.title("InvoiceImager")
         menubar = Menu(root)
         menubar.add_command(label="Detect", command=mainFun(fname.name))
         root.config(menu=menubar)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ADAPTIVE)
        self.image = ImageTk.PhotoImage(resized)
        #self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

root = Tk()
app = App(root)
app.mainloop()
#root.destroy()
