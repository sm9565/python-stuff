#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a sever socket
   #Fill in start
   serverSocket.bind(("192.168.1.18",13331))
   serverSocket.listen()
   #Fill in end

   while True:
       #Establish the connection
       print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()

       try:
           message = connectionSocket.recv(1024)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()

           #Send one HTTP header line into socket
           connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
               connectionSocket.send("\r\n".encode())
               connectionSocket.close()
           except IOError:
                #Send response message for file not found (404)
                connectionSocket.send("404: File Not Found")

                #Close client socket
                connectionSocket.close()

   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)