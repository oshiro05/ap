
📄 Descrição
Aplicativo desktop feito em Python com interface gráfica usando CustomTkinter, voltado para o controle de pequenos estoques de forma simples e acessível. Útil para pequenos comércios e autônomos.
💡 Funcionalidades
    • Login de usuário
    • Cadastro e listagem de produtos
    • Atualização de estoque
    • Verificação de produtos próximos ao vencimento (alerta automático)
    • Cadastro de novos usuários
    • Exibição de data e hora atual no menu principal (Iteração 2)
    • Indicação de produtos com estoque zerado (Iteração 2)
💻 Requisitos para execução
    • Python 3.9 ou superior
    • pip
📆 Instalação
    1. Clone este repositório:
git clone (https://github.com/oshiro05/ap)
cd seu-repositorio
    2. Instale a dependência principal:
pip install customtkinter
    3. Execute a aplicação:
python controle_estoque.py
🔐 Login padrão
Usuário: admin
Senha: admin

especificacao.md
📊 Objetivo do Projeto
Desenvolver uma aplicação simples de controle de estoque para uso pessoal ou por pequenos comércios, com foco em acessibilidade e controle de validade.
⚖️ Tecnologias Utilizadas
    • Python 3.11
    • CustomTkinter (GUI)
    • Tkinter MessageBox
    • datetime
✨ Funcionalidades Iteração 1
    • Tela de login e cadastro de usuários.
    • Cadastro e listagem de produtos com nome, quantidade, validade e fornecedor.
    • Alerta automático para produtos próximos ao vencimento (7 dias).
➕ Melhorias na Iteração 2
    1. Exibição da data e hora atual no menu principal.
    2. Destaque de produtos com estoque zerado no menu principal (via alerta).
📅 Validação
Testado em Windows 10 e Python 3.11. Nenhuma dependência além do customtkinter. Executável diretamente com o comando python.
