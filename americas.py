import pygal
from pygal.maps.world import COUNTRIES

wm = pygal.maps.world.World()
wm.title = 'North, central and south America'


# http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html
wm.add('North America', {'ca': 321651561, 'mx': 56415151,'us':456456})
wm.add('Central America', ['bz','cr','gt','hn','ni','pa', 'sv'])
wm.add('South America', ['ar','bo','br','cl','co','ec','gf','gy','pe','py', 'sr','uy','ve'])

wm.render_to_file('americas.svg')
#
# supra = pygal.maps.world.SupranationalWorld()
# supra.add('Asia', [('asia', 1)])
# supra.add('Europe', [('europe', 1)])
# supra.add('Africa', [('africa', 1)])
# supra.add('North america', [('north_america', 1)])
# supra.add('South america', [('south_america', 1)])
# supra.add('Oceania', [('oceania', 1)])
# supra.add('Antartica', [('antartica', 1)])
# supra.render()
# supra.render_to_file('continents.svg')