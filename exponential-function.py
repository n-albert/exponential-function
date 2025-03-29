# Implement the power function that computes //a// to the power of //b// using basic arithmetic operations
# (+, -, *, /).


def exponential_function(base, power):
    result = 0
    counter = 0

    result = 1

    while(counter < power):
        result *= base
        counter += 1

    return result

results = exponential_function(2, 4)

print(results)

