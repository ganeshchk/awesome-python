#this program is created by GANESH KHADANGA in 05-04-2019
#edited 06-04-2019 , change log; added decorrator
    #========================================


#_______________decorrator______________
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("trignometry")

decorated = decor(print_text)
decorated()
	
#_--------- GETTING THE IMPORTS ------
from math import sin as t
from math import cos as t1
from math import tan as t2


#---------- creating functions------------
def t3(x):
  return 1/(tan(x))
 
  
def t4(x):
	return 1/(cos(x))

	
def t5(x):
	return 1/(sin(x))	


#----------user input---------------
s=input("which trigonometry function you want to use:")

a=int(input("measure of corresponding angle:"))

#----------- answer section---------
print("your answer is")
if s=='sin':
	print(t(a))

elif s=='cos':
    print (t1(a))

elif s=='tan':
	print(t2(a))

elif s=='cot':
	print(t3(a))

elif s=='sec':
	print(t4(a))

elif s=='cosec':
	print(t5(a))
