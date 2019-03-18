#creating list
mylist = [10, 234 , 13, 43, 143, 54,87,123,543,678,908,345,8756]
even_number =[]
#calling my list
print(mylist)
print("\n")

#access list item at specific position by index
value_at_3 = mylist[2]
#print the value
print("the value in index 2 is %r\n\n"%value_at_3)
#accessing more than on Item

print("List Item in the range of 6...10")
print(mylist[4:8])

#looping a list
for i in mylist:
	if (i%2==0):
		even_number.append(i)
print('\nadd all even number in the list')
print(even_number)
print("\n")

#adding value in the list
mylist.append(3)

print("new list Added element 3 ")
print (mylist)

#adding multiple elements in a list. They are all added at the end
mylist.extend([101,300, 401, 544])

print("\n")
print("more than one element added to the list i.e 101,300, 401 and 544")
print(mylist)

#check if Item is in the list

if "apple" in mylist:
    print("\nyes its in ")
else:
	print("\nNot present")


