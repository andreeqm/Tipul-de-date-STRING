str=input("Introduceti un sir de caracter: ")
majuscule=0
cifre=0
for i in str:
    majuscule+=i.isupper()
print("In sir sunt:",majuscule,"majuscule")
for i in str:
    cifre+=i.isdecimal()
print("Insir sunt:",cifre,"cifre")