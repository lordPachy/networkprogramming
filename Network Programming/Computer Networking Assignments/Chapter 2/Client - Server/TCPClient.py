from socket import *
import re

# Opening socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting to server
serverName = 'PachyPC'
serverPort = 12004
clientSocket.connect((serverName,serverPort))

# Sending message
clientNumber = input('Input number between between 1 and 100:')
clientNumber = int(clientNumber)
clientName = 'Client of Francesco Calzona'
sentence = clientName + str(clientNumber)
clientSocket.send(sentence.encode())

# Receving message
serverMessage = clientSocket.recv(1024).decode()

# Processing received message
serverName = re.findall("[a-zA-Z]+", serverMessage)[0]  # Extracting letters
serverNumber = re.findall("[0-9]+", serverMessage)[0]  # Extracting numbers
serverNumber = int(serverNumber)

print(f"Client's name: Client of Francesco Calzona")
print(f"Server's name: {serverName}")
print(f"Client's number: {clientNumber}")
print(f"Server's number: {serverNumber}")
print(f"Sum: {clientNumber + serverNumber}")

# Closing socket and connection (since the connection
# is attached to it)
clientSocket.close()