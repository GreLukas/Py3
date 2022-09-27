#1
txt = "datel"[::-1]
print(txt)

#2
cislo = "1456"[::-1]
print(cislo)

#3
veta = "Řetezce se nechovají jako seznamy."
print(veta.replace("nechovají", "chovají"))

#4
text = 'Ramanujan byl velmi zajímavý geniální indický matematik'
print(len(text.split()))

#5
list = [1,2,3,4,5,6]
x =  int(input("Number Expected "))
if x in list:
    print("this number is in the list")
else:
    print("this number is not in the list")

#6
numbers = [1, 2, 3, 4, 5, 6, 7]
for i in numbers:
    print(i * i)