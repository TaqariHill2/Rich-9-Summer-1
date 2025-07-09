
Bedroom=["sunscreen, socks, shoes, hat"]
travelBag=[]
print("Pack your bags")
print("Enter the index of an item you'd like to move from your room to your bag")
print("Type '100' when you ar done packing\n") 
for item in Bedroom:
    print(item)

item= int(input("item Index"))
while item !=100:
    travelBag.append(Bedroom[item])
    Bedroom.remove(Bedroom[item])
    print("\nyour Bedroom:")
    print(Bedroom)
    print("\nyour Travel Bag")
    print(travelBag)
    item= int(input("item index:"))

    print("\nyour finished luggage")
    for item in travelBag:
        print(item)

