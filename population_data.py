import json
from pygal.maps.world import COUNTRIES
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

def get_country_code(country_name):
    """ Returns the two digit country code for the given country
    as the country code in our dataset is 3 digit"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code



filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

max_pop = 1
max_pop_name = ''
cc_populations = {} # to buid a dictionary of population data
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        country_code = pop_dict['Country Code']
        year = pop_dict['Year']
        population = int(float(pop_dict['Value']))
        print("Country: " + country_name + " Country Code: " + country_code + " Year: " + year +
              " Population: " + str(population))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
            cc_populations[code] = population
        else:
            print("Error -" + country_name)
        # This if gives you the highest population
#         if float(pop_dict['Value']) > max_pop:
#             max_pop = int(float(pop_dict['Value']))
#             max_pop_name = pop_dict['Country Name']
#
# print("Highest pop: " + str(max_pop_name) + " ---> " + str(max_pop))


# See how many countries are in each category
pop1, pop2, pop3 = {}, {}, {}
for country_code_pop, country_pop in cc_populations.items():
    if country_pop < 10000000:
        pop1[country_code_pop] = country_pop
    elif country_pop < 1000000000:
        pop2[country_code_pop] = country_pop
    else:
        pop3[country_code_pop] = country_pop

#Size of each category
print('First= ', len(pop1), 'Second= ', len(pop2), 'Third= ', len(pop3))

# print(COUNTRIES.items())
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
# # similarly we have below code which returns the same result
# for code,name in COUNTRIES.items():
#     print(code, name)

# print(get_country_code('Iran, Islamic Republic of'))

wm_style = RotateStyle('#0000FF', base_style= LightColorizedStyle) #RGB  00-->FF
# wm_style = LightColorizedStyle
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population in 2010'
# wm.add('2010', cc_populations) using this we don't have any categories

wm.add('0-10m', pop1)
wm.add('10m-1bn', pop2)
wm.add('>1bn',pop3)
wm.render_to_file('World_population2010.svg')