# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:07:50 2018

@author: Diego Wanderley
"""

from enum import Enum

class Quality(Enum):
    GOOD = 1
    BAD = -1
    PARTIAL = 0
    

class RD(Enum):
    R0 = 0
    R1 = 1
    R2 = 2
    R3 = 3
    RX = -1


class Sex(Enum):
    F = -1
    M = 1
    

class Laterality(Enum):
    L = -1
    R = 1    
    
    
ANNOTATORS = [
'cef38b53-a00b-4cb2-9910-9b434420f28b',
'8508a0a6-929f-4609-a6c4-ab70af7ac10f',
'72c224f9-ea4e-41e9-bec4-6b6a2622d56a',
'252fb397-171f-48b0-b49f-36de705e7c5a',
'11e66e2e-eab2-4651-af1f-4e7fd3d2538a'
]


REGION =[
'',
'Braga',
'Esposende',
'FEIRA',
'Nordeste',
'RET5',
'RET9',
'Retinografo 11',
'Retinografo 15',
'Retinografo 6',
'VISUCAM-NM'
]