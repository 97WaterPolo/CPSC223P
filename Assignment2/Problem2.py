def sanitize(func):
    def inner(l1, l2):
        newl2 = []  # Create a new list to add the new objects too
        for x in l2:
            # If it is a number or a string then add it to new list
            if type(x).__name__ == 'str':  # Make sure that it is a string
                for z in x.split(","):  # Split on the comma
                    newl2.append(z)  # Append it to the new list
            elif x >= 4:  # If the number is greater than or equal to 4
                newl2.append(x)  # Add it to the new list
        return func(l1, newl2)  # Return the original call with new params

    return inner


@sanitize
def combine_with_list(list_obj, list2_obj):
    list_obj.extend(list2_obj)  # Extend appends the second iterable object to the list
    return list_obj


@sanitize
def combine_with_set(list_obj, set_obj):
    list_obj.extend(set_obj)  # Extend appends the second iterable object to the list
    return list_obj


print(combine_with_list([1, 2, 3], ["Is,this,one,that,counts", 3, 4, 5, 7, 8, True, -986]))
print(combine_with_set([1, 2, 3], {"hi,l,o,l,1,2,3,4,5", 1, 2, 3, 2.2, -9264, 5, 6}))
