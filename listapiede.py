"""
data una lista[1,2,2,4,5,8,9], calcolare e stampare a video la media
"""
somma=0
lista=[1,2,2,4,5,8,9]
for i in range(0,len(lista)):
    somma=somma+lista[i]
media=somma/len(lista)
print(media)