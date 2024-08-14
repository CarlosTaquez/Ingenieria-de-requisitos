#AREA RECTANGULO
print ("'area rectangulo")

base_rectangulo = input("digite la base: '")

altura_rectangulo = input("digite la altura: ")

area_rectangulo = int (base_rectangulo)*int(altura_rectangulo)
print (f'la area total del rectangulo es {area_rectangulo}')
#AREA TRIANGULO
print ("area triangulo")

base_triangulo = input("digite la base: ")
altura_triangulo = input ("digite la altura: ")
area_triangulo = int(base_triangulo)*int(altura_triangulo)/2
print (f'la area total del triangulo es {area_triangulo}')

#AREA DEL TERRENO
print ("area total del terreno")
area_terreno = area_rectangulo+area_triangulo
print (f'la area tota ldel terreno es {area_terreno}')