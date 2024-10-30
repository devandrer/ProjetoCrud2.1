#ANDRÉ RICARDO BORGES
from tkinter import *

class Janela:
    def calcular_imc(self): #Metodo "calcular_imc" para fazer o calculo do IMC
        #Variavel para receber as informações que o cliente vai colcoar em peso altura e fazer o calculo do IMC
        peso = float(self.spin_peso.get())*100 
        altura = float(self.spin_altura.get())
        imc = (peso/(altura*altura))*100

        #If para verificar os valores somados do IMC masculino e informar se está abaixo do peso, no peso normal, marginalmente acima do peso, acima do peso ou obesa.
        if self.rb_value.get() == 1: #Masculino
            if imc<20.7:
                self.v.set("abaixo do peso")
            elif 20.7< imc<26.4:
                self.v.set("no peso normal")
            elif 26.4< imc<27.8:
                self.v.set("Marginalmente acima do peso")
            elif 27.8< imc<31.1:
                self.v.set("Acima do peso ideal")
            elif imc>31.1:
                self.v.set("Obeso")
        #If para verificar os valores somados do IMC feminino e informar se está abaixo do peso, no peso normal, marginalmente acima do peso, acima do peso ou obesa.
        if self.rb_value.get() == 2: #Feminino
            if imc<19.1:
                self.v.set("abaixo do peso")
            elif 19.1< imc<25.8:
                self.v.set("no peso normal")
            elif 25.8< imc<27.3:
                self.v.set("Marginalmente acima do peso")
            elif 27.3< imc<32.3:
                self.v.set("Acima do peso ideal")
            elif imc>32.3:
                self.v.set("Obesa")
    #Método construtor da classe, recebe uma instância de Tk como parâmetro.       
    def __init__(self,instancia_de_Tk):
        #Criando e configurando os frames para cada função.
        frame1 = Frame(instancia_de_Tk)
        frame1.configure(border=5);frame1.pack()
        frame2 = Frame(instancia_de_Tk)
        frame2.configure(border=5);frame2.pack()
        frame3 = Frame(instancia_de_Tk)
        frame3.configure(border=5);frame3.pack()
        frame4 = Frame(instancia_de_Tk)
        frame4.configure(border=5);frame4.pack()

        label1 = Label(frame1,text="Nome");label1.pack() #Cria um Label com o texto "Nome" no frame1 e o empacota
        entry1 = Entry(frame1);entry1.pack() #Cria um campo de entrada no frame1 e o empacota
        label2 = Label(frame1,text="Sexo");label2.pack() #Cria um Label com o texto "Sexo" no frame1 e o empacota

        self.rb_value = IntVar()#Cria uma variável inteira para armazenar o valor do botão de rádio.
        self.rb1 = Radiobutton(frame2,text="Masculino",value=1,variable=self.rb_value).pack(anchor=W) #Cria um botão de rádio para "Masculino", associando-o à variável rb_value, e o empacota à esquerda.
        self.rb1 = Radiobutton(frame2,text="Feminino",value=2,variable=self.rb_value).pack(anchor=W) #Cria um botão de rádio para "Feminino", associando-o à mesma variável, e o empacota à esquerda.

        self.altura = DoubleVar()#Cria uma variável de ponto flutuante para armazenar a altura.
        label3 = Label(frame3,text="Altura(cm):");label3.pack() #Cria um Label com o texto "Altura(cm):" no frame3 e o empacota.
        self.spin_altura = Spinbox(frame3, from_=0, to=150);self.spin_altura.pack() #Cria um Spinbox para selecionar a altura entre 0 e 150 cm e o empacota.
        
        self.peso = IntVar() #Cria uma variável inteira para armazenar o peso.
        label3 = Label(frame3,text="Peso(kg):");label3.pack() #Cria um Label com o texto "Peso(kg):" no frame3 e o empacota.
        self.spin_peso = Spinbox(frame3, from_=0, to=150);self.spin_peso.pack() #Cria um Spinbox para selecionar o peso entre 0 e 150 kg e o empacota.

        label4 = Label(frame4,text="Resultado:");label4.pack() #Cria um Label com o texto "Resultado:" no frame4 e o empacota.

        self.v = StringVar() #Cria uma variável de string para armazenar o resultado.
        label5 = Label(frame4,text="",textvariable=self.v);label5.pack() #Cria um Label que exibirá o texto armazenado em v e o empacota.

        button1 = Button(instancia_de_Tk,text="OK",command=self.calcular_imc);button1.pack() #Cria um botão com o texto "OK" que, ao ser clicado, chama o método calcular_imc e o empacota.
        l1 = Label(text="André Ricardo Borges",foreground="red");l1.pack() #Cria um Label com o texto "André Ricardo Borges" em vermelho e o empacota.
        l1.configure(font="Arial 24 bold",border=5) #Configura a fonte do Label l1 para Arial, tamanho 24, negrito e define uma borda de 5 pixels.
raiz=Tk()
Janela(raiz)
raiz.title("Calculadora IMC")
raiz.mainloop()