from tkinter import *


class TecladoNumerico:

    def __init__(self, container):

        self.janela = container

        # FRAME
        self.frame_numeros = Frame(self.janela, width=200, height=270, bg='red')
        self.frame_numeros.pack(side=LEFT)

        i = 0
        contador = 9
        while(i < 3):

            j = 3
            while(j > 0):

                #self.nome_botao
                Button(self.frame_numeros,text=contador,font=('arial', 15, 'bold'),
                 command=lambda:self.acao_tela(contador)).grid(row=i, column=j, padx=15, pady=10)

                j -= 1
                contador -= 1


            i += 1
