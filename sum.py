# return a sum of any number of numeric arguments

def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(sum(1, 2, 3, 4, 5, 5, 6, 6, 7))