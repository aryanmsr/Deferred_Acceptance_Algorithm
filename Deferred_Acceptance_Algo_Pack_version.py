#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 21:54:10 2021

@author: aryan
"""

from Deffered_Acceptance_Algo_source import GaleShapley


thewomen = ["Amy", "Lacy" , "Katie", "Bertha"]


themen = ["John", "Peter", "Tyrion", "Max"]


thepref = {"John": ["Amy", "Lacy", "Katie", "Bertha"],
           "Peter":["Lacy", "Amy", "Katie", "Bertha"],
           "Tyrion":["Lacy", "Katie", "Amy","Bertha"],
           "Max": ["Lacy", "Katie", "Amy","Bertha"],
           "Amy": ["John", "Tyrion", "Peter", "Max"],
           "Lacy": ["Peter", "John", "Tyrion", "Max"],
           "Katie": ["Tyrion", "John", "Peter", "Max"],
           "Bertha": ["Tyrion", "John", "Peter", "Max"]}



eng = GaleShapley(themen, thewomen, thepref)

print(eng)


