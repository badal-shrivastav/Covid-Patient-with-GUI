import covid
from tkinter import *
a=""

def check():
    data = covid.Covid()
    global a
    a = data.get_status_by_country_name(txt.get())
    out=("Country: "+str(a["country"])+"\n"+"Confirmed: "+str(a["confirmed"])+"\n"+\
         "Active: "+str(a["active"])+"\n"+"Deaths: "+str(a["deaths"])+"\n"+"Recovered: "+ str(a["recovered"]))


    Label(tk,height=20,width=20, text=out,font="Times").pack(pady=8)


tk= Tk()
tk.title("Live Corona Details")
# tk.configure(bg="grey")
txt=StringVar()

tk['background']="#ebe99b"
tk.geometry("300x300")
tk.maxsize(300,300)
tk.minsize(300,300)
t = Entry(tk,border="3",width=26,font="Arial 15",textvariable=txt)
t.pack(pady="10",ipady="3")

b= Button(tk,text="Check",width="11",command=check)
b.pack(ipady=4)



tk.mainloop()