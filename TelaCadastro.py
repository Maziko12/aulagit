import tkinter as tk
from cachorro import Cachorro
from gato import Gato
from tkinter import messagebox
from tkinter import ttk

lista=[]#lista de animais salvos
def cadastrarVeiculo():#pega os valores da tela cria o objeto manda salvar
    idade = entryIdade.get()
    nome = entryNome.get()
    tipo = varTipo.get()
    porte = entryPorte.get()
    if tipo == "Cachorro":
        c = Cachorro(idade, nome, porte)
        salvar(c)
        messagebox.showinfo("Cadastro", f"{varTipo.get()} cadastrado com sucesso!")
    else:
        g = Gato(idade,nome,porte)
        salvar(g)
        messagebox.showinfo("Cadastro", f"{varTipo.get()} cadastrado com sucesso!")

def salvar(obj):
    lista.append(obj)
    
def atualizarListbox():
    listbox.delete(0,tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

# Criação da janela principal
janela = tk.Tk()
janela.title("Cadastro de pets")
janela.geometry("500x300")#tamanho da tela

#faz com q todo conteudo se ajuste a janela
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

#criando o frame
janelinha = ttk.Notebook(janela)
janelinha.grid(row=0,column=0, sticky="nsew")

#criando as abas
tab1 = ttk.Frame(janelinha)
for i in range(6): # Configura as linhas
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1) # Configura a coluna das labels
tab1.grid_columnconfigure(1, weight=1) # Configura a coluna das entradas

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

#adicionando as tabs na janelinha
janelinha.add(tab1,text="Cadastro")
janelinha.add(tab2,text="Lista")

#tela de Cadastro
#Labels e entradas de texto
tk.Label(tab1, text="Idade:", font=("",15)).grid(row=0, column=0,
sticky="w",padx=10)
entryIdade = tk.Entry(tab1,font=("",15))
entryIdade.grid(row=0, column=1, sticky="nsew",padx=10, pady=5)

tk.Label(tab1, text="Nome:",font=("",15)).grid(row=1, column=0,
sticky="w",padx=10)
entryNome = tk.Entry(tab1,font=("",15))
entryNome.grid(row=1, column=1, sticky="nsew",padx=10, pady=5)

tk.Label(tab1, text="Porte/Raca:",font=("",15)).grid(row=2, column=0,
sticky="w",padx=10)
entryPorte = tk.Entry(tab1,font=("",15))
entryPorte.grid(row=2, column=1, sticky="nsew",padx=10, pady=5)

tk.Label(tab1, text="Tipo:",font=("",15)).grid(row=4, column=0, sticky="w",
padx=10)
varTipo = tk.StringVar(value="Cachorro")

tk.Radiobutton(tab1, text="Cachorro",font=("",15), variable=varTipo,
value="Cachorro").grid(row=4, column=1,sticky="w",padx=10, pady=5)

tk.Radiobutton(tab1, text="Gato",font=("",15), variable=varTipo,
value="Gato").grid(row=4, column=1, sticky="e",padx=10, pady=5)

# Botão de cadastro
tk.Button(tab1, text="Cadastrar", font=("",15),
command=cadastrarVeiculo).grid(row=5, columnspan=2)
listbox = tk.Listbox(tab2)
listbox.config(font=("",15))
listbox.grid(row=0,column=0, sticky="nsew", padx=10,pady=5)

tk.Button(tab2, text="Atualizar",font=("",15),
command=atualizarListbox).grid(row=1, column=0)
# Inicia o loop da interface
janela.mainloop()