# Basics 
from collections.abc import Sequence


a = 10
b = 10

print(id(a))
print(id(b))

# In Python, small integers (typically between -5 and 256) are cached and reused, so they have the same memory address. 
# However, for larger integers, Python creates a new object each time, so they may have different memory addresses. 
c = 1000
d = 1000
print(id(c))
print(id(d))

# In Python, strings are immutable, so they are also cached and reused.
# An address of a variable will be same if the value of the datatype is same. if any one of them changes the address will change
e = "Hello"
f = "Hello"
print(id(e))
print(id(f))

# Lists are mutable, so they are not cached and reused. Each time you create a new list, it will have a different memory address.

g = [1, 2, 3]  
h = [1, 2, 3]
print(id(g))
print(id(h))

# In Python, the `is` operator checks for identity, meaning it checks whether two variables point to the same object in memory.
# The `==` operator checks for equality, meaning it checks whether the values of the variables are the same, regardless of whether they are the same object in memory.


print(a is b)  # True, because a and b point to the same object (small integer caching)
print(c is d)  # False, because c and d point to different objects (large   integer)
print(e is f)  # True, because e and f point to the same object (string caching)
print(g is h)  # False, because g and h point to different objects (lists are mutable)
print(a == b)  # True, because a and b have the same value
print(c == d)  # True, because c and d have the same value
print(e == f)  # True, because e and f have the same value
print(g == h)  # True, because g and h have the same value (the contents are the same)

# In Python, the `id()` function returns the identity of an object, which is a unique integer that represents the memory address of the object.
# The `id()` function can be used to check if two variables point to the same object in memory. If two variables have the same `id()`, it means they point to the same object. If they have different `id()`, it means they point to different objects, even if their values are the same.
# In the example above, `a` and `b` have the same `id()` because they point to the same small integer object (10), while `c` and `d` have different `id()` values because they point to different large integer objects (1000). Similarly, `e` and `f` have the same `id()` because they point to the same string object ("Hello"), while `g` and `h` have different `id()` values because they point to different list objects ([1, 2, 3]).    
# In summary, the `id()` function is a useful tool for understanding how Python manages memory and how variables reference objects in memory. It helps to clarify the difference between identity (whether two variables point to the same object) and equality (whether two variables have the same value).
# In Python, the `is` operator checks for identity, meaning it checks whether two variables point to the same object in memory. The `==` operator checks for equality, meaning it checks whether the values of the variables are the same, regardless of whether they are the same object in memory.
# In the example above, `a` and `b` are small integers that are cached by Python, so they point to the same object in memory, and `a is b` returns `True`. However, `c` and `d` are larger integers that are not cached, so they point to different objects in memory, and `c is d` returns `False`. Similarly, `e` and `f` are strings that are cached by Python, so they point to the same object in memory, and `e is f` returns `True`. On the other hand, `g` and `h` are lists that are mutable and not cached, so they point to different objects in memory, and `g is h` returns `False`. However, since the contents of the lists are the same, `g == h` returns `True`.
# In summary, the `is` operator checks for identity (whether two variables point to the same object), while the `==` operator checks for equality (whether two variables have the same value). The behavior of these operators can vary depending on the type of data being compared and how Python manages memory for that data type.
# In Python, the `id()` function returns the identity of an object, which is a unique integer that represents the memory address of the object. The `id()` function can be used to check if two variables point to the same object in memory. If two variables have the same `id()`, it means they point to the same object. If they have different `id()`, it means they point to different objects, even if their values are the same.
# In the example above, `a` and `b` have the same `id()` because they point to the same small integer object (10), while `c` and `d` have different `id()` values because they point to different large integer objects (1000). Similarly, `e` and `f` have the same `id()` because they point to the same string object ("Hello"), while `g` and `h` have different `id()` values because they point to different list objects ([1, 2, 3]).
# In summary, the `id()` function is a useful tool for understanding how Python manages memory and how variables reference objects in memory. It helps to clarify the difference between identity (whether two variables point to the same object) and equality (whether two variables have the same value).
# If any thing is inside ("") then it will be always true
# In Python, the `bool()` function is used to convert a value to a Boolean (True or False). When you pass a non-empty string to the `bool()` function, it will return `True`, because non-empty strings are considered truthy in Python. On the other hand, an empty string (`""`) is considered falsy and will return `False` when passed to the `bool()` function.


print(bool("Hello"))  # True, because it's a non-empty string
print(bool(""))       # False, because it's an empty string

