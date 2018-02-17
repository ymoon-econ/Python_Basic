# Read data
f = open('US_births_1994-2003_CDC_NCHS.csv','r')
f = f.read()
rawdata = f.split('\n')

# purge the label
data = rawdata[1:]

# create function which read csvdata and produce inter list
def read_csv(csvdata):
    temp = open(csvdata,'r')
    temp = temp.read()
    temp = temp.split('\n')
    string_list = temp[1:]
    final_list = []
    for i in string_list:
        int_fields = []
        string_fields = i.split(',')
        for j in string_fields:
            int_fields.append(int(j))
        final_list.append(int_fields)
    return final_list

# Tabulate in dictionary form
def month_births(List):
    births_per_month = {}
    for i in List:
        if i[1] in births_per_month:
            births_per_month[i[1]] += i[4]
        else:
            births_per_month[i[1]] = i[4]
    return births_per_month

# More generally 
def calc_counts(Data, Col):
    Birth = {}
    for i in Data:
        if i[Col] in Birth:
            Birth[i[Col]] += i[4]
        else:
            Birth[i[Col]] = i[4]
    return Birth
