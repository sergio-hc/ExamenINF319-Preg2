# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:25:06 2021

@author: SERGIO
"""

from pyswip import Prolog
p = Prolog()

p.assertz("padrede(Juan,Maria)")
p.assertz("padrede(Pablo,Juan)")
p.assertz("padrede(Pablo,Marcela)")
p.assertz("padrede(Carlos,Debora)")

list(p.query("padrede(Juan,X)"))==[{'X':'Maria'}]
list(p.query("padrede(Pablo,X)"))==[{'X':'Juan'},{'X':'Marcela'}]
list(p.query("padrede(Carlos,X)"))==[{'X':'Debora'}]
for elemento in p.query("padrede(X,Y)"):
    print(elemento["X"], "es padre de ", elemento["Y"])