from guitar import Guitar
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Line 6 JTV-59", 2013, 1512.9)
age1 = guitar1.get_age()
print(age1)
age2 = guitar2.get_age()
print(age2)
vintage1 = guitar1.is_vintage(age1)
print(vintage1)
if vintage1 == True:
    print(guitar1 , str("(vintage)"))
else:
    print(guitar1)
vintage2 = guitar2.is_vintage(age2)
print(vintage2)
if vintage2 == True:
    print(guitar2 , str("(vintage)"))
else:
    print(guitar2)