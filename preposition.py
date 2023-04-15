import os
import time

with open("pippi02.txt") as f:
    lines=f.read().strip()

lines=lines.split(".")
preposition=["i","på","under","vid","med","till"]
for line in lines:
    test=0
    ord=""
    substrings=line.split()
    newstring=[]
    for i,s in enumerate(substrings):
        if s in preposition:
            #print ("found preposition")
            s_query=s
            s="______"
            test+=1

        newstring.append(s)
    if test==1 and i==len(substrings)-1:
        print (" ".join(newstring))
        while ord!=s_query:
            ord=input("Skriv preposition som saknas: ")
        if ord==s_query:
            print ("-------------BRA-----------------    ")
            time.sleep(3)
    else:
        print (line)
