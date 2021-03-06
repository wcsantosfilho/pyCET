#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 09 11:59:00 2019
#PYCET - Calculate Total Effective Cost (CET in portuguese)
@author: wcsantosfilho
"""

import datetime as dt
from datetime import timedelta
import decimal
import numpy as np


def bdays_between(d2, d1):
    x = dt.date(d1.year, d1.month, d1.day)
    y = dt.date(d2.year, d2.month, d2.day)
    return np.busday_count(x,y)


def days_between(d1, d2):
    return abs((d2 - d1).days)

#POC numpy
x = dt.date(2019, 12, 15)
y = dt.date(2020, 1, 15)
days = np.busday_count(x, y)

print days
#END POC

#Define precision for Decimal class
decimal.getcontext().prec = 18
#Make a series of installments
installments=[decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97'),decimal.Decimal('55.97')]
#Define other inputs
print installments
totalCreditValue = decimal.Decimal(1000.00)
effectiveTotalCost = decimal.Decimal(0.11)
aproximatedTotalCost = decimal.Decimal(0)
baseDateForInterest = dt.date(2019,12,15)
baseDateForPayment = dt.date(2020,1,15)

rateStep = decimal.Decimal(0.005)
currentError = decimal.Decimal(0)
lastError = decimal.Decimal(0)
aproximatedTotalCost = effectiveTotalCost
enough = True
while enough == True:
    sumOfPaymentsInPresentValue = decimal.Decimal(0)
    current = baseDateForPayment
    for inst in installments:
        differenceOfDates = decimal.Decimal(days_between(current, baseDateForInterest))
        powerToInstallmentPresValue = decimal.Decimal(differenceOfDates / 365)
        denominator = (decimal.Decimal(1) + aproximatedTotalCost) ** powerToInstallmentPresValue
        installmentPresentValue = ( decimal.Decimal(inst) / decimal.Decimal(denominator))
        sumOfPaymentsInPresentValue += installmentPresentValue
        current += timedelta(days=30)
        current = dt.date(current.year, current.month, baseDateForPayment.day)
    currentError = sumOfPaymentsInPresentValue - totalCreditValue
    
    print("% 5.2f - % 0.18f - % 0.18f" %(sumOfPaymentsInPresentValue,currentError,lastError))

    if ( currentError.compare(0) == decimal.Decimal('-1') and lastError.compare(0) == decimal.Decimal('1')) or \
        ( currentError.compare(0) == decimal.Decimal('1') and lastError.compare(0) == decimal.Decimal('-1')):
        rateStep = ( rateStep / 2 ) * -1
    if currentError.compare_total_mag(decimal.Decimal(0.000000000000000001)) == decimal.Decimal('-1') or \
        currentError.compare(lastError) == decimal.Decimal('0'):
        enough = False
    else:
        aproximatedTotalCost += rateStep
    lastError = currentError
print ("% 0.8f" %(aproximatedTotalCost*100))
x = decimal.Decimal(1) / decimal.Decimal(12)
y = ((1+aproximatedTotalCost)**(x))-1
print ("% 0.8f" %(y*100))
print(" -----------")
print("FIM")