#Crea un script que le pida al usuario una lista de países (separados por comas). 
#Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente 
#y separados por comas.panama, panama, japon, alemania, colombia, rusia

entrada = input("Ingrese nombre de paises separados por coma")
paises = entrada.split(',')
print("colocando comas con split", paises)
l = set(paises)
print("verificando se hay paises repetidos con set", l)
paisesOrdenados = sorted(l)
print("ordenamos la lista con los paises con sorted()", paisesOrdenados)