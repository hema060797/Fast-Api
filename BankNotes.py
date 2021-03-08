# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 04:00:59 2021

@author: l
"""


#Basemodel inherting from pydantic
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float
