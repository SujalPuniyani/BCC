# for i in range(1,5):
#     if (i==3):
#         break
#     print(i)

# for i in range(1,5):
#     if (i==3):
#         continue
#     print(i)
    
# for i,j in zip(range(1,6),range(5,0,-1)):
#     if(i == 3 and j == 3):
#         continue
#     print(i,end = "\t")
#     print(j)

#While Loop:

# i = 1
# while i<=5:
#     print(i)
#     i += 1

# user_name = input("Enter username: ")
# pwd = input("Enter password: ")

# while True:
#     if(user_name == "sujal" and pwd == "1234"):
#         print("Login Successfull")
#         break
#     else:
#         user_name = input("Enter username: ")
#         pwd = input("Enter password: ")

# username = ''
# pwd = ''
# while username != "sujal" and pwd != "1234":
#     username = input("Enter username: ")
#     pwd = input("Enter password: ")

# n = int(input("Enter number: "))
# sum = 0
# i = 1
# while i<=n:
#     sum += i
#     i+=1

# print(f"The sum of first {n} numbers: {sum}")

# name = 'prashant'
# a= ''
# for i in name:
#     if i not in a:
#         a+=i
# print(a)
    
# rev = ''
# l = len(name)
# for i in range(l-1,-1,-1):
#     rev += name[i]
# print(rev)

# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("This my purchased cart item")
#         continue
#     print(i)

# str  = input("Enter any string: ")
# rev = str[::-1]
# if(str == rev):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Sample Output = "listen" and "silent"
#Expected Output = "Anagrams"

# dic = {
#     "name" : "Alice"
# }
# key = input("Enter key: ")
# value = input("Enter value: ")
# dic.update({key:value})
# print(dic)

# dic = {
#      "name" : "Alice",
#      "age" : 30
# }
# # dic.pop("age")
# # print(dic)

# key = input("Enter key: ")

# for i in dic:
#     if key == i:
#         print("Yes")
#     else:
#         print("No")


# 1 1 1
# 2 2 2
# 3 3 3 
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end = " ")
#     print()


# A A A
# B B B
# C C C
# D D D 
# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()


# 4 4 4 4
# 3 3 3 3
# 2 2 2 2
# 1 1 1 1
# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()
        

# n = int(input("Enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()        


    
        