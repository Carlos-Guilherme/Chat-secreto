# Chat Secreto Com MySQL

Este é um aplicativo de bate-papo simples criado em Python usando MySQL como banco de dados para armazenar informações de usuários e mensagens. Ele permite que os usuários criem uma conta, façam login e enviem mensagens em um chat secreto.
## Requisitos

- Python 3.x
- Módulo mysql-connector-python

## Instalação
Antes de executar o código, você precisa instalar o módulo mysql-connector-python. Você pode fazer isso usando o comando pip:
```bash
pip install mysql-connector-python
```
## Uso
1 - Execute o script.

2 - Escolha entre criar uma conta (opção 1) ou fazer login (opção 2).
  - Se você escolher criar uma conta, insira um nome de usuário e senha. O programa solicitará que você repita a senha para garantir a precisão.
  - Se você escolher fazer login, insira seu nome de usuário e senha.
    
3 - Após o login bem-sucedido, você poderá enviar mensagens e ver o histórico de mensagens do chat secreto.
  - Para enviar uma mensagem, escolha a opção 1, digite sua mensagem e pressione Enter.
  - Para atualizar o chat e ver novas mensagens, escolha a opção 2.
  - Para fazer logoff, escolha a opção 3.

## Estrutura do Banco de Dados

### O aplicativo utiliza duas tabelas no banco de dados MySQL:
- banco_2: Armazena informações de usuários.
    - Campos: id (chave primária e autoincrementável), usuario (nome de usuário), senha (senha do usuário).
- data_2: Armazena mensagens do chat secreto.
    - Campos: id (chave primária e autoincrementável), usuario (nome de usuário que enviou a mensagem), texto (conteúdo da mensagem).
 
## Notas
- Este aplicativo de bate-papo utiliza uma conexão ao banco de dados MySQL. Certifique-se de ter uma criado o banco de dados no MySQL em seu computador para acessar o banco de dados ou se conecte em um banco de dados na nuvem.
- As senhas são armazenadas no banco de dados como texto simples para fins de simplicidade. Em um ambiente de produção, é altamente recomendável usar técnicas de hash e sal para armazenar senhas de forma segura.

Este aplicativo de bate-papo utiliza uma conexão ao banco de dados MySQL hospedado na nuvem (host='aws.connect.psdb.cloud'). Certifique-se de ter uma conexão de internet estável para acessar o banco de dados.
As senhas são armazenadas no banco de dados como texto simples para fins de simplicidade. Em um ambiente de produção, é altamente recomendável usar técnicas de hash e sal para armazenar senhas de forma segura.
