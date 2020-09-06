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
    z = []

    for p in range(len(patt_list)):
                
        for s in range(len(patt_list)):
            temp.insert(s,patt_list[s])

        for q in range(len(inp_list)):
            
            st = ""
            temp[p] = inp_list[q]
            z1 = st.join(temp)
            z.append(z1)   
        del temp[:]

    for i in range(len(z)):
        t1.insert(END,str(z[i]) + "\n")
        # labels[i].place(x=20,y=30+(20*i))
    
   

if __name__=="__main__":
    root = Tk()
    root.title("Sequence Builder")
    root.config(bg="gray85")

    pattern = StringVar()
    inputs = StringVar()

    # frame = Frame(root, width=600, height=200, bg="dark sea green")
    # frame.grid(row=0,column=0,padx=10,pady=5)

    # c = Canvas(root, height=400, width=600, bg="gray78")
    # c.grid(row=1,column=0, padx=5, pady=5)

    l1=Label(root,text="Pattern")
    l1.place(x=0,y=0)

    l2=Label(root,text="Inputs")
    l2.place(x=0,y=30)

    e1=Entry(root,textvariable=pattern)
    e1.place(x=120,y=0)

    e2=Entry(root,textvariable=inputs)
    e2.place(x=120,y=30)

    b1=Button(root,text="Enter",command=sequence,width=30,bg="light slate blue",activebackground="slate blue")
    b1.grid(row=11,column=0,padx=10)

    t1=Text(root,width=80,height=20)
    t1.grid(row=0,column=1)

    root.mainloop()
