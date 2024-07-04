import math

distance_ft = 65 #distance to object
angle_deg = 74 # the angle to the top of the object

#convert degrees to radians
angle_rad = math.radians(angle_deg)
#calcuate the height of the object
height_ft = distance_ft * math.tan(angle_rad)
# Round to one decimal place
height_ft = round(height_ft, 1)

print(height_ft) # outputs 226.7

