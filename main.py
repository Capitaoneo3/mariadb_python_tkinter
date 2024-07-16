import tkinter as tk

from controler.user_c import UsuarioController
from controler.delete_c import DeleteController
from controler.atualiza_c import AtualizaController
from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
from view.delete_v import DeleteView
from view.atualiza_v import AtualizaView

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    #view = DeleteView(root)
    #controller = DeleteController(view, model)
    view = AtualizaView(root)
    controller = AtualizaController(view, model)
    root.mainloop()
    model.fechar_conexao()


