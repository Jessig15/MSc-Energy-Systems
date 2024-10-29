# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:31:00 2024

@author: ibane
"""
import math

building_length = 28
building_width = 8
roof_angle = 22
pv_width = 1690
pv_height = 1046
pv_power = 405

roof_length = building_length
roof_width = building_width * math.cos(math.radians(roof_angle))

roof_size = roof_length * roof_width
      
NumberOfPanels = roof_size //((pv_width/1000)*(pv_height/1000))
print("The maximum number of PV panels is %d." %NumberOfPanels)

power_capacity = pv_power * NumberOfPanels
print("The power capacity is %d kWp." %power_capacity)



        
        
        