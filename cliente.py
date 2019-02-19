import socket
import time

#criacao de uma funcao para o recebimento do arquivo, passando como parametro o nome do arquivo
def receberArquivo(nomeArquivo):
    with open('caminho'+nomeArquivo, 'wb') as file:
        print("Abrindo arquivo ...")
        time.sleep(5)
        print("Arquivo aberto")
        while True:
            print("Recebendo dados ...")
            data = socket.recv(1024)
            print('%s', data)
            if not data:
                break
            file.write(data)
    file.close()
    print("Tranferencia completa")
    socket.close()
    print("Conexao encerrada")


#definição do host e da porta
host = 'localhost'
port = 6464

#criação do socket tcp/ip
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

print("""   LISTA DE COMANDOS
        [1] - Wallpaper 1
        [2] - Wallpaper 2
        [3] - Wallpaper 3
        [4] - Wallpaper 4
        [0] - Sair
        """)
#pega a opcao desejada
op = input('Insira a opção desejada: ')
#pega a opcao do usuario guarda em outra variavel e o que o usuario digitou fica tudo minusculo
verificarComando = op.lower()
#envia para o servidor o comando do usuario codificado em utf8
socket.send(verificarComando.encode('utf-8'))

#verifica o comando que o usuario digitou e faz o recebimento do arquivo
if verificarComando == '1':
    receberArquivo('arqRecebido1.jpg')
elif verificarComando == '2':
    receberArquivo('arqRecebido2.jpg')
elif verificarComando == '3':
    receberArquivo('arqRecebido3.jpg')
elif verificarComando == '4':
    receberArquivo('arqRecebido4.jpg')
else:
    print('Digite uma opção válida!')