#Positive number and negative number are always true
print(bool(5))        # True, because it's a positive number
print(bool(-5))       # True, because it's a negative number
print(bool(0))        # False, because it's zero

# In Python, the following values are considered falsy and will return `False` when passed to the `bool()` function:
print(bool(0))        # False, because it's zero
print(bool(0.0))      # False, because it's zero (float)
print(bool([]))       # False, because it's an empty list
print(bool(()))       # False, because it's an empty tuple
print(bool({}))       # False, because it's an empty dictionary
print(bool(set()))    # False, because it's an empty set
print(bool(None))     # False, because it's None (null value)

a = 0
if a :
  print("Yes")
else :
  print("No")

# In the above code, the variable `a` is assigned the value `0`. In Python, `0` is considered a falsy value. Therefore, when the `if` statement checks the value of `a`, it evaluates to `False`, and the code inside the `else` block is executed, printing "No". If `a` were assigned a non-zero value (e.g., `1`), it would be considered truthy, and the code inside the `if` block would be executed, printing "Yes".

a = []
print(a)
print(not(a))

# In the above code, the variable `a` is assigned an empty list `[]`. When we print `a`, it will output `[]`. The expression `not(a)` evaluates to `True` because an empty list is considered falsy in Python. Therefore, when we print `not(a)`, it will output `True`.
#NOTE : In other languages "." creates an error but in python we access it by {[""]}

a = {"name": "Hello"}
print(a)
print(a["name"])
print(not(a))

# In the above code, the variable `a` is assigned a dictionary with a key-value pair where the key is "name" and the value is "Hello". When we print `a`, it will output `{'name': 'Hello'}`. The expression `a["name"]` accesses the value associated with the key "name" in the dictionary, which will output `Hello`. The expression `not(a)` evaluates to `False` because a non-empty dictionary is considered truthy in Python. Therefore, when we print `not(a)`, it will output `False`.

a = {"address": {"city": "Jaipur","Area": "Arya Main"}}
print(a["address"]["city"])
print(a["address"]["Area"])

# In the above code, the variable `a` is assigned a nested dictionary where the key "address" maps to another dictionary containing the keys "city" and "Area". When we access `a["address"]["city"]`, it retrieves the value associated with the key "city" in the nested dictionary, which will output `Jaipur`. Similarly, when we access `a["address"]["Area"]`, it retrieves the value associated with the key "Area" in the nested dictionary, which will output `Arya Main`.

dict = {"friends": {"Best friends": "Hello", "Just Friend": "Hello 1", "Plain Friend": "Hello 2"}}
print(dict["friends"]["Best friends"])
print(dict["friends"]["Just Friend"])
print(dict["friends"]["Plain Friend"])

# In the above code, the variable `dict` is assigned a nested dictionary where the key "friends" maps to another dictionary containing the keys "Best friends", "Just Friend", and "Plain Friend". When we access `dict["friends"]["Best friends"]`, it retrieves the value associated with the key "Best friends" in the nested dictionary, which will output `Hello`. Similarly, when we access `dict["friends"]["Just Friend"]`, it retrieves the value associated with the key "Just Friend" in the nested dictionary, which will output `Hello 1`. Finally, when we access `dict["friends"]["Plain Friend"]`, it retrieves the value associated with the key "Plain Friend" in the nested dictionary, which will output `Hello 2`.
# In summary, the code demonstrates how to access values in a nested dictionary by using multiple keys to navigate through the layers of the dictionary structure.
# In Python, dictionaries are a powerful data structure that allows you to store and retrieve values using keys. When you have a nested dictionary, you can access the inner values by chaining the keys together. This is done by using square brackets `[]` to access each level of the dictionary. For example, `dict["friends"]["Best friends"]` accesses the value associated with the key "Best friends" in the nested dictionary under the key "friends". This allows you to easily retrieve specific pieces of information from complex data structures.
# In summary, the code demonstrates how to access values in a nested dictionary by using multiple keys to navigate through the layers of the dictionary structure. This is a common technique in Python for working with complex data structures and allows for efficient retrieval of information based on specific keys.
# In Python, the `not` operator is a logical operator that negates the truth value of an expression. When you apply `not` to a value, it returns `True` if the value is falsy and `False` if the value is truthy. In the context of the code provided, when we use `not(a)` where `a` is an empty list or an empty dictionary, it evaluates to `True` because both empty lists and empty dictionaries are considered falsy in Python. Conversely, when we use `not(a)` where `a` is a non-empty dictionary, it evaluates to `False` because non-empty dictionaries are considered truthy in Python. This behavior allows us to easily check for the presence or absence of elements in data structures like lists and dictionaries using the `not` operator.

