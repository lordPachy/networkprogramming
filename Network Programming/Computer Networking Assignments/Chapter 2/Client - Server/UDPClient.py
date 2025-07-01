from socket import *

# Opening socket:
# AF_INET = IPv4
# SOCK_DGRAM = port decided by OS
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Setting destination
serverName = 'PachyPC'
serverPort = 12000

# Sending message
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))

# Receiving message
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

# Closing socket
clientSocket.close()