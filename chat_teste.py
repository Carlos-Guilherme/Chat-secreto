import mysql.connector
import time
import os

conexao = mysql.connector.connect(
    host='',
    user='',
    password='',
    database='',
)

cursor = conexao.cursor()

comando = ('CREATE TABLE IF NOT EXISTS banco_2 (id INT PRIMARY KEY AUTO_INCREMENT, usuario text, senha text)')
cursor.execute(comando)

comando = ('CREATE TABLE IF NOT EXISTS data_2 (id INT PRIMARY KEY AUTO_INCREMENT, usuario text, texto text)')
cursor.execute(comando)

os.system('cls')
print('1 - criar conta')
print('2 - fazer login')
resposta = input(str('digite: '))
match resposta:
    case '1':
        while True:
            user = input(str('username:'))
            os.system('cls') 
            passwd = input(str('senha:'))
            os.system('cls') 
            passwd_2 = input(str('repita a senha:'))
            os.system('cls') 
            if passwd_2 != passwd:
                print('senha não bate')
            
            else:
                comando = (f'INSERT INTO banco_2 (usuario, senha) VALUES ("{user}", {passwd})')
                cursor.execute(comando)
                conexao.commit()
                os.system('cls') 
                print('pode fazer login')
                break
    case '2':
        os.system('cls')
        user = input(str('username:'))
        os.system('cls') 
        passwd = input(str('senha:'))
        os.system('cls') 

        # Consulta SQL para verificar o usuário e senha na tabela "banco_2"
        consulta = ("SELECT * FROM banco_2 WHERE usuario = %s AND senha = %s")
        valores = (user, passwd)

        # Execute a consulta
        cursor.execute(consulta, valores)

        # Verifique se o usuário e senha correspondem a algum registro na tabela
        if cursor.fetchone():
            print("Login bem-sucedido!")
            time.sleep(1)
            while True:
                cursor.execute('SELECT * FROM data_2')
                resultado = cursor.fetchall()
                os.system('cls') 
                print('##### CHAT SECRETO #####')
                for linha in resultado:
                    print(f'{linha[1]} disse: {linha[2]}')

                time.sleep(1)
                print('################################')
                print('1 - enviar mensagem')
                print('2 - atualizar chat')
                print('3 - fazer logoff')
                resposta = input(str('Digite: '))
                match resposta:
                    case '1':
                        conexao = mysql.connector.connect(
                            host='aws.connect.psdb.cloud',
                            user='60r8y0qxmtz9l9noesu5',
                            password='pscale_pw_4ZxTtrQ7y2FPb63mbAqsJDBBszpyMDNnSXw1yaOIW5Q',
                            database='banco',
                        )
                        cursor = conexao.cursor()

                        msg = input(str('digite uma mensagem:'))
                        comando = f'INSERT INTO data_2 (usuario, texto) VALUES ("{user}", "{msg}")'
                        cursor.execute(comando)
                        conexao.commit()
                    case '2':
                        conexao = mysql.connector.connect(
                            host='aws.connect.psdb.cloud',
                            user='60r8y0qxmtz9l9noesu5',
                            password='pscale_pw_4ZxTtrQ7y2FPb63mbAqsJDBBszpyMDNnSXw1yaOIW5Q',
                            database='banco',
                        )
                        cursor = conexao.cursor()

                        cursor.execute('SELECT * FROM data_2')
                        resultado = cursor.fetchall()
                        print('##### CHAT SECRETO #####')
                        for linha in resultado:
                            print(f'{linha[1]} disse: {linha[2]}')
                    case '3':
                        break

        else:
            print("Usuário ou senha incorretos.")