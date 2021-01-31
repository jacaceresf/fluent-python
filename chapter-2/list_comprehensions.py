import os

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
print(f'20 divided by 3 results in quotient {quotient} and reminder {reminder}')


path_to_file, file_name = os.path.split('/home/jacaceresf/test.json')
print(f"{file_name}'s path is {path_to_file}")

#Grabbing excess items by using *
a, b, *rest = range(5, 50, 5)
print(a)
print(b)
print(type(rest))

#we can apply the prefix to exactly one variable
# but it can be appear in any position
c, d, *f, g = range(2, 20, 2)
print(f'{c} of type {type(c)}')
print(d)
print(f'{f} of type {type(f)}')
print(g)