def get_zone(x,y,width,height):
    zone_width = width//3

    if x < zone_width:
       return "Zone A"
    elif x <2*zone_width:
        return "Zone B"
    else:
        return "Zone C"
