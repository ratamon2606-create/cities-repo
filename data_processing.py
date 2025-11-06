import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

def filter(condition, dict_list):
    return [d for d in dict_list if condition(d)]

def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [float(d[aggregation_key]) for d in dict_list if aggregation_key in d]
    return aggregation_function(values)


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(aggregate('temperature',lambda x: sum(x)/len(x), cities))
print()

# Print all cities in Germany
print("All cities in Germany:")
germany = filter(lambda x: x['country'] == 'Germany',cities)
print(', '.join([c['city'] for c in germany]))
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
spain = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
print(', '.join([c['city'] for c in spain]))
print()


# Count the number of unique countries
print("Count the number of unique countries:")
print(len(set(c['country'] for c in cities)))
print()


# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany:")
avg = aggregate('temperature', lambda x: sum(x)/len(x), germany)
print(avg)
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy:")
italy = filter(lambda x: x['country'] == 'Italy', cities)
imax = aggregate('temperature', max, italy)
print(imax)
print()