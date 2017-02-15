# tp1

## compte GitHub

## Client UDP Python

Il faut récupérer le programme dans le chapitre du livre.

 - récupérer le pdf
 - chercher la pages
 - recopier le programme dans un éditeur
 - executer
 
 ##UDPclient
 
 ````python
 //UDPclient//
 from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('texte ?')

clientSocket.sendto(message,(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print modifiedMessage

clientSocket.close()
```
##UDPserver
````python

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)

```

