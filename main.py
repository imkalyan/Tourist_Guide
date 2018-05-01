#need to do map to travel according to distance
import random

    
def readfiles():
    fp=open("south.txt","r+")
    line=fp.readline()
    south=[]
    while (line!=""):
        r1=line.split('-')
        line=fp.readline()
        south.append(r1)
    #print(south)
    print("\n")

    fp.close()
    
    return south
def readfiles1():
    fp1=open("north.txt","r+")
    line1=fp1.readline()
    north=[]
    while (line1!=""):
        r1=line1.split('-')
        line1=fp1.readline()
        north.append(r1)
    #print(north)
    fp1.close()
    return north
def readfiles2():
    fp2=open("foreign.txt","r+")
    line=fp2.readline()
    foreign=[]
    while (line!=""):
        r1=line.split('-')
        line=fp2.readline()
        foreign.append(r1)
    #print(south)
    print("\n")

    fp2.close()
    
    return foreign
def trip(ran,discount,south):
    fp3=open("out4.txt","a+")
    req=[]
    for i in range(0,len(south)):
           if int(south[i][3])<=ran:
               req.append(south[i])
               print(south[i][0],"-",south[i][1],"-",south[i][2],end="\n")
    print("Enter the number of places that u want to visit:")
    
    l=[int(i) for i in (input().split(' '))]
    area=l
    visit=[]
    price=0
    for i in range(0,len(area)):
           for j in range(0,len(req)):
               if int(req[j][0])==int(area[i]):
                  visit.append(req[j])
                  price=price+int(south[j][3])
               else:
                   price=price+0
    print("-----------------------------------------------------------------------------------------------------------------")               
    print("actual cost for the trip you designed for yourself is : %d" %(price))
    fp3.write("PRICE before discount:")
    fp3.write(str(price))
    fp3.write("\n")
    fp3.write("discount percentage:")
    fp3.write(str(discount))
    fp3.write("\n")
    print("After reducing discount that we provide:\n")
    price=price-(price)*(discount/100)
    fp3.write("PRICE after including discount for whole trip without transport charges:")
    fp3.write(str(price))
    fp3.write("\n")
    print("the travel costs for your whole trip : %d " %(price))
    #print(k)
    print("-----------------------------------------------------------------------------------------------------------------")
    fp3.close()
    return visit
def sort(l):
    for i in range(0,len(l)):
            for j in range(0,(len(l)-i-1)):
                if int(l[j][2])>int(l[j+1][2]):
                    temp=l[j]
                    l[j]=l[j+1]
                    l[j+1]=temp
    return l    
def plan(south,north,visit,distance,station,foreign):
                fp3=open("out4.txt","a+")
                #print(visit)
                planarray=[]
                l=[]
                #print(station)
                for j in range(0,len(distance)):
                                for i in range(0,len(visit)):
                                                if visit[i][1]==distance[j][1] and distance[j][0]==station and distance[j] not in l:
                                                                        #print(visit[i][1],",",distance[j][1])
                                                                        l.append(distance[j])
                                                
                                                #print(distance[j][0],"-",distance[j][1],"-",distance[j][2])
                                                #planarray.append(int(distance[j][2]))
                                                                
                                                
                #print(l)
                l=sort(l)
                print("-----------------------------------------------------------------------------------------------------------------")
                print("we planned a map which may  save ur time:\n\t")
                fp3.write("Plan that we designed for you is as follow\n")
                for i in range(0,len(l)):
                                for j in range(0,len(visit)):
                                                if visit[j][1]==l[i][1]:
                                                                        
                                                                        fp3.write(str(visit[j][2]))
                                                                        fp3.write("->")
                                                                        print("->",visit[j][0],visit[j][1],visit[j][2],end=" ")
                fp3.write("\n")              
                print("follow this map\n")
                print("-----------------------------------------------------------------------------------------------------------------")
                fp3.close()
