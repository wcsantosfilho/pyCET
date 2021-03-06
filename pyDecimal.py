#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 11:59:00 2019
#PYCET - Calculate Total Effective Cost (CET in portuguese)
@author: wcsantosfilho
"""

from decimal import Decimal

def xaxa(d1, d2):
    x = Decimal(d1)
    y = Decimal(d2)
    return x.compare(0.0)

a = Decimal('123.45')
b = Decimal('445.22')

print xaxa(a, b)
print xaxa(b, a)