#Function
# def msg():
#     print("Hello World")
# msg()

# def add():
#     n1 = int(input("Enter num1: "))
#     n2 = int(input("Enter num2: "))
#     sum = n1+n2
#     sub = n1-n2
#     mul = n1*n2
#     div = n1/n2
#     return sum,sub,mul,div
# result = add()
# print(result)

#Types of Arguments:
# 1.Positional Argument
# 2.Keyword argument
# 3.Default Argument
# 4.Variable length argument/Variable number of argument

# #1.Positional Argument
# def personalInfo(fname,lname):
#     print(f"First Name: {fname}")
#     print(f"Last Name: {lname}")
# personalInfo("Sujal","Puniyani")

# #2.Keywoed Argument
# def personalInfo(fname,lname):
#     print(f"First Name: {fname}")
#     print(f"Last Name: {lname}")

# fname = "Sujal"
# lname = "Puniyani"
# personalInfo(fname,lname)

# #3.Default Argument
# def cityname(city="Nagpur"):
#     print(city)

# cityname("Mumbai")
# cityname("Delhi")
# cityname()

# #4.Variable length argument
# def studentnames(*name):
#     print(name)
    
# studentnames("Sujal","Ritesh","PK")

# mylist = [5,3,1,7,4,6]
# def search(target):
#     for i in range(len(mylist)):
#         if(target == mylist[i]):
#             return i
    
#     return -1
        
# target = int(input("Enter Target: "))
# result = search(target)
# if(result != -1):
#     print(result)
# else:
#     print("Target not found")



