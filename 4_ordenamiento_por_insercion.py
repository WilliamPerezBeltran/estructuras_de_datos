"""

Ordenamiento por selección 
es un algoritmo que consiste en ordenar los elementos de manera acendente odescendente 

fucniamiento 
-Recorremos cada elemento de la lista
-Cada ellemento de la lista se ordena si a suizquirerda tiene un elemento mayor que el actual
-Si es correcto el paso anteiror, se hace el intercambio de valores
-El elemento se sigue recorriendo hacia la  izquierda hasta que tenga un elemento menor que el 


"""
lista = [1,5,7,3,2,48,52,11,10,21,35,68,1,5,7,48,0]
print(lista)

for i in range(1,len(lista)):
	po = i
	cu = a[i]
	if a[i] < a[a-1]:
		for x in range(po,-1,-1):
			pivote = a[x-1]
			a[x-1] = a[x]
			a[x] = pivote
	
print(lista)