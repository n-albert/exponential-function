# Implement the power function that computes //a// to the power of //b// using basic arithmetic operations
# (+, -, *, /).


def recursive_exponential_function(base, power):

    if power == 0:
        result = 1
    else: 
        result = base * recursive_exponential_function(base, power - 1)

    return result

results = recursive_exponential_function(2, 4)

print(results)
