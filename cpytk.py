from tkinter import *
def a():
    lb["text"] = ed.get()
janela = Tk()
ed = Entry(janela)
ed.place(x=150, y=100)
lb = Label(janela)
lb["bg"] = "#ebeb87"
lb.place(x=250, y=200)
bt = Button(janela, text="OK")
bt["command"] = a
bt.place(x=400, y=250)
janela["bg"] = "#ebeb87"
janela.title("Testee")
janela.geometry("500x350+500+250") #LxA+E+T
janela.mainloop()