import socket
import random
HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5019            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msgSetUp = tcp.recv(1024)

setUpDecoded = msgSetUp.decode()
l = setUpDecoded.split(' ')
a = int(l[0])
p = int(l[1])

KprB = random.choice([x for x in range(2,p-1)])
KpubB = (a**KprB)%p
tcp.send(str(KpubB).encode())

KpubA = tcp.recv(1024)
KpubA = KpubA.decode()

Km = (int(KpubA)**KprB)%p

print("Chave privada Bob: ",KprB)
print("Chave publica Bob: ", KpubB)
print("Chave publica Alice: ",KpubA)
print("**************************")
print("Chave da mensagem: ",Km)
print("**************************")

msg = input()
msg = (int(msg)**Km)%p
while(str(msg) != '\x18'):
	tcp.send(str(msg).encode())
	rq = tcp.recv(1024)
	print("Mensagem de Alice: ", (int(rq.decode())**Km)%p)
	msg = input()
	msg = (int(msg)**Km)%p
tcp.close()