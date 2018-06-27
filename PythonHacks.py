
# coding: utf-8

# # Unpacking

# In[65]:


a , b, c = (1, 2, 3)
print(a)
print(b)
print(c)


# # Output format

# https://www.python-course.eu/python3_formatted_output.php

# In[31]:


# pythonic way: use str.format()
print('Amount: {0:3d}, Price: {1:3.2f}'.format(100,20.33))
print('The number of items she purchased is {0:d} and the price for each item is {1:.2f}'.format(100,32.11))
print('The value is {:6,d}'.format(12345678))
print('The capital of {0:s} is {1:s}'.format('China','Beijing'))


# In[35]:


# use dictionary in format
print('The capital of {country} is {capital}'.format(country='China', capital='Beijing'))

capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print('\n')
format_string = 'The capital of {country} is {capital}'
for c in capital_country:
    print(format_string.format(country=c, capital=capital_country[c]))    


# In[37]:


# other string methods
"Beijing".center(20,'*')


# # Functional programming, map()

# syntax -- map(function, iterable1, iterable2 ... )
# iterable can be list, dictionary, tuple, set, string

# In[48]:


# compare prices from two stores
store1 = [10,6,3]
store2 = [11,4,7]
cheapest = map(min, store1, store2)

# min() won't be called unless we are really looking into the value
# map is iterable
print(cheapest)
for i in cheapest:
    print(i)


# # Lambda

# - create a anonymmous function
# - cannnot have default value or complex logic
# - lambda [input1, input2, input3...] : [expression of return value]

# In[96]:


# lambda with more than one input

full_name = lambda fname, lname: fname.strip().title() + " " + lname.strip().title()
full_name('  leonhaRd','EULER')


# In[97]:


# common example : sorting data 
# pass a function as an argument to sort() function

scifi_authors = ['Ray Bradbury', 'Robert Heinlein','Issac Asimov']
scifi_authors.sort(key = lambda name:name.split(' ')[-1].lower())
print(scifi_authors)


# In[98]:


# build a function that returns a function

def build_quadratic_function(a,b,c):
    return lambda x:a*x*x + b*x +c

f = build_quadratic_function(2,3,-1)
print(2*2*2+3*2-1)
print(f(2))

# another way to write, less readable tho
print(build_quadratic_function(2,3,-1)(2))


# # Combine lambda and map()

# In[135]:


# option 1
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

split = lambda x:x.split(' ')[0] + ' ' + x.split(' ')[-1]
for i in list(map(split,people)):
    print(i)


# In[165]:


# element-wise add of lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# use map
for i in map(lambda x,y:x+y, list1, list2):
    print(i)

# use list comprehension 
sum_2 = [sum(x) for x in zip(list1,list2)]
print(sum_2)


# # Zip()

# - zip takes n number of iterables and returns list of tuples. ith element of the tuple is created using the ith element from each of the iterables
# - python 3 uses lazy evalution. It won't return a list directly but instead, a zip object
# - unzip use zip() too but takes the zip object as input

# In[172]:


list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd', 'e']

# zip a list
zipped_list = zip(list_a, list_b)

# convert the zip object to a list
print(list(zipped_list))

# iterate through the zip object
for i in zipped_list:
    print(i)


# In[ ]:


# unzip a list, it works in Spyder
list1, list2 = zip(*zipped_list)
print(list1)
print(list2)


# In[175]:


# use zip() to format output
players = [ "Sachin", "Sehwag", "Gambhir", "Dravid", "Raina" ]
scores = [100, 15, 17, 28, 43 ]

for player, score in zip(players,scores):
    print('The score of %s is %d'%(player, score))


# # List comprehension

# - create an empty list and set a loop to add items is tedious
# - list comprehension allows people to create a list in a single line
# - **general expression** : [expression for value in collection]
# - **use if condition** : [expression for value in collection if 1 and 2]
# - **look for value in more than 1 collection** : [expression for value in collection1 for value in collection2]

# In[101]:


# without list comprehension
squares = []
for i in range(1,101):
    squares.append(i**2)

# with list comprehension
squares2 = [x**2 for x in range(1,101)]

print(squares)
print('\n')
print(squares2) 


# In[120]:


# quadratic reciprocity

prime_num = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
remainder_count = [len(set([x**2%p for x in range(1,101)])) for p in prime_num]
print(remainder_count)

theory = [(p+1)/2 for p in prime_num]
print(theory)


