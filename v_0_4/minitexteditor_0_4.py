#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.scrolledtext as ScrolledText
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *

master = Tk()
master.title("MiniTextEditor")
#===Variables
choicevar = StringVar()
#===
#master.resizable(width=0, height=0)
try:
      #master.iconbitmap("minitexteditorico_v1.png")
      #master.iconphoto(False, tk.PhotoImage(file="minitexteditorico_v1.png"))
      #master.call(
      #"wm", 
      #"iconphoto", 
      #master._w, 
      #PhotoImage(file="minitexteditorico_v1.png")
      #)
      master.iconphoto(False, PhotoImage(file="minitexteditorico_v1.png"))
except TclError:
      showwarning("UI error ...", "The icon wasn't found.")
#commands
def openf():
    filename = askopenfilename(title="Open a text file ...",filetypes=[("txt files",".txt"),("all files",".*")])
    fichier = open(filename, "r")
    content = fichier.read()
    content = str(content)
    st.delete("1.0", END)
    st.insert(INSERT, content)
def saveasf():
    file = asksaveasfile(title="Save your file ...", mode="w", defaultextension=".txt")
    text = str(st.get(1.0, END))
    file.write(text)
    file.close()
def aboutmen():
    showinfo("About", "About\n________________________\nMiniTextEditor\nby mibi88\n\nVersion : v.0.4\n\nLicense :\nThe Unlicense\n________________________\n Thank you for using\nthis text editor !")
def helpmen():
    showinfo("Help", "Help\n________________________\n\n________________________\n")
def newf():
    if askyesno("New file ...", "If you create a new file, you can lose content.\nDo you want to create a new file ?"):
        st.delete("1.0", END)
    else:
        showinfo("New file ...", "Your content wasn't deleted.")
def quitw():
    if askyesno("Quit ...", "If you quit this text editor, you can lose content.\nDo you want to quit ?"):
        master.quit()
    else:
        showinfo("Quit ...", "The text editor is stayed open.")
def search():
      start = 1.0
      inputwin = askstring("Search", "Text to search :")
      try:
            start = "1.0"
            text_end = "1.0"
            text_end_t = "1.0"
            text = st.search(inputwin, start, stopindex='end')
            data = st.get("1.0", END)
            data = str(data)
            print(data)
            nbword = data.count(inputwin)
            print(nbword)
            scrolled = 0
            tag_name = 1
            while scrolled != nbword:
                  lenght = None
                  lenght_t = ""
                  start = str(text_end_t)
                  text = st.search(inputwin, start, stopindex='end')
                  start = text
                  msg = "'text' var : " + str(text)
                  print(msg)
                  lenght = len(inputwin)
                  lenght_t = str(lenght)
                  """
                  lenght_t = "0." + lenght_t
                  msg = "'lenght_t' var " + str(lenght_t)
                  print(msg)
                  text_end_t = float(text) + float(lenght_t)
                  msg = "'text' var : " + str(text)
                  print(msg)
                  msg = "'text_end_t' var : " + str(text_end_t)
                  print(msg)
                  """
                  todelete = len(lenght_t)
                  text_t = str(text)
                  text_lenght = len(text_t)
                  #
                  scrolled += 1
                  tag_name += 1
                  st.tag_add(str(tag_name), text, text_end_t)
                  st.tag_config(str(tag_name), background="yellow")
      """
      inputwin = askstring("Search", "Text to search :")
      try:
            text = st.findall(inputwin)
            st.tag_add("foundtext", text)
            st.tag_config("foundtext", background="yellow")
      """
      except TclError:
            pass
            #showinfo("Result ...", "Text not found")
#---
#separatorf = Frame(master, borderwidth=2, relief=GROOVE)
#separatorf.pack(side=LEFT, padx=5)
#---
def undoa():
    st.edit_undo()
def redoa():
    st.edit_redo()
def choice():
      choice = choicevar.get()
      print(choice)
      if choice == "Search":
            search()

#---
#def updatefont():
#    fontsiz = fontsize.get()
#    st.set(font = ("Liberation Serif", fontsiz)
#---
#fontsiz = 12
#---
commands = LabelFrame(master, text="File")
#commands.pack(fill="both", expand="yes")
commands.pack(fill=X)
#===
newfil = Button(commands, text="New file", command=newf)
newfil.pack(side=LEFT)
#===
openfil = Button(commands, text="Open", command=openf)
openfil.pack(side=LEFT)
#===
saveasfil = Button(commands, text="Save As", command=saveasf)
saveasfil.pack(side=LEFT)
#---
undo = Button(commands, text="Undo", command=undoa)
undo.pack(side=LEFT)
redo = Button(commands, text="Redo", command=redoa)
redo.pack(side=LEFT)
#---
other_tools = Combobox(commands, values=["Search", "Search and replace", "Syntax color"], textvariable = choicevar)
other_tools.pack(side=LEFT)
validate_choice = Button(commands, text="Validate", command=choice)
validate_choice.pack(side=LEFT)
#---
#value = DoubleVar()
#fontsize = Scale(commands, orient='horizontal', variable=value)
#fontsize.pack(side=LEFT)
#updatefont = Button(commands, text="Apply the selected font size", command=updatefont)
#updatefont.pack(side=LEFT)
#fontsiz = fontsize.get()
#===
quitb=Button(commands, text="Quit", command=quitw)
quitb.pack(side=RIGHT)
#===
aboutmen = Button(commands, text="About", command=aboutmen, cursor="plus")
aboutmen.pack(side=RIGHT)
#===
helpmen = Button(commands, text="Help", command=helpmen, cursor="plus")
helpmen.pack(side=RIGHT)
#===
st = ScrolledText.ScrolledText(master, undo="True", wrap="word", takefocus=0)
#st = ScrolledText.ScrolledText(master, font = ("Liberation Serif", fontsiz))
st.pack(expand=True, fill=BOTH, side=BOTTOM)

print( st.get(1.0, END) )
master.mainloop()
