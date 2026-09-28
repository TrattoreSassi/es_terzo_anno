"""
data una lista di 20 elementi di temperature randomiche nell'intervallo -20, 40, calcolare il numero di elementi sopra lo 0,
sotto lo 0 e stampare a video la scritta freddo estremo se le temperature sotto 0 superano quelle sopra, caldo estremo nell'altro
caso
"""
import random
temperature=[]
tsot=0
tsop=0
for i in range (0,20):
    temperature.append(random.randint(-20,40))
for i in range (0,20):
    if temperature[i] < 0:
        tsot=tsot+1
    else:
        tsop=tsop+1
    
    
if tsot>tsop:
    print("freddo estremo")
else:
    print("caldo estremo")
        
    
