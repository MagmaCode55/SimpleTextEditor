from tkinter import filedialog, Scrollbar
import tkinter as tk
from tkinter.messagebox import showerror
from ctypes import windll
filename = 'Untitled'

def newFile(event=None):
    global filename
    filename = 'Untitled'
    root.title("Cool Text Editor - " + str(filename))
    text.delete(0.0, tk.END)

def saveFile(event=None):
    global filename
    print(filename)
    if filename is None or filename == 'Untitled':
        saveAs()
        return
    
    t = text.get(0.0, tk.END)
    f = open(filename, "w")
    f.write(t)
    
def saveAs(event=None):
    global filename
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    
    if f is None:
        return
    
    t = text.get(0.0, tk.END)
    try:
        f.write(t.rstrip())
        filename = f.name
        root.title("Cool Text Editor - " + str(filename))
        f.close()
    except:
        showerror(title='Oops!', message="Unable to save file")
        
def openFile(event=None):
    global filename
    f = filedialog.askopenfile(mode='r')
    if f is None:  
        return
    
    t = f.read()
    filename = f.name
    root.title("Cool Text Editor - " + str(filename))
    text.delete(0.0, tk.END)
    text.insert(0.0, t)
    



root = tk.Tk()
root.title("Cool Text Editor - " + str(filename))
root.minsize(width=400, height = 400)
windll.shcore.SetProcessDpiAwareness(1)

scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

text = tk.Text(root, font='Roboto', borderwidth=0, padx="5px", pady="5px", yscrollcommand=scrollbar.set)
text.pack(side='top', fill=tk.BOTH, expand=True)
text.focus_set()
text.mark_set("insert", tk.END)

menubar = tk.Menu(root, tearoff=0)

fileMenu = tk.Menu(menubar, tearoff=0, font='Arial 14')
fileMenu.add_command(label='New (Crtl+n)', command=newFile)
root.bind('<Control-n>', newFile)
fileMenu.add_command(label='Open (Crtl+o)', command=openFile)
root.bind('<Control-o>', openFile)
fileMenu.add_command(label='Save (Crtl+s)', command=saveFile)
text.bind('<Control-s>', saveFile)
fileMenu.add_command(label='Save As (Crtl+S)', command=saveAs)
text.bind('<Control-S>', openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Quit (Crtl-q)', command=root.quit)
root.bind('<Control-q>', lambda e: root.quit())

menubar.add_cascade(label='File', menu=fileMenu)

root.config(menu=menubar)

scrollbar.config( command = text.yview )

root.mainloop()