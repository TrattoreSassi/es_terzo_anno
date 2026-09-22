"""

scrivi un programma che:
chiede all'utente la distanza percorsa (in m) e il tempo impiegato (in s).
calcola la velocità media.
stampa il risultato con due cifre decimali e indica l'unità di misura

"""

distanza=input("inserire la distanza in m: ")
distanza=float(distanza)
tempo=input("inserire il tempo impiegato in s: ")
tempo=int(tempo)
velocità=distanza/tempo
velocità=round(velocità,2)
print("la velocità è: "+str(velocità))