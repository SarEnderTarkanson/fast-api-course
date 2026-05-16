user_dictionary={
    "username": "sarenderblanche",
    "name": "Alpy",
    "age": 32
}

for i, j in user_dictionary.items():
    print(i, j)

user_dictionary2 = user_dictionary.copy()

user_dictionary2.pop("age")
print(user_dictionary)
print(user_dictionary2)