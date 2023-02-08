import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
sp.init_printing()
import numpy as np
#from bokeh.io import output_notebook
from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot
from bokeh.models import Slider, Div
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes

#output_notebook()

S = sp.Symbol('S',real=True) #narażeni
I = sp.Symbol('I',real=True) #chorzy
R = sp.Symbol('R',real=True) #usunięci
beta = sp.Symbol('beta',real=True) #zarazliwosc
gamma = sp.Symbol('gamma',real=True) #zdrowotnosć
t=sp.Symbol('t',real=True)

macierz = sp.lambdify((t,[S,I,R],beta,gamma),[-beta*S*I,beta*S*I-gamma*I,gamma*I])
ts = np.linspace(0, 50, 5000)

S0 = 0.999
R0= 0
I0 = 0.001
B = 2
G = 1.5
sol = solve_ivp(macierz, (0, 50), [S0,I0,R0], t_eval=ts, args=[B, G])
fig = figure(title ='SIR',
             x_axis_label = 'days',
             y_axis_label = 'population')
fig.toolbar.logo = None
fig.toolbar.autohide = True
fig.grid.grid_line_dash =(5,5)
hb1 = fig.line(ts, sol.y[0], color = 'orange', line_width =3, legend_label = 'S')
hb2 = fig.line(ts, sol.y[1], color = 'green', line_width =3, legend_label = 'I')
hb3 = fig.line(ts, sol.y[2], color = 'black', line_width =3, legend_label = 'R')

B = 2
G = 1.5
S0 = 0.999
R0= 0
I0 = 0.001
def solvingB(attr, old, new):
  B = new
  sol = solve_ivp(macierz, (0, 50), [S0,I0,R0], t_eval=ts, args=[B, G])
  hb1.data_source.data = sol.y[0]
  hb2.data_source.data = sol.y[1]
  hb3.data_source.data = sol.y[2]
def solvingG(attr, old, new):
  G = new
  sol = solve_ivp(macierz, (0, 50), [S0,I0,R0], t_eval=ts, args=[B, G])
  hb1.data_source.data = sol.y[0]
  hb2.data_source.data = sol.y[1]
  hb3.data_source.data = sol.y[2]
s1 = Slider(start = 0.1, end = 10.1, step = 0.5, value = 2.1, title = 'Beta', sizing_mode = 'stretch_width')
s1.on_change('value_throttled', solvingB)
s2 = Slider(start = 0.1, end = 10.1, step = 0.5, value = 1.6, title = 'Gamma', sizing_mode = 'stretch_width')
s1.on_change('value_throttled', solvingG)
row(column(s1, s2), fig)

#show(row(column(s1,s2, width =200), fig))
curdoc().add_root(row(column(s1,s2, width =200), fig))