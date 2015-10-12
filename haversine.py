# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:35:02 2015

@author: Michelle
"""

"""Copied from Stack Overflow on Aug 11 2015 
 http://stackoverflow.com/questions/4913349/haversine-formula-in-python-
      bearing-and-distance-between-two-gps-points
"""
import math

#==============================================================================
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
     
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
#==============================================================================


print('hello')
print(math.pi)
print(haversine(32, -83, 33, -83))