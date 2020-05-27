from tkinter import *

class Display:

    def acao_tela(self, valor):

        # self.valor = valor
        print(valor)


    def __init__(self, container):

        self.janela = container

        self.valor = IntVar()
        self.valor.set(10)

        # FRAME
        self.frame_visor = Frame(self.janela, width=300, height=50, bg='yellow')
        self.frame_visor.pack(side=TOP)

        self.label_visor = Label(self.frame_visor, textvariable=self.valor, font=('arial', 15, 'bold'))
        self.label_visor.place(x=20, y=10)






