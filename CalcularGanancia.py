print ("control de regsitro")

produccion_litros = input("digite producido en litros: ")

print ("conversion")

conversion = int (produccion_litros)*float (3.785)

print ("valor galon")

valor = input("digite el valor: ")
print ("ganacias")
ganancia = conversion*int(valor)
print (f'la ganancia del productor es {ganancia}')