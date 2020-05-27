from tkinter import *

class Operadores:

    def __init__(self, container):

        self.janela = container

        # FRAME
        self.frame_botoes = Frame(self.janela, width=100, height=270, bg='blue')
        self.frame_botoes.pack(side=RIGHT)

        i = 0
        lista = ['<x', '+', '-', '*', '/']
        while(i < 5):

            Button(self.frame_botoes,text=lista[i],font=('arial', 15, 'bold'),
            command=lambda:self.acao_tela(i)).grid(row=i, column=i, padx=10, pady=5)

            i += 1
