# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:01:40 2015

@author: Ruofei
"""
from markov_python.cc_markov import MarkovChain

file=open("test.txt")

mc=MarkovChain(file)

print mc.generate_text()

