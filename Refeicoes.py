import tkinter as tk
from tkinter import *
import mysql.connector

cor = '#636e72'

window = Tk()
window.title('Refeições')



"4169E1"


frame = tk.Frame(window, bg = cor, highlightbackground="black", highlightthickness=1)

label_comida = tk.Label(frame, text = 'Alimento:', bg = cor, font=('Arial', 14), highlightbackground="black", highlightthickness=1)
entry_comida = tk.Entry(frame, font=('Arial', 14))
label_comida.grid(row=0, column=0, padx = 5, pady= 5)
entry_comida.grid(row=0, column=1, padx =5, pady= 5)

label_tipo = tk.Label(frame, text = 'Tipo Nutricional:', bg = cor, font=('Arial', 14), highlightbackground="black", highlightthickness=1)
entry_tipo = tk.Entry(frame, font=('Arial', 14))
label_tipo.grid(row=1, column=0, padx = 5, pady= 5)
entry_tipo.grid(row=1, column=1, padx = 5, pady= 5)

label_calorias = tk.Label(frame, text = 'Calorias:', bg = cor, font=('Arial', 14), highlightbackground="black", highlightthickness=1)
entry_calorias = tk.Entry(frame, font=('Arial', 14))
label_calorias.grid(row=2, column=0, padx = 5, pady= 5)
entry_calorias.grid(row=2, column=1, padx = 5, pady= 5)


label_periodo = tk.Label(frame, text = 'Período:', bg = cor, font=('Arial', 14), highlightbackground="black", highlightthickness=1)
entry_periodo = tk.Entry(frame, font=('Arial', 14))
label_periodo.grid(row=3, column=0, padx = 5, pady= 5)
entry_periodo.grid(row=3, column=1, padx = 5, pady= 5)


"PARTE MYSQL"

connect = mysql.connector.connect(host='localhost', user = 'root', password = '', port = '3306', database = 'dbcomidas')
cursor = connect.cursor()

def dados_envio():
    comida = entry_comida.get()
    tipo = entry_tipo.get()
    periodo = entry_periodo.get()
    calorias = entry_calorias.get()

    envio_db = "INSERT INTO `comidas` (nome, tipo, calorias, periodo) VALUES (%s, %s, %s, %s)"
    dados = (comida, tipo, calorias, periodo)
    cursor.execute(envio_db, dados)
    connect.commit()

botao_enviar = tk.Button(frame, text='Enviar', bg=cor, font='Arial', command=dados_envio)
botao_enviar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

frame.pack()

window.mainloop()



