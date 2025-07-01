from socket import *

# Opening socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')


while True:
 # Receiving message
 message, clientAddress = serverSocket.recvfrom(2048)
 modifiedMessage = message.decode().upper()

 # Sending message
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)