dict = {"Address":["Jaipur", "Kukas", "Chandwaji", "Transport Nagar"], "Jaipur": {"city": "Sindhi Camp", "Area": "Bus Stand"}}
print(dict["Address"][0])
print(dict["Address"][1])
print(dict["Address"][2])
print(dict["Address"][3])
print(dict["Jaipur"]["city"])
print(dict["Jaipur"]["Area"])

# In the above code, the variable `dict` is assigned a nested dictionary where the key "Address" maps to a list of strings, and the key "Jaipur" maps to another dictionary containing the keys "city" and "Area". When we access `dict["Address"][0]`, it retrieves the first element of the list associated with the key "Address", which will output `Jaipur`. Similarly, when we access `dict["Address"][1]`, it retrieves the second element of the list, which will output `Kukas`. When we access `dict["Address"][2]`, it retrieves the third element of the list, which will output `Chandwaji`. When we access `dict["Address"][3]`, it retrieves the fourth element of the list, which will output `Transport Nagar`. Finally, when we access `dict["Jaipur"]["city"]`, it retrieves the value associated with the key "city" in the nested dictionary under "Jaipur", which will output `Sindhi Camp`. When we access `dict["Jaipur"]["Area"]`, it retrieves the value associated with the key "Area" in the nested dictionary under "Jaipur", which will output `Bus Stand`.
# In summary, the code demonstrates how to access values in a nested dictionary that contains both lists and dictionaries. By using the appropriate keys and indices, we can retrieve specific pieces of information from the complex data structure. This is a common technique in Python for working with nested data structures and allows for efficient retrieval of information based on specific keys and indices.
# In Python, you can have a nested dictionary that contains both lists and dictionaries. To access the values in such a structure, you can use a combination of keys and indices. For example, `dict["Address"][0]` accesses the first element of the list associated with the key "Address", while `dict["Jaipur"]["city"]` accesses the value associated with the key "city" in the nested dictionary under "Jaipur". This allows you to navigate through complex data structures and retrieve specific pieces of information based on your needs.

a = [10, 20, 30, [40,50]]
print(a)
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])

# In the above code, the variable `a` is assigned a list that contains integers and another nested list. When we print `a`, it will output `[10, 20, 30, [40, 50]]`. The expression `a[1]` accesses the second element of the list, which will output `20`. The expression `a[2]` accesses the third element of the list, which will output `30`. The expression `a[3]` accesses the fourth element of the list, which is itself a nested list `[40, 50]`, so it will output `[40, 50]`. Finally, `a[3][0]` accesses the first element of the nested list (which is `40`), and `a[3][1]` accesses the second element of the nested list (which is `50`), so they will output `40` and `50`, respectively.
# In summary, the code demonstrates how to access elements in a list that contains both integers and a nested list. By using the appropriate indices, we can retrieve specific pieces of information from the complex data structure. This is a common technique in Python for working with nested data structures and allows for efficient retrieval of information based on specific indices.

a = {
    "catalogFeedType":"catalog_listing_page",
    "enable":False,
    "catalogs":[
        {
            "id":3050654,
            "hero_pid":15293867,
            "name":"Mangalsutra",
            "popular":False,
            "has_mrp":True,
            "is_added_to_wishlist":False,
            "assured_details":{
                "is_assured":False,
                "message":"Best quality products from trusted suppliers."
            }
        }
    ]}
print(a["catalogFeedType"])
print(a["enable"])
print(a["catalogs"][0]["id"])
print(a["catalogs"][0]["hero_pid"])
print(a["catalogs"][0]["name"])
print(a["catalogs"][0]["popular"])
print(a["catalogs"][0]["has_mrp"])
print(a["catalogs"][0]["is_added_to_wishlist"])
print(a["catalogs"][0]["assured_details"]["is_assured"])
print(a["catalogs"][0]["assured_details"]["message"])

