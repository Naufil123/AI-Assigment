# Question 1
lst=[]
sum=0
for i in range(8):
    user=int(input("enter number"))
    lst.append(user)
    sum=sum+user
    print(lst)
    print(sum)
# Question 2
sum=0
n=int(input("enter number"))
for i in range(0,n+1):
    b=i**2
    sum+=b
print(sum)
# Question 3
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# Question 4
for i in range(3):   
    n = int(input("enter the number : "))
    a = 5*n*n +4
    if a%2==0:
        print('yes')
    else:
        print('No')
# Question 5

n=int(input("enter number"))
for i in range(0,n+1):  
    b=n*i
    print(b)
# Question 6
lst = []
for i in range(0,10):
    lst.append(i)
print(max(lst))
print(min(lst))
# Question 7
lst = [12,10,52,36,52,36]
lst[4] = 12
lst[0] = 5
lst[5] = 10
lst[1] = 6
print(lst)
# Question 8
list1 = [2, -7, 5, -64, -14]
list2 = [-12, 14, 95, 3]
pos_num=0
neg_num=0
for i in list1:
    if i >=0:
        pos_num+=1
    else:
        neg_num+=1
for j in list2:
    if j >=0:
        pos_num+=1
    else:
        neg_num+=1
print(pos_num)
print(neg_num)
# Question 9
n=str (input("Enter string"))
if n==n[::-1]:
    print("yes")
else:
    print("No")
# Question 10
a = str(input("enter the string : "))
a.lower()
for i in a.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print("ACCEPTED")
        break
    else:
            print("NOT ACCEPTED")
            break
       





























    
    


             
