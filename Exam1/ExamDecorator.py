# 890457906
# Alexander Sigler
# Question 4
function_3_count = 0
function_4_count = 0
function_5_count = 0

def decFunc(func):
    def inner(*args):
        if len(args) == 3:  # If the function has 3 args
            global function_3_count
            function_3_count = function_3_count+1  # Increase count
        elif len(args) == 4: # If the function has 4 args
            global function_4_count
            function_4_count = function_4_count + 1  # Increase count
        elif len(args) == 5: # If the function has 5 args
            global function_5_count
            function_5_count = function_5_count + 1  # Increase count
        return func(*args)
    return inner


@decFunc
def function_3(arg1, arg2, arg3):
    print('3 args')


@decFunc
def function_4(arg1, arg2, arg3, arg4):
    print('4 args')


@decFunc
def function_5(arg1, arg2, arg3, arg4, arg5):
    print('5 args')

function_3(1,2,3)
function_4(1,2,3,4)
function_5(1,2,3,4,5)
function_3(1,2,3)
function_4(1,2,3,4)
function_3(1,2,3)
function_3(1,2,3)
function_4(1,2,3,4)
function_5(1,2,3,4,5)
function_3(1,2,3)
function_4(1,2,3,4)
function_3(1,2,3)


print('Function 3 called ' + str(function_3_count))  # 6 times called
print('Function 4 called ' + str(function_4_count))  # 4 times called
print('Function 5 called ' + str(function_5_count))  # 2 times called
