import tkinter as tk

from controler.user_c import UsuarioController
from model.usuario_m import UsuarioModel
from view.user_v import UsuarioView
UsuarioView.check_name()
print(f"modulo: {__name__}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = UsuarioView(root)
    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()
