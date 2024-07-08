import tkinter as tk
from tkinter import ttk

notas = ["C", "D", "E", "F", "G", "A", "B"]
tmpArray = []
tmpMaior = []
tmpMenor = []

def on_button_click():
    selected_item = combobox.get()

    if selected_item == "C":
        index = 0
        calcula(index)
    if selected_item == "D":
        index = 1
        calcula(index)
    if selected_item == "E":
        index = 2
        calcula(index)
    if selected_item == "F":
        index = 3
        calcula(index)
    if selected_item == "G":
        index = 4
        calcula(index)
    if selected_item == "A":
        index = 5
        calcula(index)
    if selected_item == "B":
        index = 6
        calcula(index)

def calcula(index):
    tmpArray.clear()
    tmpMaior.clear()
    tmpMenor.clear()
    for i in range(index, len(notas)):
        if i == 1 or i == 2 or i == 5:
            tmpMaior.append(notas[i] + "m")
        elif i==6:
            tmpMaior.append(notas[i] + "dim")
        else:
            tmpMaior.append(notas[i])
        
        if i == 0 or i == 3 or i == 4:
            tmpMenor.append(notas[i] + "m")
        elif i==1:
            tmpMenor.append(notas[i] + "dim")
        else:
            tmpMenor.append(notas[i])
        
        # tmpArray.append(notas[i])
    for i in range(0, index):
        tmpArray.append(notas[i])
    # print(tmpArray)
    # print("------------")
    print(tmpMaior)
    print("------------")
    print(tmpMenor)
    print("------------")


    # M m m M M m dim

    # m dim M m m M M

# Criar a janela principal
root = tk.Tk()
root.title("Aplicativo Tkinter")
root.geometry("400x300")

# Criar um rótulo (label)
label = tk.Label(root, text="Digite algo e clique no botão", font=("Arial", 14))
label.pack(pady=20)

# Criar uma Combobox
combobox = ttk.Combobox(root, values=notas, font=("Arial", 12))
combobox.pack(pady=10)
combobox.set("C")

# Criar um botão para exibir a entrada
button = tk.Button(root, text="Mostrar Escala", command=on_button_click, font=("Arial", 12))
button.pack(pady=10)



# Iniciar o loop principal
root.mainloop()
