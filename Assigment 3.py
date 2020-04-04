# Question 1
dictt={"nile":"Egypt","Amazon":"South America","Volga":"Russia"}
for i,j in dictt.items():
    print(i, "runs through",j)
    print("River-",i)
    print("Location-",j)
#Question 2a
dictt={"First_name":"Naufil","Last_name":"Nadeem","Age":"19","City":"Karachi"}
print(dictt.values())

#Question 2b
dictt={"First_name":"Naufil","Last_name":"Nadeem","Age":"19","City":"Karachi"}
dictt1={"First_name":"Nadeem","Last_name":"Mukhtar","Age":"24","City":"Karachi"}
dictt={"First_name":"Aasir","Last_name":"Rafi","Age":"21","City":"Karachi"}
People=[{"dictt":{"First_name":"Naufil","Last_name":"Nadeem","Age":"19","City":"Karachi"}},
{"dictt1":{"First_name":"Nadeem","Last_name":"Mukhtar","Age":"24","City":"Karachi"}},
{"dictt2":{"First_name":"Aasir","Last_name":"Rafi","Age":"21","City":"Karachi"}}]
for i in People:
    print(i)
#Question 3
Cities={"karachi":{"Country":"Pakistan","Population":"1 Crore","Fact":"City of light"},
        "Lahore":{"Country":"Pakistan","Population":"88 lac","Fact":"City of greenery"},
        "Islamabad":{"Country":"Pakistan","Population":"2 Crore","Fact":"Capital of pakistan"}}
for i in Cities.items():
    print(i)
#Question 4
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
a=dic1.update(dic1)
b=dic1.update(dic2)
print(dic1)
#Question 5
str1 = 'Dictionaries' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
# Question 6
dictt = {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
for i in dictt.values():
    print('the fifth value is ',i[4])
# Question 7a
prices = {'banana':'4','apple':'2','orange':'1.5','pear':'3'}
for i,j in prices.items():
    print(i)
    print("Price :",j)
# Question 7b
prices = {'banana':4,'apple':2,'orange':1.5,'pear':3}
total = 0
number_in_stock = 9
for i,j in prices.items():
    a=j*number_in_stock
    total += a
    print(total)
# Question 9
dictt ={'a':1, 'b':-2, 'c':-3, 'd':7, 'e':0}
dictt1 = {}
for i,j in dictt.items():
    if j>=0:
        dictt1[i]=j
print(dictt1)
# Question 10
print('Name \t Age \t Course')
dictt = {1: ['Samuel', 21, 'Data Structures'],2: ['Richie', 20, 'Machine Learning'],3: ['Lauren', 21, 'OOPS with java'],}
for i,j in dictt.items():
    print(j[0] ,"\t", j[1],"\t",j[2]) 

