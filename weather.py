degree=int(input("Enter the degree:"))
if degree <=26:
    print("Cold weather")
elif degree >26 and degree <=40:
    print("Normal weather stay fit")
else:
    print("Hot! Weather! drink some water")
fahrenheit=((degree*1.8)+32)
print("the fahrenheit value is",fahrenheit,"F")    

