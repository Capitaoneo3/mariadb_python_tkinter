import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AtualizaView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        self.master.geometry("800x400")
    def create_widgets(self):
        self.id_label = ttk.Label(self, text="ID:")
        self.id_label.grid(row=0, column=2, padx=10, pady=5)

        self.id_entry = ttk.Entry(self)
        self.id_entry.grid(row=0, column=3, padx=10, pady=5)

        self.nome_label = ttk.Label(self, text="novo Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=5)

        self.nome_entry = ttk.Entry(self)
        self.nome_entry.grid(row=0, column=1,columnspan=1, padx=10, pady=5)

        self.idade_label = ttk.Label(self, text="nova Idade:")
        self.idade_label.grid(row=1, column=0, padx=10, pady=5)

        self.idade_entry = ttk.Entry(self)
        self.idade_entry.grid(row=1, column=1,columnspan=1, padx=10, pady=5)

        self.atualizar_button = ttk.Button(self, text="Atualizar Dados")
        self.atualizar_button.grid(row=2, column=0, pady=10, padx=10)

        self.usuarios_listbox = tk.Listbox(self)
        self.usuarios_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def get_nome(self):
        return self.nome_entry.get()

    def get_idade(self):
        return self.idade_entry.get()
    def get_id(self):
        id = self.id_entry.get()
        return id

    def adicionar_usuario_lista(self, usuario):
        self.usuarios_listbox.insert(tk.END, f"id {usuario[0]} | {usuario[1]} ({usuario[2]} anos)")
    def show_info(self):
        messagebox.showinfo("Aviso!", "Os campos não podem estar vazios e a idade deve ser digito.")