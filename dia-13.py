numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([n for n in numbers if n < 0])

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([n for row in list_of_lists for inner in row for n in inner])

print([(n, 1, n, n*n, n*n*n, n*n*n*n, n*n*n*n*n) for n in range(0, 11)])

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print([country.upper()
       for row in countries for tup in row for country in tup])
