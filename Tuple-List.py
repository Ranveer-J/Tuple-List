def convert_tuple_to_list(data_tuple):
    return list(data_tuple)


person_tuple = ("Alice", 30, 5.5, "blue", "pizza")


person_list = convert_tuple_to_list(person_tuple)

# Display the result
print("Original tuple:", person_tuple)
print("Converted list:", person_list)
