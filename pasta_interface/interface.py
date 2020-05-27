from tkinter import *

from Display import Display
from TecladoNumerico import TecladoNumerico
from Operadores import Operadores


class Interface():

    __value = 0

    def setterValue(self):

        pass


    def iniciar_interface(self):

        self.janela = Tk()

        display = Display(self.janela)
        # teclado_numerico = TecladoNumerico(self.janela)
        # operadores = Operadores(self.janela)

        self.janela.title('Calculadora')
        self.janela.geometry('300x320+550+150')
        self.janela.mainloop()


    def __init__(self):

        pass


a = Interface()
a.iniciar_interface()
