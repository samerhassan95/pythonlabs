





#************************  1 *************************
# string=input("enter string")  #'This is javascript'
# ch=input("enter character")
# list=[]

# for x in range(0,len(string)):
#     if(string[x] == ch):
#         list.append(x)


# print(list)




#****************************** 2 ***************

# number = int(input("enter num"))
# listin=[]
# listout=[]
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         listin.append(j*i)
#     listout.append(listin) 
#     listin=[]

# print(listout)


#************************************ 3 ***********************


input_string = input("Enter a list element separated by space ")
input_string = input_string.replace('"',"").replace("'","").replace("[","").replace("]","").replace(" ","")
l=input_string
list = l.split(",")

print(list)

dic={}
for x in list:
    dic[x[0]]=x

print(dic)

