import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime

usuarios = {"admin": "admin"}
estoque = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque Acessível")
        self.geometry("600x700")
        self.resizable(False, False)
        self.usuario_logado = None
        self.tela_login()

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def tela_login(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Login", font=("Arial", 24, "bold")).pack(pady=20)
        self.login_entry = ctk.CTkEntry(self, placeholder_text="Usuário")
        self.login_entry.pack(pady=10)
        self.senha_entry = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.senha_entry.pack(pady=10)
        ctk.CTkButton(self, text="Entrar", command=self.verificar_login).pack(pady=20)

    def verificar_login(self):
        usuario = self.login_entry.get()
        senha = self.senha_entry.get()
        if usuarios.get(usuario) == senha:
            self.usuario_logado = usuario
            self.menu_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    def menu_principal(self):
        self.limpar_tela()
        hoje = datetime.now()
        dias_alerta = 7
        proximos = [p for p in estoque if 0 <= (p["validade"] - hoje).days <= dias_alerta]

        if proximos:
            lista = "\n".join(
                [f'- {p["nome"]} (vence em {p["validade"].strftime("%d/%m/%Y")})' for p in proximos]
            )
            messagebox.showwarning("⚠️ Atenção!", f"Produtos próximos ao vencimento:\n\n{lista}")
            
        saudacao = f"Bem-vindo(a), {self.usuario_logado}!"
        ctk.CTkLabel(self, text=saudacao, font=("Arial", 20)).pack(pady=5)    

        ctk.CTkLabel(self, text="📦 Menu Principal", font=("Arial", 24, "bold")).pack(pady=30)

        botoes = [
            ("➕ Cadastrar Novo Produto", self.cadastrar_produto),
            ("🛠 Atualizar Estoque", self.atualizar_estoque),
            ("📋 Listar Estoque", self.listar_estoque),
            ("⏰ Verificar Vencimentos", self.verificar_vencimentos),
            ("👤 Cadastrar Novo Usuário", self.cadastrar_usuario),
            ("🚪 Sair", self.tela_login)
        ]

        for texto, comando in botoes:
            ctk.CTkButton(self, text=texto, width=350, height=40, font=("Arial", 16),
                          command=comando, corner_radius=10).pack(pady=10)

        # ✅ MODIFICAÇÃO AQUI
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
        ctk.CTkLabel(self, text=f"Data e hora atual: {data_atual}", font=("Arial", 12)).pack(pady=10)

    def cadastrar_produto(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Novo Produto", font=("Arial", 24)).pack(pady=20)
        nome = ctk.CTkEntry(self, placeholder_text="Nome do Produto")
        nome.pack(pady=10)
        quantidade = ctk.CTkEntry(self, placeholder_text="Quantidade")
        quantidade.pack(pady=10)
        validade = ctk.CTkEntry(self, placeholder_text="Validade (dd/mm/aaaa)")
        validade.pack(pady=10)
        fornecedor = ctk.CTkEntry(self, placeholder_text="Fornecedor")
        fornecedor.pack(pady=10)

        def salvar():
            try:
                data = datetime.strptime(validade.get(), "%d/%m/%Y")
                estoque.append({
                    "nome": nome.get(),
                    "quantidade": int(quantidade.get()),
                    "validade": data,
                    "fornecedor": fornecedor.get()
                })
                messagebox.showinfo("Sucesso", "Produto cadastrado!")
                self.menu_principal()
            except:
                messagebox.showerror("Erro", "Preencha os dados corretamente.")

        ctk.CTkButton(self, text="Salvar", command=salvar).pack(pady=20)
        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack()

    def atualizar_estoque(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Atualizar Estoque", font=("Arial", 24)).pack(pady=20)

        for produto in estoque:
            frame = ctk.CTkFrame(self)
            frame.pack(pady=5, padx=10, fill="x")

            ctk.CTkLabel(frame, text=produto["nome"], width=140).pack(side="left")
            qnt = ctk.CTkEntry(frame, width=60)
            qnt.insert(0, str(produto["quantidade"]))
            qnt.pack(side="left", padx=5)

            val = ctk.CTkEntry(frame, width=100)
            val.insert(0, produto["validade"].strftime("%d/%m/%Y"))
            val.pack(side="left", padx=5)

            def salvar_atualizacao(p=produto, qnt_field=qnt, val_field=val):
                try:
                    p["quantidade"] = int(qnt_field.get())
                    p["validade"] = datetime.strptime(val_field.get(), "%d/%m/%Y")
                    messagebox.showinfo("Sucesso", f"{p['nome']} atualizado!")
                except:
                    messagebox.showerror("Erro", "Erro ao atualizar produto")

            ctk.CTkButton(frame, text="Salvar", command=salvar_atualizacao).pack(side="right", padx=5)

        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=20)

    def listar_estoque(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Lista de Produtos", font=("Arial", 24)).pack(pady=20)

        for p in estoque:
            texto = f'{p["nome"]} | Qtd: {p["quantidade"]} | Val: {p["validade"].strftime("%d/%m/%Y")} | Forn: {p["fornecedor"]}'
            ctk.CTkLabel(self, text=texto).pack(pady=2)

        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=20)

    def verificar_vencimentos(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Produtos Próximos ao Vencimento", font=("Arial", 20)).pack(pady=20)

        hoje = datetime.now()
        dias_alerta = 7
        proximos = [p for p in estoque if 0 <= (p["validade"] - hoje).days <= dias_alerta]

        if not proximos:
            ctk.CTkLabel(self, text="Nenhum produto próximo ao vencimento.").pack(pady=10)
        else:
            for p in proximos:
                texto = f'{p["nome"]} | Qtd: {p["quantidade"]} | Vence: {p["validade"].strftime("%d/%m/%Y")}'
                ctk.CTkLabel(self, text=texto).pack(pady=2)

        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack(pady=20)

    def cadastrar_usuario(self):
        self.limpar_tela()
        ctk.CTkLabel(self, text="Cadastrar Novo Usuário", font=("Arial", 24)).pack(pady=20)
        nome = ctk.CTkEntry(self, placeholder_text="Nome do Usuário")
        nome.pack(pady=10)
        senha = ctk.CTkEntry(self, placeholder_text="Senha")
        senha.pack(pady=10)

        def salvar():
            if nome.get() and senha.get():
                usuarios[nome.get()] = senha.get()
                messagebox.showinfo("Sucesso", "Usuário cadastrado!")
                self.menu_principal()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos.")

        ctk.CTkButton(self, text="Salvar", command=salvar).pack(pady=20)
        ctk.CTkButton(self, text="Voltar", command=self.menu_principal).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
