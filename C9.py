# Teacher Activity 1 and Additional Activity 1
for i in range(3): 
    print(i)
    
for i in range(1,4):
    print(i)
        
        
# Teacher Activity 2        
a = ["b","f","b","f","f"]
for i in a:
    if i == "b":
        print(i)
    elif i == "f":
        print(i)
        
        
# Student Activity        
a = ["b","f","b","f","f", "c", "c"]
for i in a:
    if i == "b":
        print(i)
    elif i == "f":
        print(i)
    elif i == "c":
        print(i)
        


# Additional Activity 2
import random        
ring = random.randint(1,18)
print(ring)
for i in range(1,19):
    if i == ring:
        print(i)
        break
    print(i)
