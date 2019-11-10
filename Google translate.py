"""
@auther ; ganesh khadanga
date;- 16/05/2029

"""

"""

before using the script install google translet library . use the following command ;- [pip install googletrans]

"""


#=======import=======
from googletrans import Translator
translator = Translator()

#======= while loop and user note====
while True:
	print("NOTE;\n by default it auto find input language and translet to english. If you want to use custom languge then enter [ gtrans --custom] and in next input window enter your language \'iso\' code ex: [french] has iso code [fr] ")

#======user input==========
	u_input=input("enter your text you want to translet:\n")
	
	
#======== result===========	
	if u_input=='gtrans --custom':
		iso= input("enter your language iso code:   ")
		ab=translator.translate(u_input, dest=iso)
		print(u_input ,'→', ab.text)
		
	
	else:
		ab=translator.translate(u_input, dest='en')
		print(u_input ,'→', ab.text)