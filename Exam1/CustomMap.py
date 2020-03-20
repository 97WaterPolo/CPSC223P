# 890457906
# Alexander Sigler
# Question 1


def custom_map_func(myCustomFunction, *lists):
    output = []
    minValue = len(lists[0])  # Default min Value
    for x in lists:
        minValue = len(x) if int(len(x)) < minValue else minValue  # Find the min value

    for i in range(0, minValue):  # Only go up to lists that we have same value for
        output.append(myCustomFunction(*[splitList[i] for splitList in lists]))  # Append value using lamda function
    return output  # Return the custom value


list1 = [1, 2, 3]
list2 = [2, 3, 4]
myCustomFunction = lambda a, b: a**5 + b**5
print(custom_map_func(myCustomFunction, list1, list2))
# Proper calculated value should be [33, 275, 1267]
