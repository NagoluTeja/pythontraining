
myname=str(input("enter name: "))
myage=int(input("enter age: "))
hundredthyear=2021+(100-myage)
print("the user  age will in the year",hundredthyear," become 100 years ")


------using functions-------

myname=str(input("enter name: "))
myage=int(input("enter age: "))
def age(n,a):
    hundredthyear=2021+(100-myage)
    return hundredthyear
print(myname," age become 100 in the year in ",age(myname,myage))