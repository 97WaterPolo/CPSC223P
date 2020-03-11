import functools  # Needed for the reduce function


def calc_poly_func(r, n, m, a_list, x_list, y_list):
    N = min(len(a_list), len(x_list), len(y_list))  # Get the highest N value we can use
    # Use lambda function to generate each ith element
    ithElement = lambda ith: (a_list[ith] / r) * (x_list[ith]) ** n * (y_list[ith]) ** m
    ithList = []  # Used to track the ith element in list
    for i in range(0, N):  # Loop through our summation
        ithList.append(ithElement(i))  # Append it to the list
    return functools.reduce(lambda a, b: a + b, ithList)  # Sum it all up using reduce


print(calc_poly_func(1, 2, 3, [1, 2, 3], [2, 3, 4], [3, 4, 5]))  # Call our function
