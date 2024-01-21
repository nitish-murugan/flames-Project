name1 = input("Enter your name without any spaces => ")
name2 = input("Enter your partner name without any spaces => ")

name1 = list(name1.upper())
name2 = list(name2.upper())
for i in name1:
    if i in name2:
        index = name1.index(i)
        name1[index] = "-"
        index = name2.index(i)
        name2[index] = "-"

names = name1 + name2
count =  0
for i in names:
    if(i != '-' and ' '):
        count+=1

flames = ['Friends','Love','Affection','Marriage','Enemy','Siblings']
index = 0
for i in range(5):
    for j in range(count):
        index+=1
        if(index > len(flames)):
            index = 1
    flames.remove(flames[index-1])
    index-=1
print(flames[0])
ii = input("Press any key to exit")

