
# coding: utf-8

# # Simple Equation
# 
# Let us now implement the following equation:
# $$ y = x^2$$
# 
# where $x = 2$
# 

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate

# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')


# In[3]:


x=sympy.Symbol('x')
y=sympy.Function('y')

f=y(x)*(1 - y(x))*(1 -2*y(x))
sympy.Eq(y(x).diff(x),f)


# In[24]:


edo_sol=sympy.dsolve(y(x).diff(x)-f)#,ics=ics)
edo_sol


# In[23]:


ics = {y(0): .0001}#varia segun sea el rango entre [0,1]
C_eq1 = sympy.Eq(edo_sol[0].lhs.subs(x, 0).subs(ics), edo_sol[0].rhs.subs(x, 0))
C_eq1
C_eq2 = sympy.Eq(edo_sol[1].lhs.subs(x, 0).subs(ics), edo_sol[1].rhs.subs(x, 0))
C_eq2
ci=[C_eq1,C_eq2]
cn=[sympy.solve(C_eq1),sympy.solve(C_eq2)]
#soluciones de las cntes de integracion
cn


# In[40]:


#lim es d dnd grafica en x y y
def plot_direction_field(x, y_x, f_xy, x_lim=(-1,10), y_lim=(-1, 2), ax=None):
    """Esta función dibuja el campo de dirección de una EDO"""
    
    f_np = sympy.lambdify((x, y_x), f_xy, modules='numpy')
    x_vec = np.linspace(x_lim[0], x_lim[1], 20)
    y_vec = np.linspace(y_lim[0], y_lim[1], 20)
    
    if ax is None:
        _, ax = plt.subplots(figsize=(4, 4))
    
    dx = x_vec[1] - x_vec[0]
    dy = y_vec[1] - y_vec[0]
    
    for m, xx in enumerate(x_vec):
        for n, yy in enumerate(y_vec):
            Dy = f_np(xx, yy) * dx
            Dx = 0.8 * dx**2 / np.sqrt(dx**2 + Dy**2)
            Dy = 0.8 * Dy*dy / np.sqrt(dx**2 + Dy**2)
            ax.plot([xx - Dx/2, xx + Dx/2],
                    [yy - Dy/2, yy + Dy/2], 'b', lw=0.5)
    
    ax.axis('tight')
    ax.set_title(r"$%s$" %
                 (sympy.latex(sympy.Eq(y(x).diff(x), f_xy))),
                 fontsize=18)
    
    return ax


# In[41]:


x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
f =y(x)*(1 - y(x))*(1 -2*y(x))

# grafico de campo de dirección
fig, axes = plt.subplots(1, 1, figsize=(6, 6))
campo_dir = plot_direction_field(x, y(x), f, x_lim=(-1,10), y_lim=(0, 1), ax=axes)
ics = {y(0): 0}

# Resolviendo la ecuación diferencial
edo_sol = sympy.dsolve(y(x).diff(x) - f, ics=ics)
edo_sol


# In[21]:


import sympy

#define symbolic vars, function
x,y=sympy.symbols('x y')
fun=y*(1 - y)*(1 -2*y)

#take the gradient symbolically
#calcula el gradiente, hay que hacerlo a nivel de decimales
gradfun=[sympy.diff(fun,var) for var in (x,y)]

#turn into a bivariate lambda for numpy
numgradfun=sympy.lambdify([x,y],gradfun)

import numpy as np
import matplotlib.pyplot as plt

X,Y=np.meshgrid(np.arange(-10,11),np.arange(-3,3))
#X,Y=np.meshgrid(np.arange(-3,3),np.arange(0,2))
graddat=numgradfun(X,Y)

plt.figure()
plt.quiver(X,Y,graddat[0],graddat[1])
plt.show()


# In[43]:



# la convierto en una función ejecutable
f_np = sympy.lambdify((y(x), x), f)

# Definimos los valores de la condición inicial y el rango de x sobre los 
# que vamos a iterar para calcular y(x)

#graf bajo 1/2
y0 = 0.01
xp = np.linspace(0, 10, 100)

# Calculando la solución numerica para los valores de y0 y xp
yp = integrate.odeint(f_np, y0, xp)

#graf sobre 1/2
y0 = 0.9
yp2 = integrate.odeint(f_np, y0, xp)


#graf 0
xn = np.linspace(0, 10, 100)
yc = integrate.odeint(f_np, 0, xn)

#graf 1
xn = np.linspace(0, 12, 100)
ysu = integrate.odeint(f_np, -0.000001, xn)

yu = integrate.odeint(f_np, 1, xn)

fig, axes = plt.subplots(1, 1, figsize=(8, 6))
plot_direction_field(x, y(x), f, x_lim=(-1,12),ax=axes)
axes.plot(xn, yc, 'r', lw=2)
axes.plot(xn, yu, 'r', lw=2)
axes.plot(xn, ysu, 'g', lw=1)
axes.plot(xp, yp, 'b', lw=2)
axes.plot(xp, yp2, 'b', lw=2)

plt.show()


# In[25]:


# raices de la ec diferencial
x,y=sympy.symbols('x y')
fun=y*(1 - y)*(1 -2*y)
sympy.solve(fun)

