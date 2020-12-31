#  ---------------------------->>> Tuples <<<----------------------------
std_name = ("Zahid", "Ali", "Farhan", "Tasneem", "Gul")
Fruits = ("orange", "banana", "apples", "grapes")
print(std_name)
print(type(std_name))
print(len(std_name))
print(std_name[1])
print(std_name[-2])
print(std_name[2:4])
b = list(std_name)
b[2:4] = "pea", "cabbage"
std_name = tuple(b)
print(std_name)
b.append("tomato")
std_name = tuple(b)
print(std_name)
b.remove("cabbage")
std_name = tuple(b)
print(std_name)
# unpacking of tuple
print("onion")
print("potato")
print("tomato")
print("pepper")
print("carrot")
# Joining and multiplying of tuples
print(std_name + Fruits)
print(std_name*3)
# delete std_name -> print(std_name) tuple is deletd due to it causes an error.

# ------------------------->Sets<------------------------------
# sets are unchangeable, Unindexed and unordered
our_team = {"Zahid", "Ali", "Tasneem", "Gull"}
print(our_team)
print(type(our_team))
print(len(our_team))
# by using set constructor
my_friends = set(("Gull", "Sultan", "MH", "Farhan", "Mobi"))
# access the set item
print(my_friends)
for x in my_friends:
    print(x)
print("Farhan" in my_friends)
# add items in a set.
my_friends.add("Ali")
print(my_friends)
my_friends.update(our_team) # we can add list in a set by using update() method.
print(my_friends)
# joining of sets
print(my_friends.union(our_team)) # update() also used to join the sets.
our_team.intersection(my_friends)
print(our_team)
print(my_friends.intersection(our_team))
# Remove item from set
my_friends.remove("Mobi")
print(my_friends)
my_friends.discard("Farhan")
print(my_friends)
a = our_team.pop()
print(a)
our_team.clear()
print(our_team)
# del method removes the whole set and it causes error.
# del my_friends
# print(my_friends)
#------------------------>>> Booleans <<<--------------------------
print(our_team > my_friends)
print(my_friends == our_team)
print(my_friends >= our_team)
if my_friends > our_team:
    print("My friends are more than our team.")
else:
    print("Our team has more member than my freinds.")
