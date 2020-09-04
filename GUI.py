from tkinter import *
import sys
import random

def sequence():
    patt = pattern.get()
    inp = inputs.get()

    def split(l):
        return list(l)

    patt_list = split(patt)
    inp_list = split(inp)


    temp = []
    
    for p in range(len(patt_list)):
                
        for s in range(len(patt_list)):
            temp.insert(s,patt_list[s])

        for q in range(len(inp_list)):
            
            str = ""
            temp[p] = inp_list[q]
            z1 = z1 + str.join(temp)
        del temp[:]

    
    L=Label(root, text=z1)
    L.grid(row = 1,column = 1)


root = Tk()
root.title("Sequence Builder")
root.config(bg="gray85")

pattern = StringVar()
inputs = StringVar()

frame = Frame(root, width=600, height=200, bg="dark sea green")
frame.grid(row=0,column=0,padx=10,pady=5)

c = Canvas(root, height=400, width=600, bg="gray78")
c.grid(row=1,column=0, padx=5, pady=5)

e1= Entry(root,textvariable=pattern,font=('calibre',10,'normal')) 
e1.grid(row=0,column=0,padx=5,pady=5)

e2= Entry(root,textvariable=inputs,font=('calibre',10,'normal')) 
e2.grid(row=0,column=1,padx=5,pady=5)

button = Button(root, text = 'Enter', width = 10,
    command = sequence)
button.grid(row = 0, column = 2)

# max_val = Scale(frame,from_=80, to=100,length=100,resolution=1,orient=HORIZONTAL,label="Max. value",activebackground="lavender")
# max_val.grid(row=0,column=1,padx=5,pady=5)
# max_val.config(bg="LightCyan2")
root.mainloop()