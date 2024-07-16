    
import tkinter as tk

class MenuView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    #view = DeleteView(root)
    #controller = DeleteController(view, model)
   

    def opcao_selecionada(self,opcao):
        self.title(f'Opção selecionada: {opcao}')



    # Função para criar um menu dropdown
    def criar_menu_dropdown(master):
        menu_dropdown = tk.Menu(master, tearoff=0)
        menu_dropdown.add_command(label="Opção 1", command=lambda: opcao_selecionada("Opção 1"))
        menu_dropdown.add_command(label="Opção 2", command=lambda: opcao_selecionada("Opção 2"))
        menu_dropdown.add_command(label="Opção 3", command=lambda: opcao_selecionada("Opção 3"))
        return menu_dropdown

    def create_widgets(self):
        # Criar um Menubutton para mostrar o menu dropdown
        mb = tk.Menubutton(self, text="Escolha uma opção", relief=tk.RAISED)
        mb.menu = self.criar_menu_dropdown(mb)  # Associa o menu dropdown ao Menubutton
        mb["menu"] = mb.menu  # Define o menu dropdown como o menu do Menubutton
        mb.pack(anchor="e",pady=12,padx=12)
