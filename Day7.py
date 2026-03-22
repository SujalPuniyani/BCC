# #import re
# x="gasgg54@#vscsd!*"
# count=0
# for i in x:
#   z=ord(i)
#   if z>=97 and z<=122:
#     continue
#   elif z>=48 and z<=57:
#     continue
#   else:
#     count+=1
# print(count)



# x = [1,2,3]
# y = [2,3,4]
# z = [3,4,5]
# for i in x:
#   if i in y and i in z:
#     print(i)


# x = [0,1,0,3,12]
# for i in x:
#   if i==0:
#     x.remove(i)
#     x.append(0)
# print(x)


# x=[7,3,9,2,8]
# x.sort()
# print(x[3]) #print(x[-2])



x = [10,11,7,12,14]
j=i+1
result=0
for i in range(len(x)-1):
  # for j in range(len(x)-1):
    diff=(x[i+1]-x[i])
    if((x[i+1]-x[i])<0):
      diff=diff*(-1)
      result=result+diff
    else:
      result=result+diff
print(result)



n = int(input() )
# w = int(input("width:")
# h = int(input("heigth:")
l=int(input("length"))               # Reading input from STDIN
# print('Hi, %s.' % name)
for _ in range(n):
    w = int(input("width:"))
    h = int(input("heigth:"))
    if (w and h)<l:
        print("Upload another")
    elif ((w and h)>1) and (w==h) :
        print("acceppted")
    else:
        print("CropIt")














