import os
from collections import namedtuple

# Build a list of Unicode codepoints from a string
print('----- LIST COMPREHENSIONS ------')
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

letters = 'abcdefghijklmnopqrst'
letters_list = [str.upper(letter) for letter in letters]
print(letters_list)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

print('----- GENERATOR EXPRESSIONS ------')
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

print('----- TUPLES ------')
city, year, population, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print(
    f"""Data about {city}
        Year: {year} 
        Population: {population} 
        Pop. change: {chg} 
        and Area: {area}""")

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# building a passport
for passport in sorted(traveler_ids):
    country, traveler_id = passport
    print(f'{country}/{traveler_id}')

for country, _ in traveler_ids:
    print(country)

# holding the return of a function with tuple unpacking
quotient, reminder = divmod(20, 3)
print(
    f'20 divided by 3 results in quotient {quotient} and reminder {reminder}')


path_to_file, file_name = os.path.split('/home/jacaceresf/test.json')
print(f"{file_name}'s path is {path_to_file}")

# Grabbing excess items by using *
a, b, *rest = range(5, 50, 5)
print(a)
print(b)
print(type(rest))

# we can apply the prefix to exactly one variable
# but it can be appear in any position
c, d, *f, g = range(2, 20, 2)
print(f'{c} of type {type(c)}')
print(d)
print(f'{f} of type {type(f)}')
print(g)

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
               ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
               ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
               ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
               ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
               ]

print('{:20} | {:^9} | {:^9}'.format('  City', 'lat.', 'long.'))
fmt = '{:20} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


print('----- NAMEDTUPLES ------')
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokio', 'JP', 36.933, (35.234234, 123.343434))
print(tokyo)
print(tokyo.population)

Person = namedtuple('Person', 'name last_name born_date nationality')

person = Person('Jorge', 'Caceres', '03/09/1997', 'paraguayan')

# Accessing fields by name
print(f'Person name -> {person.name} {person.last_name}')
print(f'Nationality -> {person.nationality}')

# Accessing field by its position
print(person[1])

print(person._fields)

print('|{:15}| | |{:20}| '.format('  Field name', 'Value'))
nt_fmt = '|{:15}| : |{:20}|'

for field, value in person._asdict().items():
    print(nt_fmt.format(field, value))


print('----- LIST SORT ------')
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(sorted(fruits, key=len))