import math
root = math.sqrt(99)
flr  = math.floor(89.9)

# or 
import math as m
root = sqrt(89)



# import every object in a module
from math import *
root = sqrt(1001)

# module contains not only the functions
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)


# easier way to load data (use csv module)
import csv

f = open('nfl.csv')
f = csv.reader(f)
nfl = list(f)
