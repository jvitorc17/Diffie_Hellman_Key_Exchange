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

KprA = random.choice([x for x in range(2,p-1)])
KpubA = (a**KprA)%p
tcp.send(str(KpubA).encode())

KpubB = tcp.recv(1024)
KpubB = KpubB.decode()

Km = (int(KpubB)**KprA)%p

print("Chave privada Alice: ",KprA)
print("Chave publica Alice: ", KpubA)
print("Chave publica Bob: ",KpubB)
print("**************************")
print("Chave da mensagem: ",Km)
print("**************************")

msg = input()
msg = (int(msg)**Km)%p
while(str(msg) != '\x18'):
	tcp.send(str(msg).encode())
	rq = tcp.recv(1024)
	print("Mensagem de Bob: ", (int(rq.decode())**Km)%p)
	msg = input()
	msg = (int(msg)**Km)%p
tcp.close()
