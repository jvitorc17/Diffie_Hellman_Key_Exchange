import socket
import random
HOST = ''              # Endereco IP do Servidor
PORT = 5019            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

#Set-up
# Choose a large prime p
p = 17
# Escolha um inteiro a entre {2,3, ... , p-2}
a = random.choice([x for x in range(2,p-1)])
#public a e p

print("p:",p)
print("a:",a)

while True:
    con, cliente = tcp.accept()
    con2, cliente2 = tcp.accept()
    print('Conectado por ALICE: ', cliente)
    print('Conectado por BOB: ',cliente2)
    con.send((str(a)+" "+str(p)).encode())
    con2.send((str(a)+" "+str(p)).encode())
    KpubA = con.recv(1024) #chave publica Alice
    KpubB = con2.recv(1024) # chave publica Bob
    con2.send(KpubA)
    con.send(KpubB)

    while True:
	#recebe a mensagem de ambos os clientes conectados
        msg = con.recv(1024)
        print("Mensagem interceptada: "+msg.decode())
        con2.send(msg)
        msg2 = con2.recv(1024)
        print("Mensagem interceptada: "+msg2.decode())
        con.send(msg2)

    con.close()
    con2.close()
