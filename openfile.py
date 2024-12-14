import os
from os.path import isfile, exists
from sys import argv
import tkinter as tk
from tkinter import messagebox
path= ' '.join(argv[1:])

def popup(titulo, conteudo):
    messagebox.showinfo(titulo, conteudo)
if path and (exists(path) and isfile(path)):
    try:
        if os.path.isabs(path):
            pass
        else: path= os.path.abspath(path)
        janela= tk.Tk()
        janela.title(f'Arquivo [ {path} ]')
        janela.geometry('500x550')
        frame= tk.Frame(janela, bg= 'silver')
        frame.pack_propagate(False)
        frame.pack(fill= tk.BOTH, expand= True)
        # Cria um Scrollbar
        scrollbar = tk.Scrollbar(frame, orient= tk.VERTICAL)
        scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
        # Cria um Scrollbar
        scrollbarB = tk.Scrollbar(frame, orient= tk.HORIZONTAL)
        scrollbarB.pack(side= tk.BOTTOM, fill= tk.X)
        ftext= tk.Frame(frame, bg= 'green')
        ftext.pack(fill= tk.BOTH, expand= True)
        text= tk.Text(ftext, wrap= 'none')
        text.pack(fill= tk.BOTH, expand= True)
        # Configuração da tag de realce
        text.tag_configure('keyword', foreground='red')
        scrollbar['command']= text.yview
        scrollbarB['command']= text.xview
        text['yscrollcommand']= scrollbar.set
        text['xscrollcommand']= scrollbarB.set
        f= open(path, 'r')
        data= f.read()
        f.close()
        text.insert(tk.END, data)

        def salvar():
            data= text.get('1.0', tk.END)
            f= open(path, 'w')
            f.write(data)
            popup('Salvo', 'Alteração feita com sucesso.')
        text.bind('<Control-s>', lambda event: salvar())
        janela.mainloop()
    except PermissionError:
        janela.quit()
        popup('Erro', f'Acesso negado a {path}')
    except Exception as e:
        janela.quit()
        popup('Erro', e)