# In the above code, the variable `a` is assigned a nested dictionary that contains various key-value pairs, including a list of catalogs. The code demonstrates how to access specific values within this complex data structure by using a combination of keys and indices. For example, `a["catalogFeedType"]` retrieves the value associated with the key "catalogFeedType", while `a["catalogs"][0]["id"]` accesses the "id" of the first catalog in the list. This allows us to efficiently retrieve specific pieces of information from the nested dictionary based on our needs.
# In summary, the code demonstrates how to access values in a nested dictionary that contains both dictionaries and lists. By using the appropriate keys and indices, we can navigate through the complex data structure and retrieve specific pieces of information based on our requirements. This is a common technique in Python for working with nested data structures and allows for efficient retrieval of information based on specific keys and indices.
# In Python, you can have a nested dictionary that contains both dictionaries and lists. To access the values in such a structure, you can use a combination of keys and indices. For example, `a["catalogFeedType"]` accesses the value associated with the key "catalogFeedType", while `a["catalogs"][0]["id"]` accesses the "id" of the first catalog in the list. This allows you to navigate through complex data structures and retrieve specific pieces of information based on your needs.

c = 0
if (not(c)) :
  print("zero || absent")
else :
  print("studnt present")


# In the above code, the variable `c` is assigned the value `0`. The expression `not(c)` evaluates to `True` because `0` is considered a falsy value in Python. Therefore, the condition in the `if` statement is satisfied, and the code inside the `if` block is executed, printing "zero || absent". If `c` were assigned a non-zero value (e.g., `1`), it would be considered truthy, and the code inside the `else` block would be executed, printing "student present". This demonstrates how the `not` operator can be used to check for falsy values and control the flow of the program accordingly.

a = 10
b = 20
print(a+b)

c = 20
d = 10
print(c-d)

e = 5
f = 10
print(e*f)

