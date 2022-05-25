# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:06:57 2022

@author: Enqey De-Ben Rockson
"""

import random 

#responses can be written hear to avoind cluster on a code page

#create a function to reply to unclear random messages
def unknown():
    response = ['could you rephrase the ?',
                "....",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response
 
