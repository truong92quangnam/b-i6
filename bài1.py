#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle
import math
t=turtle.Turtle()
t.shape("turtle")
a=200
goc=72
t.pencolor('blue')

t.begin_fill()
t.fillcolor('red')  

t.forward(a)
t.left(goc)
t.forward(a)
t.left(goc)
t.forward(a)
t.left(goc)
t.forward(a)
t.left(goc)
t.forward(a)
t.left(goc)

t.end_fill()

p=5*a
S=math.sqrt(25+10*math.sqrt(5))*pow(a,2)/4
print(p)
print(round(S,3))
turtle.done()