g = 10
h = 2
print(g//h)

i = 9
j = 2
print(i%j)

k = 5
l = 2
print(k ** l)

m = 4
n = 5
print(m==n)
m=n
print(m==n)

a,b = b,a
print(a)
print(b)

print( a>= 20)
print( a<= 20)
print( a== b)

# In the above code, we demonstrate various basic operations in Python, including arithmetic operations (addition, subtraction, multiplication, floor division, modulus, and exponentiation), comparison operations (greater than or equal to, less than or equal to, and equality), and variable swapping. The code also shows how to check for equality between variables and how to swap the values of two variables using tuple unpacking. These are fundamental concepts in Python programming that allow us to perform calculations, compare values, and manipulate data effectively.
# In summary, the code provides examples of basic operations in Python, including arithmetic operations, comparison operations, and variable swapping. These operations are essential for performing calculations, comparing values, and manipulating data in Python programming. Understanding these concepts is crucial for writing efficient and effective code in Python.

a = []
b = 10
print(not a or b)

# In the above code, the variable `a` is assigned an empty list `[]`, which is considered falsy in Python. The variable `b` is assigned the value `10`, which is considered truthy. The expression `not a or b` evaluates to `True` because `not a` evaluates to `True` (since `a` is falsy), and the `or` operator returns `True` if at least one of the operands is true. Therefore, when we print `not a or b`, it will output `True`. This demonstrates how logical operators can be used to evaluate expressions based on the truthiness of variables in Python.

a = 5
b = 3
print(a & b)

print(a | b)

c = 10
d = 7
print(not (a & b))

a = ["stu1", "stu2", "stu3", "stu4"]
b = "stu3"
print(b in a)

# In the above code, we demonstrate the use of bitwise operators (`&` and `|`) and the logical operator `not` in Python. The expression `a & b` performs a bitwise AND operation between the binary representations of `a` and `b`, while `a | b` performs a bitwise OR operation. The expression `not (a & b)` negates the result of the bitwise AND operation. Finally, we check if the string `b` is present in the list `a` using the `in` operator, which returns `True` if the element is found in the list and `False` otherwise. These operations are fundamental in Python programming for performing bitwise calculations and checking for membership in data structures.
# In summary, the code demonstrates the use of bitwise operators and logical operators in Python, as well as how to check for membership in a list. Understanding these concepts is essential for performing various operations in Python programming, including bitwise calculations and data structure manipulation.

dict = {"class": [10, 11,12],
        "student": ["Ram", "shyam", "ghanshyam"]}
c = 10
s ="ram"
if c in dict["class"]:
  print("class present", c)
else : print("class not present", c)
if s in dict["student"]:
  print("student present", s)
else : print("student not present", s)

# In the above code, we have a dictionary `dict` that contains two keys: "class" and "student". The value associated with the key "class" is a list of integers representing class numbers, while the value associated with the key "student" is a list of strings representing student names. We then check if the variable `c` (which is assigned the value `10`) is present in the list associated with the key "class". If it is present, we print "class present" along with the value of `c`. If it is not present, we print "class not present" along with the value of `c`. Similarly, we check if the variable `s` (which is assigned the value `"ram"`) is present in the list associated with the key "student". If it is present, we print "student present" along with the value of `s`. If it is not present, we print "student not present" along with the value of `s`. This demonstrates how to check for membership in lists within a dictionary in Python.
# In summary, the code demonstrates how to check for membership in lists that are values in a

# In while loop, While is a reserved keyword. By using while keyword we are declaring the while loop. In while loop condition is true but loop is continuous, if condition is false loop endes.
i = 1
while i <= 5:
    print(i)
    i += 1

a = 5
i = 0
while i<a:
  print(i)
  i+=1
print(i,a)
print(id(i),id(a))

L = ["Raj", 10, 20, False]
i = 0
while i<len(L):
  print(L[i])
  i+=1
print(i,L)

dict ={"Laptops": ["Infinix", "Apple", "Samsung"]}
i=0
while i<3:
  print(dict["Laptops"][i])
  i+=1
print(i,dict)

# In the above code, we demonstrate the use of a while loop in Python to iterate through a list and a dictionary. The while loop continues to execute as long as the condition is true. In the first example, we print the numbers from 1 to 5 by incrementing the variable `i` in each iteration. In the second example, we iterate through a list `L` and print each element until we reach the end of the list. In the third example, we access the values in a nested dictionary and print each laptop brand until we have printed all three brands. This demonstrates how to use while loops to iterate through different data structures in Python.
# In summary, the code demonstrates how to use while loops in Python to iterate through lists and dictionaries. The while loop continues to execute as long as the specified condition is true, allowing us to perform operations on each element of the data structure until we reach the end. This is a fundamental concept in Python programming for controlling the flow of execution and performing repetitive tasks based on certain conditions.

# For loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence. The syntax of a for loop in Python is as follows:
for variable in Sequence:
    # code to execute for each item in the sequence
# In the above code, `variable` is a temporary variable that takes on the value of each item in the `sequence` one at a time. The block of code inside the for loop will be executed for each item in the sequence until all items have been processed. This is a common way to iterate through lists, tuples, strings, and other iterable objects in Python.
# In summary, the for loop in Python is a powerful tool for iterating over sequences and other iterable objects. It allows you to execute a block of code for each item in the sequence, making it easy to perform operations on each element without having to manually manage the loop counter or index. This makes for loops a convenient and efficient way to process data in Python programming.
 L = ["Raj", 10, 20, False]
for i in L:
  print(i)
print(i,L)
dict ={"Laptops": ["Infinix", "Apple", "Samsung"]}
for i in dict["Laptops"]:
  print(i)
print(i,dict)
# In the above code, we demonstrate the use of a for loop in Python to iterate through a list and a dictionary. In the first example, we iterate through the list `L` and print each element. After the loop, we print the last value of `i` (which will be `False`, the last element of the list) and the entire list `L`. In the second example, we access the values in a nested dictionary and print each laptop brand using a for loop. After the loop, we print the last value of `i` (which will be `Samsung`, the last brand in the list) and the entire dictionary `dict`. This demonstrates how to use for loops to iterate through different data structures in Python.
# In summary, the code demonstrates how to use for loops in Python to iterate through lists and dictionaries. The for loop allows us to execute a block of code for each item in the sequence, making it easy to process data without having to manually manage loop counters or indices. This is a fundamental concept in Python programming for controlling the flow of execution and performing operations on each element of a data structure efficiently.

L = ["Raj", 10, 20, False]
for i in L:
  print(i)
i+=1
print(i,L)

dict = {"Clothes": [{"Name": "Shirt"}, {"Name": "Jeans"}, {"Name": "Tshirt"}]}
for i in dict["Clothes"]:
  print(i["Name"])

  dict = {"Bags": [{"Sky Bags": ["Bag1","Bag2","Bag3","Bag4"]}]}
for i in dict["Bags"]:
  for j in i:
    for k in i[j]:
      print(k)


dict = {"Bags": [{"Sky Bags": ["Bag1","Bag2","Bag3","Bag4"]}]}
i = 0
while i < len(dict["Bags"][0]["Sky Bags"]):
  print(dict["Bags"][0]["Sky Bags"][i])
  i+=1

# In the above code, we demonstrate the use of both for loops and while loops to iterate through nested data structures in Python. The first example shows how to iterate through a list and print each element, while also demonstrating how to access the last value of the loop variable after the loop has completed. The second example demonstrates how to iterate through a nested dictionary and access specific values within it using for loops. The third example shows how to achieve the same result using a while loop, where we manually manage the loop counter to access each element in the nested list. This illustrates the flexibility of Python in allowing us to choose between different looping constructs based on our preferences and the specific requirements of our code.
# In summary, the code demonstrates how to use both for loops and while loops in Python to iterate through nested data structures such as lists and dictionaries. The for loop provides a convenient way to iterate through sequences, while the while loop allows for more manual control over the iteration process. Both constructs are essential tools in Python programming for processing data and controlling the flow of execution based on specific conditions. Understanding when to use each type of loop can help you write more efficient and readable code.

L = ["Hello", 10, 20, 30, 40]
for i in L:
  if i==20:
    print(i)
    break
print(i)


for i in range(5):
  if(i==2):
    continue
  print("i is:",i)

# In the above code, we demonstrate the use of the `break` and `continue` statements in Python. The first loop iterates through the list `L` and prints each element. When it encounters the value `20`, it prints it and then uses the `break` statement to exit the loop immediately. After the loop, we print the last value of `i`, which will be `20`. The second loop uses a `for` loop with a `range` of 5. When `i` is equal to `2`, it uses the `continue` statement to skip the rest of the loop body for that iteration and move on to the next iteration. This means that when `i` is `2`, it will not print "i is: 2", but it will print for all other values of `i`. This demonstrates how to control the flow of loops using `break` and `continue` statements in Python.
# In summary, the code demonstrates how to use the `break` and `continue` statements in Python to control the flow of loops. The `break` statement allows you to exit a loop prematurely when a certain condition is met, while the `continue` statement allows you to skip the current iteration and move on to the next one. These statements are essential for managing the flow of execution within loops and can help you write more efficient and readable code in Python programming.

masks = [100, 95, 85, 65]
for i in masks:
  if i == 95:
    print(i)
    break
  else:
    continue
    print(i)

# In the above code, we have a list of `masks` with different values. The for loop iterates through each element in the list. When it encounters the value `95`, it prints it and then uses the `break` statement to exit the loop immediately. For all other values, it uses the `continue` statement to skip the rest of the loop body for that iteration and move on to the next iteration. However, since the `print(i)` statement is placed after the `continue` statement, it will never be executed for any value other than `95`. This means that only `95` will be printed, and all other values will be skipped without being printed. This demonstrates how the placement of statements within a loop can affect the flow of execution when using `break` and `continue` statements in Python.

countries=["USA","Canada","India"]
countries.append("Spain")
countries.insert(1, "Arya")
print(countries)

# In the above code, we have a list of `countries` that initially contains "USA", "Canada", and "India". We use the `append()` method to add "Spain" to the end of the list. Then, we use the `insert()` method to add "Arya" at index `1`, which means it will be placed between "USA" and "Canada". Finally, we print the updated list of countries, which will output `['USA', 'Arya', 'Canada', 'India', 'Spain']`. This demonstrates how to modify a list in Python by adding new elements using both `append()` and `insert()` methods.
# In summary, the code demonstrates how to use the `append()` and `insert()` methods to modify a list in Python. The `append()` method adds an element to the end of the list, while the `insert()` method allows you to specify the index at which you want to add a new element. By using these methods, you can easily modify and manage lists in Python programming.

ages = [56, 72, 24, 46]
ages.reverse()
print(ages)

ages = [56, 72, 24, 46]
ages.sort()
print(ages)

ages = [56, 72, 24, 46]
ages.sort(reverse=True)
print(ages)

# In the above code, we demonstrate how to use the `reverse()` and `sort()` methods to manipulate a list of ages in Python. The `reverse()` method reverses the order of the elements in the list, while the `sort()` method sorts the elements in ascending order by default. By passing `reverse=True` to the `sort()` method, we can sort the elements in descending order. This allows us to easily rearrange and organize data in a list based on our requirements.
# In summary, the code demonstrates how to use the `reverse()` and `sort()` methods to manipulate a list in Python. The `reverse()` method changes the order of the elements in the list, while the `sort()` method organizes the elements in either ascending or descending order based on the parameters provided. These methods are essential for managing and organizing data in lists effectively in Python programming.