str=input("Introduceti un sir de caractere: ")
c=0
for i in str:
    c+=i.isdecimal()
print("In sir sunt",c,"cifre")
