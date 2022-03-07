from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = int(detik.get())
        menit.set(int(value/60))
        jam.set(int((value/60)/60))
    except ValueError:
        pass

root = Tk()
root.title("Detik ke menit dan jam")

mainframe = ttk.Frame(root, padding="25 25 25 25")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=5)
root.rowconfigure(0, weight=5)

detik = StringVar()
detik_entry = ttk.Entry(mainframe, width=7, textvariable=detik)
detik_entry.grid(column=2, row=1, sticky=E)

menit = StringVar()
ttk.Label(mainframe, textvariable=menit).grid(column=2, row=2, sticky=E)

jam = StringVar()
ttk.Label(mainframe, textvariable=jam).grid(column=2, row=3, sticky=E)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="Detik").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Menit").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Jam").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

detik_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()