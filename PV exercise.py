# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:31:00 2024

@author: ibane
"""
import math

def calc_pv_array_size (building_length,building_width,roof_angle,pv_width,pv_height,pv_power):
    roof_length = building_length
    roof_width = building_width / math.cos(math.radians(roof_angle))

    roof_size = roof_length * roof_width
      
    NumberOfPanels = roof_size //((pv_width/1000)*(pv_height/1000))
    print("The maximum number of PV panels is %d." %NumberOfPanels)

    power_capacity = (pv_power * NumberOfPanels)/1000
    print("The power capacity is %d kWp." %power_capacity)
    
    return NumberOfPanels, power_capacity

calc_pv_array_size(28,8,22,1690,1046,400)




        
        
        