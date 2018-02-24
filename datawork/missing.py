# Missing data?

# Either
# 1. Remove any rows that contain missing data.
# 2. Populate the empty fields with a specified value 
# 3. Populate the empty fields with a calculated value
# 4. Use analysis techniques that work with missing data


import csv
f = open('legislators.csv')
f = csv.reader(f)
legislators = list(f)

gender = []
for i in legislators:
    gender.append(i[3])
gender = set(gender)

# ' ' is missing value

# Let's replace it with 'M'
for i in legislators:
    if i[3] == '':
        i[3] = 'M'
        
birth_years = []
for i in legislators:
    parts = i[2].split('-')
    birth_years.append(parts[0])
    
