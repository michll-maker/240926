"""
#los generadores son funciones que pueden pausar su ejecucion.
#cuando se invoca una funcion generador ( aka inter)

# el codigo dentro de la funcion no se ejecuta 
# de inmediato solo se compila.

# la funcion se ejecuta unicamente cuando 
# iteras sobre el generador  

"""

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
#se invoca la funcion generador

my_iterator = my_generator()
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4
#se itera manualmente sobre el generador

#print(next(my_iterator))#1
#print(next(my_iterator))#2
#print(next(my_iterator))#3
#print(next(my_iterator))#4

#los interadores se puede iterar con un for
for value in my_iterator:
    print(value)
