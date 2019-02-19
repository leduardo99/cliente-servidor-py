import socket
import threading

port = 6464
host = 'localhost'

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.bind((host, port))
socket.listen(10)

print("[*] ESPERANDO CONEXÃO ...")


def conectarSocket(socket, adrr):
    print("Recebendo conexão de {}".format(adrr))
    msgCliente = socket.recv(2543616).decode('utf-8')

    if msgCliente == '1':
        #abre o arquivo
        file = open('caminho', 'rb')
        #le 1024 bytes do arquivo
        l = file.read(1024)
        #enquanto tiver algo no arquivo ele vai enviando para o cliente a cada 1024 bytes
        while l:
            #enviar para o cliente parte a parte o arquivo
            socket.send(l)
            print('Enviado ', repr(l))
            l = file.read(1024)
        #fecha o arquivo
        file.close()
        print("[*] ARQUIVO ENVIADO COM SUCESSO")
        #fecha o socket
        socket.close()
    elif msgCliente == '2':
        file = open('caminho', 'rb')
        l = file.read(1024)
        while l:
            socket.send(l)
            print('Enviado ', repr(l))
            l = file.read(1024)
        file.close()
        print("[*] ARQUIVO ENVIADO COM SUCESSO")
        socket.close()
    elif msgCliente == '3':
        file = open('caminho', 'rb')
        l = file.read(1024)
        while l:
            socket.send(l)
            print('Enviado ', repr(l))
            l = file.read(1024)
        file.close()
        print("[*] ARQUIVO ENVIADO COM SUCESSO")
        socket.close()
    elif msgCliente == '4':
        file = open('caminho', 'rb')
        l = file.read(1024)
        while l:
            socket.send(l)
            print('Enviado ', repr(l))
            l = file.read(1024)
        file.close()
        print("[*] ARQUIVO ENVIADO COM SUCESSO")
        socket.close()
    else:
        socket.close

while True:
    sckt, addr = socket.accept()
    thread = threading.Thread(target=conectarSocket, args=(sckt, addr))
    thread.start()