import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_test_rotation=45, show_legend=False)
chart.title = 'Python project description'
chart.x_tests = ['httpie', 'django', 'flask']

plot_dict = [{'value': 45654, 'test': 'Description of httpie'},
             {'value': 34234, 'test': 'Description of django'},
             {'value': 39234, 'test': 'Description of flask'}
             ]
chart.add('', plot_dict)
chart.render_to_file('bar_descriptions.svg')