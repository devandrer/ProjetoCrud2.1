#ANDRÉ RICARDO BORGES
from tkinter import *

class Janela: # classe para criar janela de iniciação.
    def __init__(self, instancia_de_Tk):#função inicializar o tkinter
        principal = Menu(instancia_de_Tk) #criando o menu e declarando a variavel para inicializar.
        arquivo = Menu(principal) #criando a opção no menu "arquivo"
        arquivo.add_command(label="Abrir",command=self.abrir) #comando para adicionar uma label "abrir" como submenu em "arquivo"
        arquivo.add_command(label="Salvar",command=self.salvar) #comando para adicionar uma label "salvar" como submenu em "arquivo"
        principal.add_cascade(label="Arquivo",menu=arquivo) #criar uma label "arquivo" no menu
        principal.add_command(label="Ajuda",command=self.ajuda) # criando uma label "ajuda" no menu
        instancia_de_Tk.configure(menu=principal) #a função configure permite que o 
        l1 = Label(text="André Ricardo Borges",foreground="black");l1.pack() #criado uma label para colocar meu nome no trabalho
        l1.configure(font="Arial 24 bold",border=5) #criado para adicionar fonte e ajustar o nome no trabalho
    def abrir(self): print,"abrir" #metodo para apresentar a mensagem "abrir"
    def salvar(self): print,"salvar" #metodo para apresentar a mensagem "salvar"
    def ajuda(self): print,"ajudar" #metodo para apresentar a mensagem "ajudar"
    
raiz = Tk() # 
Janela(raiz)
raiz.mainloop()