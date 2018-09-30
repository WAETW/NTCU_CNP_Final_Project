import socket
import sys
import random
import time
import os
HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((HOST, PORT))
money = raw_input('input your money:')
s.send(money)
start = raw_input('start your game: (y/n)')

if start == 'y' or 'Y':
	s.send(start)
else:
	exit()

while 1:
	ra = s.recv(512)
	print(ra)
	sa = s.recv(512)
	print(sa)
	aa = s.recv(1024)
	time.sleep(1)
	if aa == 'l':
		print("you lose")
		break
	else:	
		print(aa)
		st = raw_input('continue (y/n)')
		s.send(st)
		if st != 'y':
			print("end the game")
			s.close()
	

	


 

  

	

