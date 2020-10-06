#!/usr/bin/python3
import random
def bypair(x):
	b=x.decode('utf-8')
	s=0
	for i in range(len(b)):
		if b [i] == "1":
			s += 1
	if (s%2) != 0:
		b= "1"+ b
	else:
		b = "0" + b
	print (b)
	x=bytearray(b,'utf-8')
	return x
def rand_key(p):
	key1 = ""
	#pr connaitre la longueur
	for i in range(p):
	#generer la fonction random
		temp = str(random.randint(0, 1))
		key1 += temp

	return(key1)
n= 9
str1 = rand_key(n)
print (str1)
x = bytearray(str1,'utf-8')
print (bypair(x))
