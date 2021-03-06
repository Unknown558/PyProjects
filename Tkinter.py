from tkinter import *
class Application:
    def __init__(self, master=None):
        self.tela1 = Frame(master)
        self.tela1["pady"] = 10
        self.tela1.pack()

        self.tela2 = Frame(master)
        self.tela2["padx"] = 20
        self.tela2.pack()

        self.tela3 = Frame(master)
        self.tela3["padx"] = 20
        self.tela3.pack()

        self.tela4 = Frame(master)
        self.tela4["padx"] = 20
        self.tela4.pack()

        self.msg1 = Label(self.tela1, text="Login")
        self.msg1["font"] = ("Calibri", "16")
        self.msg1.pack()

        self.msg2 = Label(self.tela2, text="Nome: ")
        self.msg2.pack(side=LEFT)
        self.nome = Entry(self.tela2)
        self.nome.pack()

        self.msg3 = Label(self.tela3, text="Senha: ")
        self.msg3.pack(side=LEFT)
        self.senha = Entry(self.tela3)
        self.senha["show"] = "*"
        self.senha.pack()
        self.botao = Button(self.tela4, text="Entrar", width=22, bg="#1f3c58", fg="#ebebeb")
        self.botao["command"] = self.autenticando_usuarios
        self.botao.pack()
        self.msg4 = Label(self.tela4, text="")
        self.msg4.pack()


    def autenticando_usuarios(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "Gui" and senha == "gui123":
            self.msg4["text"] = "Autenticado"
        else:
            self.msg4["text"] = "Erro na autenticação"

root = Tk()
Application(root)
root.mainloop()