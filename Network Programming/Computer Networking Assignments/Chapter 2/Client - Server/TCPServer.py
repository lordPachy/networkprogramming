from socket import *
import re
import random

# Opening socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 12004
serverSocket.bind(('',serverPort))

# Opening serverConnection
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # Opening connectionSocket
    connectionSocket, addr = serverSocket.accept()

    # Receiving message
    sentence = connectionSocket.recv(1024).decode()
    clientName = re.findall("[a-zA-Z]+", sentence)[0]  # Extracting letters
    clientNumber = re.findall("[0-9]+", sentence)[0]  # Extracting numbers
    clientNumber = int(clientNumber)

    # Processing request
    print('Server of Francesco Calzona')
    print(clientName)
    serverNumber = random.randint(1, 100)
    print(f"Client's number: {clientNumber}")
    print(f"Server's number: {serverNumber}")
    print(f"Sum: {clientNumber + serverNumber}")

    # Sending message
    sentence = "Server of Francesco Calzona " + str(serverNumber)
    connectionSocket.send(sentence.encode())

    # Closing connectionSocket
    connectionSocket.close()

    # Closing serverSocket if it has received a bad request
    if clientNumber not in range(1, 101):
        serverSocket.close()
        break