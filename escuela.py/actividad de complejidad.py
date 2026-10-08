# Creamos una lista de estudiantes 
student_list_01 = ['Jordan','Pipen','Curry','Shack','Demian','cruz','joshua'] # O(1)
def random_function(students): 
    first = students[0] # O(1) 
    total = 0 # O(1) 
    new_list = [] # O(1) 

    for student in students: # O(n) 
        print("se le suma 1 al total") #0(1)
        total += 1 # O(1) 
        new_list.append(student) # O(n)

    print(new_list) # O(1) 
    return total # O(1)

print(f"tamaño de la lista: {len(student_list_01)}")
print(random_function(student_list_01)) 
print("")
