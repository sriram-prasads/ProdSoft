# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 12:42:05 2021

@author: Sriram Prasad S
"""

f1 = open("mset.txt","r")
lines = f1.readlines()
xy = float(lines[0])
yz = float(lines[3])

print(xy + yz)