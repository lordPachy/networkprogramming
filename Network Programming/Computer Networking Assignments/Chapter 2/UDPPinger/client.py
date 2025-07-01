# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *
import time


# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Setting server address
address = ("PachyPC", 12000)

for i in range(1, 11):
    message = f"Ping {i}".encode()

    # Sending ping and start timer
    start = time.time()
    clientSocket.sendto(message, address)
    clientSocket.settimeout(1.0)

    try:
        message, address = clientSocket.recvfrom(1024)
        end = time.time()
        print(message.decode())
        print(f"Round trip time: {end-start}")
    except:
        print("Request timed out")

clientSocket.close()





