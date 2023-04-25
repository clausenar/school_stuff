import os
import time
os.system('clear')

with open("pippi02.txt") as f:
    lines=f.read()


en_ett=["en","ett"]
words=lines.split(" ")
stop_words=['gammal','gammalt','av','mycket','hel','egen','av','egen']
wrong=0
correct=0
for i,k in enumerate(words):
    guess=""
    if k in en_ett and words[i+1] not in stop_words:
        #print (words[i],words[i+1])
        while guess!=k:
            print ("________",words[i+1])
            guess=input("Är det en eller ett? ")
            wrong+=1
            if guess!=k:
                print ("Aghhhh, det är inte korrekt. Pröv igen!")
        correct+=1
        wrong-=1
            
        print ("Bra jobbat! Du har ",correct,"korrekt. Och",wrong,"fel")
        time.sleep(2)
            
        
       
