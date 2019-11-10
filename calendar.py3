# this program is created by ganesh khadanga
# date: 18/4/2019








print (" _______welcome to python calendar by ganesh khadanga __________" )


# _____import of calendar module____

import calendar

#____user guide about use of script____

user_info=" 1.get calendar of a month \n 2.get calendar of a year \n 3. chack for a leap year \n 4. chack No. of leap year in a range \n 5. get day from date "

print (user_info)

# _____input by user______

user_input= int(input("plese enter respective sl.No. to use that function:"))

#======result======

if user_input == 1:
    
    a= int(input("which year:"))
    b= int(input("month number:") )
    
    if b>12:
     print (" invalid information ")
    
    else :
    	print  (calendar.month(a, b, 3, 1))




elif user_input == 2:
    c= int(input("which year:"))

    print(calendar.calendar(c, 2, 2, 6, 3)) 
    





elif user_input == 3:
    
    d= int (input ("plese enter the year you want to check for:"))

    e= (calendar.isleap(d))
    
    if e == True:
        
        print (" yes, it is a leap year")
        
    if e== False :
        
        print ("no,it is not a leap year")




elif user_input == 4:
    
    print ("this will show you number of leap year betweeen year1 and year2")

    f= int(input ("year1:"))
    
    g = int(input("year2:"))

    print(calendar.leapdays(f, g))


elif user_input == 5:

    h= int(input("year:"))
    
    i= int(input("month:"))

    j= int (input ("date;"))


    if i>12 :
        print ("invalid information")
        
    else :    

   	 k= calendar.weekday(h, i, j)

   
   
   
    if k==0:
        print (" monday")
    if k==1:
        print ("tuesday")
    if k==2:
        print ("wednesday")
    if k==3:
        print ("Thursday")
    if k==4:
        print ("friday")
    if k==5:
        print ("saterday")
    if k==6:
        print ("sunday")



print("________Thank you_______")