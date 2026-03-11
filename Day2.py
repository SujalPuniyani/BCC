mylist = ["prashant","Ashish","komal","ankush","Ashish",77,"Sandip",60.52,"prashant"]    

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[0:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])
    
# mylist.append('Omkar')
# mylist.append("pranav")
# print(mylist)

# mylist.insert(1,"Sanket")
# print(mylist)

# mylist.remove("Sandip")
# print(mylist)

# newlist = mylist.copy()
# print(mylist)
# print(newlist)

# mylist = ["prashant","jha"],["85.56"],[440022,"yyy"]
# print("ex of multidimensional list: ")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["omkar","umale"]
# print(list1*2)

# list2 = [50,55,68]
# print(list1+list2)
# del(list2[2])
# print(list2)
# list2.clear()
# print(list2)

# mylist = [44,55,66,777,232,323]
# mylist.sort(reverse = True)
# print(mylist)

# math =50
# physics = 40
# print(id(math))
# print(id(physics))
# 
# newlist = mylist
# print(id(mylist))
# print(id(newlist))


#2 types of operator:
# 1.in
# 2.notin
# name = "omkar"
# print('Z' in name)
# print('Z' not in name)

# for i in range(1,10):
#   print(i*2 ," " ,i*3 ," " ,i*4," ", i*5," ", i*6," ", i*7," ",i*8)

# no = int(input("enter any digit:"))
# if no>0:
#     print('positive')
# if no<0:
#     print('negative')
# if no == 0:
#     print('zero')

# day = (input("enter any day:"))
# if day == ("saturday" and "sunday:"):
#   print('weekend')
# else:
#   print('working')

# write a program to accept three paper marks and calculate total, percentage and if percentage is greater than equal to 60 then he or she is eligible for placement
# math = int(input("enter marks math:"))
# chem = int(input("enter marks chem:"))
# phy = int(input("enter marks phy:"))

# total= math+chem+phy
# print(total)
# percent=int((total/3))
# print(percent)

# if (percent>60):
#   print('eligible')
# else:
#   print('not eligible')

# WAP to accept 5 different values in 5 different variable and check max value and print by using simple if statement

a = int(input("enter num1:"))
b = int(input("enter num2:"))
c = int(input("enter num3:"))
d = int(input("enter num4:"))
e = int(input("enter num5:"))

if (a>b and a>c and  a>d and a>e):
  print("A is greater")

if (b>a and b>c and b>d and b>e):
  print("B is greater")

if (c>a and c>b and c>d and c>e):
  print("c is greater")

if (d>a and d>d and b>c and d>e):
  print("D is greater")

else :
  print("E is greater")
  
