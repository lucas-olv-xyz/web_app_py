# 📝 Flask Blog CRUD com Autenticação

Este projeto é uma aplicação web desenvolvida com Flask que implementa um sistema de CRUD para posts e um sistema de autenticação de usuários utilizando SQLite como banco de dados. A aplicação permite criar, atualizar, deletar e visualizar posts, além de oferecer as funcionalidades de cadastro (signup), login e logout de usuários.

---

## 🚀 Funcionalidades

- **Posts**

  - Criação de novos posts.
  - Atualização de posts existentes.
  - Remoção de posts.
  - Listagem dos posts (ordenados por data).

- **Autenticação de Usuários**

  - Cadastro (signup) de novos usuários.
  - Login com verificação de senha (utilizando hash).
  - Logout e gerenciamento de sessão.

- **Rotas Protegidas**
  - Rotas protegidas que redirecionam para o login se o usuário não estiver autenticado.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Flask**: Framework web para Python.
- **SQLite**: Banco de dados utilizado para armazenar os posts e usuários.
- **Werkzeug**: Utilizado para gerar e verificar hashes de senhas.
- **Session do Flask**: Para gerenciamento de sessões e autenticação.

---

## ▶️ Como Executar

1. **Clone o repositório** ou copie os arquivos para o seu ambiente de desenvolvimento.

2. **Instale as dependências** (por exemplo, utilizando um ambiente virtual):

   ```bash
   pip install flask werkzeug
   ```

3. **Crie os bancos de dados**:

   - Crie um arquivo `posts.db` com uma tabela `posts` contendo colunas como `id`, `title`, `content`, `author` e uma coluna para data/hora (se necessário).
   - Crie um arquivo `users.db` com uma tabela `users` contendo colunas como `id`, `username`, `email` e `password`.
   - Certifique-se de que as estruturas das tabelas estejam de acordo com as queries utilizadas no código.

4. **Configure a chave secreta** (caso deseje alterar):

   ```python
   app.secret_key = "secret_key"
   ```

5. **Execute a aplicação**:

   ```bash
   python nome_do_arquivo.py
   ```

6. Acesse a aplicação no navegador através de:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📄 Estrutura das Rotas

- **Posts**

  - `GET /posts`: Exibe a lista de posts.
  - `GET/POST /create`: Página para criar um novo post.
  - `GET/POST /update/<int:id>`: Página para atualizar um post existente.
  - `GET /delete/<int:post_id>`: Remove o post especificado.

- **Usuários**

  - `GET/POST /signup`: Página de cadastro de novo usuário.
  - `GET/POST /login`: Página de login.
  - `GET /logout`: Encerra a sessão do usuário.

- **Index**
  - `GET /`: Página inicial que exibe o nome do usuário autenticado.

---

## ⚠️ Observações

- **Banco de Dados**: Certifique-se de criar e configurar corretamente os bancos de dados (`posts.db` e `users.db`) e suas respectivas tabelas.
- **Autenticação**: O trecho do login utiliza uma consulta ao modelo `user` (exemplo: `user.query.filter_by(email=email).first()`) que pode precisar de ajustes, visto que o código atual utiliza SQLite diretamente em outras partes. Adapte-o conforme sua implementação.
- **Segurança**: Embora o uso do `generate_password_hash` e `check_password_hash` seja recomendado, revise e teste o fluxo de autenticação para garantir a segurança da aplicação.

---

## 🧪 Exemplo de Uso

Ao acessar a rota `/signup`, um novo usuário é criado e autenticado automaticamente, redirecionando para a página inicial (`/`). Em seguida, o usuário pode acessar a rota `/posts` para gerenciar os posts.

---

## 📄 Licença

Este projeto é livre para uso e aprendizado. Sinta-se à vontade para modificar e expandir conforme suas necessidades.
