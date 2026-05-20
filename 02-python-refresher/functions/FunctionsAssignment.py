def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age
    }
    return created_user_dictionary

solution_dictionary = user_dictionary(firstname="Alpy", lastname="Tarkanson", age=40)
print(solution_dictionary)