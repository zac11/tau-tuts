#define a new list
fruits =["apples","oranges","pears","peaches","bananas"]
years =[3,"1995",2.5,987,"1994"]
print(fruits,years)

#list methods
fruits.append("babugosha")
print(fruits)

fruits.extend(years)
print(fruits)
fruits.remove("apples")
print(fruits)
fruits.pop(1)
print(fruits)

#sort a list
numberlist = [12,5,67,9,1998,17,45,9,81,1889,909]
numberlist.sort()
print(numberlist)
print(numberlist.count(9))

#check members in list
print("babugosha" in fruits)

#check counts
print(fruits.count("peaches"))

print(fruits.index("oranges"))