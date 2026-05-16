my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for i,j in my_vehicle.items():
    print(i,j)

vehicle2 = my_vehicle.copy()

vehicle2["number of tires"] = 4

vehicle2.pop("mileage")

for i in vehicle2:
    print(i)