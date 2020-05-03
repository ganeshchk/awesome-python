"""
by ganesh khadanga
date:- 30-04-2019
edit:- 10-05-2019 // (change log : fixed problem in results)

"""


"""
information:-
make sure that you have installed wikipedia library.
to install use following command in terminal : (pip install wikipedia)

"""

#____ wikipedia import____
import wikipedia


    
#_____ user search input_____    
user_input = input("enter your text to search: ")
    
#___ information for user ____    
print(" 1. get summary \n 2. get one line defination \n 3. get related result \n 4. get link of the article \n 5. get full article ")
    
#______ get result______    
type = int(input("enter respective SL. number to get result : "))


#________result_________


page = wikipedia.page(user_input)


if type==1:
	 print(wikipedia.summary(user_input))

elif type==2:
	print(wikipedia.summary(user_input, sentences=1))

elif type==3:
	print(wikipedia.search(user_input))
	
elif type==4:
     print(page.url)
 
elif type==5:
     print(page.content) 
     
else :
	print ("invalid request")                       
				 	 		 	 		 	 		 	 