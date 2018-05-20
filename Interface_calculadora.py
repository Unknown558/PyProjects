from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
class Application:
    def __init__(self, master=None):

        self.quadranteTop = Frame(master)
        self.quadranteTop.pack()

        self.quadrante1 = Frame(master)
        self.quadrante1.pack()

        self.quadrante2 = Frame(master)
        self.quadrante2.pack()

        self.quadrante3 = Frame(master)
        self.quadrante3.pack()

        self.quadrante4 = Frame(master)
        self.quadrante4.pack()

        self.quadrante5 = Frame(master)
        self.quadrante5.pack()

        self.largura = Frame(master)
        self.largura["width"] = 450
        self.largura["height"] = 50
        self.largura.pack()

        self.msg0 = Label(self.quadranteTop, text="Calculadora de Equação do 2°Grau", height=2)
        self.msg0["font"] = 50
        self.msg0.pack()

        self.msgA = Label(self.quadrante1, text="Digite o A:", height=2)
        self.msgA["font"] = 50
        self.msgA.pack(side=LEFT)
        self.A = Entry(self.quadrante1)
        self.A.pack(side=LEFT)

        self.msgB = Label(self.quadrante2, text="Digite o B:", height=2)
        self.msgB["font"] = 50
        self.msgB.pack(side=LEFT)
        self.B = Entry(self.quadrante2)
        self.B.pack(side=LEFT)

        self.msgC = Label(self.quadrante3, text="Digite o C:", height=2)
        self.msgC["font"] = 50
        self.msgC.pack(side=LEFT)
        self.C = Entry(self.quadrante3)
        self.C.pack(side=LEFT)

        self.calcular = Button(self.quadrante4, text="CALCULAR", bg="#1f3c58", fg="#ebebeb")
        self.calcular["command"] = self.calc
        self.calcular.pack()

        self.delta = Label(self.quadrante5, text="")
        self.delta.pack()
        self.X1 = Label(self.quadrante5, text="")
        self.X1.pack()
        self.X2 = Label(self.quadrante5, text="")
        self.X2.pack()
        self.Xv = Label(self.quadrante5, text="")
        self.Xv.pack()
        self.Yv = Label(self.quadrante5, text="")
        self.Yv.pack()


    def calc(self):

        self.a = self.A.get()
        self.b = self.B.get()
        self.c = self.C.get()
        valor_a = self.a
        valor_b = self.b
        valor_c = self.c
        valor_a = float(valor_a)
        valor_b = float(valor_b)
        valor_c = float(valor_c)
        delta = ((valor_b) ** 2) - (4 * valor_a * valor_c)
        valor_x1 = (-(valor_b) + ((delta) ** (1 / 2))) / (2 * valor_a)
        valor_x2 = (-(valor_b) - ((delta) ** (1 / 2))) / (2 * valor_a)
        valor_xV = -(valor_b) / (2 * valor_a)
        valor_yV = -(delta) / (4 * valor_a)
        self.delta["text"] = "Delta =" + str(delta)
        self.X1["text"] = "X1 = " + str(valor_x1)
        self.X2["text"] = "X2 =" + str(valor_x2)
        self.Xv["text"] = "Xv =" + str(valor_xV)
        self.Yv["text"] = "Yv =" + str(valor_yV)

        eixo_x = []
        eixo_y = []
        zero = []

        variacao = abs(valor_x1 - valor_x2)
        if variacao < 3:
            variacao = 3
        for x in np.arange(valor_x1 - variacao, valor_x2 + variacao, variacao / 100):
            y = valor_a * (x ** 2) + valor_b * (x) + valor_c
            eixo_x.append(x)
            eixo_y.append(y)
            zero.append(0.0)
        plt.plot(eixo_x, eixo_y, color="blue")
        plt.plot(eixo_x, zero, color="black")
        plt.show()



root = Tk()
Application(root)
#root.configure(background="black")
root.mainloop()