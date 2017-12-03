import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Status Code: ", req.status_code)


response_dict = req.json() # to store the result in a python dictionary
print("Dictionary Keys: ", response_dict.keys())
print("Number of projects: ", response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print("Number of Repositories: ", len(repo_dicts))

# to print name of the repositories
max_stars = 0
max_stars_name = ''
print("\nRepository names are: ")
for index, value in enumerate(repo_dicts):
    repo_dict = repo_dicts[index] # convert a list to a dictionary as each item is a ssingle dictionary
    print(index, ' - ', repo_dict['name'], ' Stars: ', repo_dict['stargazers_count'])
    if int(repo_dict['stargazers_count']) > max_stars:
        max_stars = repo_dict['stargazers_count']
        max_stars_name = repo_dict['name']
print('Highest stars is ', max_stars_name, ' with ', max_stars, ' stars')

# Examine the first repository
repo_dict = repo_dicts[0] # need to convert a list to a dic
print("\nKeys: ", len(repo_dict))
for key in repo_dict.keys():
# for key in sorted(repo_dict.keys()):
    print(key)


# Visualizing the repositories
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

description_plots, names, stars = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    description = repo_dict['description']
    if not description: # we handle the issue of passing any empty value to the list
        description = "No Description provided"
    description_plot = {
                    'value': repo_dict['stargazers_count'],
                    'label': description,
                    'xlink': repo_dict['html_url']
    }
    description_plots.append(description_plot)

my_style = LS('#333366', base_style=LCS)
my_style.label_font_size = 18
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=True) after using my_config we changes it
# chart = pygal.HorizontalBar(style=my_style, x_label_rotation=45, show_legend=True)
chart.title = 'Most starred repositories'
chart.x_labels = names

# chart.add('Number of stars', stars) after adding the label and description instead of stars we used description_plotS, so in this case we have stars and description at the same time in the chart
chart.add('Number of stars', description_plots)

chart.render_to_file('Python_repositories.svg')




line_chart = pygal.StackedBar()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file('sample.svg')

from pygal.style import NeonStyle
chart2 = pygal.StackedLine(fill=True, interpolate='cubic', style=NeonStyle)
# chart2.x_labels = map(str, range(2002, 2013))
chart2.add('A', [1, 3,  5, 16, 13, 3,  7])
chart2.add('B', [5, 2,  3,  2,  5, 7, 17])
chart2.add('C', [6, 10, 9,  7,  3, 1,  0])
chart2.add('D', [2,  3, 5,  9, 12, 9,  5])
chart2.add('E', [7,  4, 2,  1,  2, 10, 0])
chart2.render_to_file('sampleNeon.svg')

from pygal.style import DarkSolarizedStyle
chart3 = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkSolarizedStyle)
chart3.add('A', [1, 3,  5, 16, 13, 3,  7])
chart3.add('B', [5, 2,  3,  2,  5, 7, 17])
chart3.add('C', [6, 10, 9,  7,  3, 1,  0])
chart3.add('D', [2,  3, 5,  9, 12, 9,  5])
chart3.add('E', [7,  4, 2,  1,  2, 10, 0])
chart3.render_to_file('sampleNeonDark.svg')