def budjet(k,south,north,foreign):
    fp3=open("out4.txt","w+")
    fp3.write("SPK TOURISM\n")
    fp3.write("hello,here is your data for trip\n")
    fp3.write("\n")
    print("we provide:\n\t 1)North-india package \n\t 2)South-india package \n\t 3)Foreign-package \n\t")
    print("-----------------------------------------------------------------------------------------------------------------")
    zone=int(input())
    print("Enter Range that u need")
    print("PLEASE ENTER YOUR BUDGET RANGE \n\t 1.1000-5000(for south and north-Indian trip)\n\t 2.5000.25000(for Foreign trip)\t:")
    ran=int(input())
    fp3.write("RANGE:")
    fp3.write(str(ran))
    fp3.write("\n")
    discount=10
    fp3.write("DISCOUNT:")
    fp3.write(str(discount))
    fp3.write("\n")
    fp3.close()
    if zone==1:
         visit=trip(ran,discount,north)
    if zone==2:
         visit=trip(ran,discount,south)
    if zone==3:
        visit=trip(ran,discount,foreign)
    detail=[]
    
    t=int(input("Do you transport facility to the place ?(ENTER 1 for yes & 0 for no)\t:"))
    if t==1:
        print("Select Mode for ticket : \n\t1)train \n\t2)flight\n\t 3)ship\n\t 4)cab\n")
        
        print("-----------------------------------------------------------------------------------------------------------------")
        mode=int(input())
        traintickets(south,north,visit,mode,foreign)
    else:
        print("thats all,no transport")
    
