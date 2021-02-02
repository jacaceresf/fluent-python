
def power_number(n):
    '''power n to n'''
    return n**n


def sum_number(n):
    '''add the n to n'''
    return n + n


def factorial(n):
    ''' returns n! '''
    return 1 if n < 2 else n * factorial(n-1)


def call_first_class_function(n, function_name):
    print('Calling [{:15}] which [{:20}] and return -> [{:9}]'.format(
        function_name.__name__, function_name.__doc__, function_name(n)))


print(factorial(2))

print(factorial(5))

print(factorial(7))

print(factorial.__doc__)

print(type(factorial))

fact = factorial
print(fact)

_fact = fact(5)
print(_fact)

call_first_class_function(5, factorial)

call_first_class_function(5, power_number)
call_first_class_function(4, sum_number)

result = list(map(fact, range(5)))
print(result)


result_2 = [factorial(n) for n in range(10) if n % 2 != 0 ]
print(result_2)
