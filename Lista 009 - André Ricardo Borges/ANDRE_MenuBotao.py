#ANDRÉ RICARDO BORGES
from tkinter import *

class Janela: #Define uma classe chamada "Janela", que representa uma janela de interface gráfica.
    def __init__(self, instancia_de_Tk): #Método construtor da classe "Janela" é criada. Recebe "instancia_de_Tk"
        self.menu = Menu(instancia_de_Tk,tearoff=0) #Cria um menu "Menu" associado à instância de Tk. "tearoff=0" desativa a opção de "destacar" o menu.
        self.menu.add_command(label="Ola 1", command=self.ola) #Adiciona um item de menu com o rótulo "Ola 1", que chama o método "ola" quando selecionado.
        self.menu.add_command(label="Ola 2", command=self.ola) #Adiciona um segundo item de menu com o rótulo "Ola 2", que também chama o método "ola".

        frame = Frame(instancia_de_Tk, width=200,height=200) #Cria um novo frame (uma área de contenção) na janela principal, com largura e altura de 200 pixels.
        frame.pack() #Adiciona o frame à interface gráfica de forma automática.
        frame.bind("<Button-3>",self.popup) #Associa um evento de clique com o botão direito do mouse (Button-3) ao método "popup", que exibirá o menu.
        l1 = Label(text="André Ricardo Borges",foreground="black");l1.pack() #criado uma label para colocar meu nome no trabalho
        l1.configure(font="Arial 24 bold",border=5) #criado para adicionar fonte e ajustar o nome no trabalho
        mainloop() #Inicia o loop principal da interface gráfica, permitindo que a janela permaneça aberta e interativa
    
    def ola(self): #Define um método chamado "ola" que é chamado quando um item de menu é selecionado.
        print("Olá") #Imprime "Olá" no console.
    
    def popup(self,e): #Define um método chamado "popup" que é chamado quando o evento de clique com o botão direito ocorre.
        self.menu.post(e.x_root,e.y_root) #Exibe o menu no local do cursor do mouse (coordenadas x e y do evento).

raiz = Tk() #Cria uma nova instância da classe Tk, que representa a janela principal da aplicação gráfica. Essa janela servirá como a base para outros widgets.
Janela(raiz) #Cria uma nova instância da classe "Janela", passando "raiz" como argumento. Isso inicializa a interface gráfica definida na classe `Janela`.
raiz.mainloop() #Inicia o loop principal da aplicação. Isso mantém a janela aberta e em execução, permitindo que o usuário interaja com a interface até que a janela seja fechada.