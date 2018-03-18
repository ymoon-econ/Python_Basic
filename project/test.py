f = open('guns.csv','r')
f = csv.reader(f)
data = list(f)

# check
data[0:5]

# remove header
headers = data[0]
data = data[1:]

years = []
for i in data:
    years.append(i[1])
    
year_counts = {}
for i in years:
    if i in year_counts:
        year_counts[i] += 1
    else:
        year_counts[i] = 1

