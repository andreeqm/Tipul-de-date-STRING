c1=str(input("Introduceti primul cuvant: "))
c2=str(input("Introduceti al doilea cuvant: "))
c3=str(input("Introduceti al treilea cuvant: "))
c4=str(input("Introduceti al patrula cuvant: "))
a=str(c1)
b=str(c2)
c=str(c3)
d=str(c4)
n=0
if(((len(a))>=3)and((len(b))>=3)and((len(c))>=3)and((len(d))>=3)):
    n=(len(d))/2
    i=int(n)
    m=a[:2]
    o=b[0]
    l=c[:3]
    p=d[:1]
    print(c1," ",c2," ",c3," ",c4)
    print(str(m)+str(o)+str(l)+str(p))
else :
    print("Nu corespunde conditiei")