def traintickets(south,north,visit,mode,foreign):
    distance=[]
    
    fp3=open("ttkt.txt","w+")
    fp2=open("distance.txt","r+")
    fp3.write("Travel tickets and Details :\n")
    line2=fp2.readline()
    while (line2!=""):
        d2=line2.split('-')
        distance.append(d2)
        line2=fp2.readline()
    #print(distance)
    cost=0
    print("-----------------------------------------------------------------------------------------------------------------")
    print("our travels have trains from the following stations: \n\t1)visakhapatnam\n\t2)bangalore\n\t3)chennai\n\t4)newDelhi\n\t5)Bhuvaneshwar\n\t6)jhansi\n\t7)jaipur\n\t8)patiala\n\t9)kashmir")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Enter the name of station:")
    station=str(input())
    fp3.write("starting at station :")
    fp3.write(station)
    fp3.write("\n")
    plan(south,north,visit,distance,station,foreign)
    destination=str(input("Enter the first  place that u want to visit:"))
    fp3.write("departure at station :")
    fp3.write(destination)
    fp3.write("\n")
    
    for i in range(0,len(distance)):
        if distance[i][1]==destination and distance[i][0]==station:
                
                if(int(distance[i][2])<=1000 and int(distance[i][2])>=200):
                
                    cost=random.randrange(200,800)
                elif int(distance[i][2])>1000 and int(distance[i][2])<=1500:
                
                    cost=random.randrange(800,1200)
                elif int(distance[i][2])<=2500 and int(distance[i][2])>1500:
                
                    cost=random.randrange(1300,1500)
 
                elif(int(distance[i][2])<5000 and int(distance[i][2])>2500):
                
                    cost=random.randrange(1500,3000)
 
   
                elif(int(distance[i][2])<=10000 and int(distance[i][2])>=5000):
                
                    cost=random.randrange(8000,10000)
                    #print(cost)
                elif(int(distance[i][2])>10000 and int(distance[i][2])<=15000):    
                
                    cost=random.randrange(10000,15000)
                    #print(cost)
                elif(int(distance[i][2])>15000 and int(distance[i][2])<=25000):
                
                    cost=random.randrange(15000,20000)       #print("error")
           
    print("-----------------------------------------------------------------------------------------------------------------") 
    print("select coach of the train : \n\t1)sleeper\n\t 2)second AC\n\t 3)third AC\n\t")
    print("-----------------------------------------------------------------------------------------------------------------")
    coach=str(input())
    if coach=="1":
        fp3.write("coach:")
        fp3.write("SLEEPER")
        fp3.write("\n")
        cost=cost+100
    elif coach=="2":
        fp3.write("coach:")
        fp3.write("second AC")
        fp3.write("\n")
        cost=cost+300
    elif coach=="3":
        fp3.write("coach:")
        fp3.write("third AC")
        fp3.write("\n")
        cost=cost+500
    #print(cost)
      
    name= str(input("ENTER YOUR NAME :"))
    fp3.write("Name:")
    fp3.write(name)
    fp3.write("\n")
    no_of_passengers=int(input("PLEASE ENTER THE NUMBER OF PASSENGERS-"))
    y=no_of_passengers
    fp3.write("No-of-passengers:")
    fp3.write(str(y))
    fp3.write("\n")
    no_of_adults=int(input("ENTER NUMBER OF ADULTS:"))
    fp3.write("No-of-adults:")
    fp3.write(str(no_of_adults))
    fp3.write("\n")
    no_of_children=int(input("ENTER NUMBER OF CHILDREN:"))
    fp3.write("No-of-children:")
    fp3.write(str(no_of_children))
    fp3.write("\n")
    address=input("ENTER DOOR-NUM , STREET-NUM, CITY-NAME,STATE NAME:")
    fp3.write("Address:")
    fp3.write(str(address))
    fp3.write("\n")
    aadhar_number=int(input("ENTER ANY ONE OF THE PASSENGER AADHAR NUMBER :"))
    fp3.write("aadhar_number:")
    fp3.write(str(aadhar_number))
    fp3.write("\n")
    if y==no_of_adults+no_of_children:
        traincost=no_of_adults*cost+(no_of_children*cost/2)
        if mode==1:
            traincost=traincost
        elif mode==2:
            traincost=traincost*4
        elif mode==3:
            traincost=traincost*3
        elif mode==4:
            traincost=traincost*(2.5)
    fp3.write("TRAVEL CHARGES:")
    fp3.write(str(traincost))
    fp3.write("\n")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("the total cost of transport : %d" %(traincost))
    fp3.close()
    #budjet1=int(input("ENTER YOUR BUDGET:"))
         #budjet(budjet1)
            # print("PLEASE SELECT YOUR BUDGET RANGE \n 1.5000-10000 \n 2.10000-15000 \n 3.15000-20000 4.20000-25000")
    #print("Do u need any transport facility?")
    if k==0:
       print("Enter your choice \n \t 1-North Indian Packages \n \t 2-South Indian Packages")
       n=int(input())
       if n==1 :
         print("Enter your Destination \n 1.Delhi-Places Include Agra,... 4 Days/3 Nights charges--15000 \n 2.Rajasthan-Places Include Jaipur,... 5 Days/4 Nights charges---20000 \n 3.Punjab-Places Include Amritsar,.... 4 Days/3 Nights charges--14000 \n 4.gangtok-Places include Temple ,... 3 Days/2 Nights charges--25000 \n 5.Kashmir-Places Include Dal Lake,... 4 Days/3 Nights charges--25000") 
       if n==2 :
         print("Enter your Destination \n 1.Hyd-Places Include Charminar,.... 2 Days/1 Night---charges--15000 \n 2.chennai-Places Include  Marina Beach,... 3 Days/2 Nights --- charges--10000 \n 3.Bangalore-Places Include Mysore,... # Days/2 Nights charges--25000 \n 4.Kerla-20000")
       d=int(input())
       if d<0 or d>6 :
         print("PLEASE ENTER THE CORRECT CODE YOU HAVE ENTERED THE WRONG CODE")
         budjet(k)
       
       else :
                   detail=[]
                   no_of_passengers=int(input("PLEASE ENTER THE NUMBER OF PASSENGERS-"))
                   for i in range(0,no_of_passengers):
                       det=[]
                       a=str(input("PLEASE ENTER THE NAME OF PASSENGER i-"))
                       det.append(a)
                       A=int(input("PLEASE ENTER THE AADHAR NUMBER OF PASSENGER i-"))
                       det.append(A)
                       a_=int(input("PLEASE ENTER THE AGE OF PASSENGER i-"))
                       det.append(a_)
                       detail.append(det)
                   #print(detail)
                
print("WELCOME to SPK TOURS THE INDIA's NO-1 TOURS \n")
#print("we provide:\n\t 1)North-india package \n \t 2)South-india package \n\t 3)Foreign-package \n\t")
south=readfiles()
north=readfiles1()
foreign=readfiles2()
k=int(input("ENTER 1 to process through budjet : "))
print("-----------------------------------------------------------------------------------------------------------------")
budjet(k,south,north,foreign)
