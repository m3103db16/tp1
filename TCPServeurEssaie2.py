from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

serverPort2 = 10000
serverSocket2 = socket(AF_INET,SOCK_STREAM)

print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()	#accepte connection 1er client
	sentence = connectionSocket.recv(1024)	#reçoit les donnée (max 1024)
	capitalizedSentence = sentence.upper() 	#passe le message 
	print "From Server:", capitalizedSentence	
	connectionSocket.close()
	serverSocket2.bind(("",serverPort2))
	serverSocket2.listen(1)
	while 1:
		connectionSocket, addr = serverSocket2.accept()   #accepte connection client2
		connectionSocket.send(capitalizedSentence)	#renvoi les donné au 2eme client
		print "From Server:", capitalizedSentence	
		connectionSocket.close()
		