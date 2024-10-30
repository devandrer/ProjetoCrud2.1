#ANDRÉ RICARDO BORGES
from tkinter import *

class Janela:#Define uma classe chamada "Janela", que representa uma janela de interface gráfica.
    def __init__(self, instancia_de_Tk): #Método construtor da classe "Janela" é criada. Recebe `instancia_de_Tk`
        top = Frame();top.pack() #classe "frame" e encaixa na janela principal
        a = Label(top,text="A");a.pack(side="left",fill="y") #cria um label com letra "A" ao lado esquerdo, na direção vertical
        b = Label(top,text="B");b.pack(side="bottom",fill="x") #cria uma label com letra "B" abaixo por conta de o side estar bottom, na direção horizontal
        c = Label(top,text="C");c.pack(side="right") #cria um Label com o texto "C" e o encaixa à direita
        d = Label(top,text="D");d.pack(side="top") #cria um Label com o texto "D" e o encaixa na parte superior
        l1 = Label(text="André Ricardo Borges",foreground="black");l1.pack() #criado uma label para colocar meu nome no trabalho
        l1.configure(font="Arial 24 bold",border=5) #criado para adicionar fonte e ajustar o nome no trabalho
        for widget in (a,b,c,d): #uma tupla de widgets (a, b, c, d).
            widget.configure(relief="groove",border=10,font="Times 24 bold") #Configura cada widget com um estilo de borda, fonte e seu tamanho 

raiz=Tk()
Janela(raiz)
raiz.mainloop()