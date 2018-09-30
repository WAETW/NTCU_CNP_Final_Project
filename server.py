from socket import socket, AF_INET, SOCK_STREAM
import sys
import random
import threading
import time
HOST = '127.0.0.1'	# Symbolic name meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

s = socket(AF_INET, SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port

s.bind((HOST, PORT))

	
print ('Socket bind complete')

#Start listening on socket
s.listen(10)
print ('Socket now listening')




def handle_client(client_socket):	
	money = 0
	money = sock.recv(1024)
	money = int(money) 
	data = sock.recv(1024)
	while 1:
		if data == 'y':
			  
			num1 = 0
			num2 = 0
			num3 = 0
			num1 = random.randrange(1,6)
			num2 = random.randrange(1,6)
			num3 = random.randrange(1,6)
			num1=str(num1)
			num2=str(num2)
			num3=str(num3)
			
			sock.send(num1+","+num2+","+num3+"\n")

			if (num1==num2 and num1==num3):
				money=money+1000
              
				meg = 'you win 1000 dollar and you have:%d dollar\n'%money
			elif (num1==num2 and num1!=num3) or (num1==num3 and num2!=num3) or (num3==num2 and num3!=num1):
				money=money+100
				meg = 'you win 100 dollar and you have:%d dollar\n'%money
			else:
				money=money-1000
				meg = 'you lost 100 dollar and you have:%d dollar\n'%money
		

			sock.send(meg)
			time.sleep(1)
			if money <= 0:
				sock.send('l')
				break
			else:
				sock.send("you still have money\n")
			
			data = sock.recv(512)
			
			if data != 'y':
				break
		else:
			break
             
while 1:
	sock, addr = s.accept()
	print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	client_handler = threading.Thread(target=handle_client, args=(sock,))
	client_handler.start()

