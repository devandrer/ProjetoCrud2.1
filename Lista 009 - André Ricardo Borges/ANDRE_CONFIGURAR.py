#ANDRÉ RICARDO BORGES
from tkinter import *

class Janela:
    def __init__(self, instancia_de_Tk):
        top = Frame();top.pack() #classe "frame" e encaixa na janela principal
        l1 = Label(top,text="André Ricardo Borges",foreground="blue");l1.pack() #criado uma label para colocar meu nome no trabalho
        l1.configure(relief="ridge",font="Arial 24 bold",border=5,background="light blue") #criado para adicionar fonte e ajustar o nome no trabalho

raiz=Tk()
Janela(raiz)
raiz.mainloop()
