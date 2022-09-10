
def prgm3(dict1,dict2):
    for i in dict2:
        if i in dict1:
            dict2[i] = dict2[i] + dict1[i]

    dict3 = {**dict1, **dict2}
    print(dict3)
    
dict1 = {}
dict2 = {}

for i in range(3):
    print("Dictionary one entry: ",i)
    entry1 = str(input("Entry One: "))
    entry2 = int(input("Entry Two: "))
    dict1[entry1] = entry2
    
for j in range(3):
    print("Dictionary two entry: ", j)
    entry3 = str(input("Entry One: "))
    entry4 = int(input("Entry Two: "))       
    dict2[entry3] = entry4

prgm3(dict1, dict2)