# In[129]:


# find the movie that starts with letter 'G'
# use if condition

movies = ['Star Wars', 'Gandhi', 'Casablanca', 'Gone with the wind', 'Rear Window']
gmovies = [title for title in movies if title.startswith('G')]
print(gmovies)

# find the movies that are released before(include) 2000
movies = [('Star Wars',1998), ('Gandhi',2000), ('Casablanca',1997), ('Gone with the wind',2005), ('Rear Window',1993)]
movies2000 = [title for (title,year) in movies if year<=2000]
print(movies2000)


# In[185]:


# common example: filtering data

num_list = [1,3,5,7,10]
result_list = [i for i in num_list if i > 5]
print(result_list)


# In[130]:


# scalar multiplication
v = [2,3,1]

# wrong operation
print(4*v)

# use list comprehension
print([4*item for item in v])


# In[133]:


# cartesian product
A = [1,3,5,7]
B = [2,4,6,8]
cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)


# # Filter()

# The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.

# In[191]:


my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70]

# use filter
result = list(filter(lambda x:x%13==0, my_list))
print(result)

# use list comprehension
# I prefer list comprehension. It's more readable
result2 = [x for x in my_list if x%13==0]
print(result2)


# # Generator

# - Sometimes the list is so large that merely creating it would consume all of the system's memory. 
# - To work around this, one may want to be able to call get_primes with a start value and get all the primes larger than start
# - generator can simply return the next value instead of all the values at once. It wouldn't need to create a list at all. No list, no memory issues. 
# - If the body of a def contains yield, the function automatically becomes a generator function (even if it also contains a return statement).
# - To be considered an iterator, generators must define a few methods, one of which is __next__(). 
# - To get the next value from a generator, we use the same built-in function as for iterators: next().
# -  You can "send" values to a generator using the generator's send method.

# In[9]:


# an ordinary iterable
# a list that stores prime numbers
import math
def get_prime(num_list):
    prime_list = [i for i in num_list if is_prime()]
    return prime_list

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


# In[10]:


# a simple generator 
def simple_generator():
    yield 1
    yield 2
    yield 3

# one way to use it : print out
for value in simple_generator():
    print(value)

# another way to use it : next()
num_gen = simple_generator()
next(num_gen)
next(num_gen)


# In[11]:


# generator version
# num is the start number
# use while True so that it won't hit the end of iteration if the first number is not a prime number
def prime_gen(num):
    while True:
        if is_prime(num):
            yield num
        num = num + 1

prime_gen_test = prime_gen(10)
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))


# In[12]:


# to set an upper limit
# if there is no upper limit, the loop will run forever to infinite when you are iterating over the prime_gen_test
def prime_gen(num,upper=100):
    while num<=upper:
        if is_prime(num):
            yield num
        num = num + 1

prime_gen_test = prime_gen(10,100)

for value in prime_gen_test:
    print(value)
    
# after we have exhausted all the numbers in the iterable, the 'StopIteration' will be raised
next(prime_gen_test)


# In[13]:


# if we want to restart, we can create a new generator
prime_gen_test2 = prime_gen(10,100)
next(prime_gen_test2)


# In[14]:


# we'll find the smallest prime number greater than successive powers of a number 
# for 10, we want the smallest prime greater than 10, then 100, then 1000, etc.

def successive_prime(base, power_limit):
    prime_list = []
    for power in range(1,power_limit+1):
        start = base**power
        prime_generator = prime_gen(start,100)
        prime_list.append(next(prime_generator))
    return prime_list


# In[ ]:


successive_prime(2,5)


# # why send() is not working??

# In[15]:


#  You can "send" values to a generator using the generator's send method
# iteration is a list of power
'''
When you're using send to "start" a generator (that is, execute the code from the first line of the generator 
function up to the first yield statement) you must send None.
'''

def successive_prime(iterations, base):
    prime_generator = prime_gen(base)
    prime_generator.send(None)
    for power in iterations:
        print(prime_generator.send(base**power))


# In[ ]:


successive_prime([1,2,3,4,5], 2)


# In[ ]:


def odd_gen(num):
    while True:
        if num%2!=0:
            yield num
        num = num + 1


# In[ ]:


def continuous_odd(base, power_list):
    odd_generator = odd_gen(base)
    odd_generator.send(None)
    result_list = []
    for power in power_list:
        result_list.append(odd_generator.send(base**power))
    return result_list
        

