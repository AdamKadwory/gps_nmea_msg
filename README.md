# gps_nmea_msg



"""
** There is different NMEA messages that GPS communicate with, just for clarfication, but the main focus 
is on GPRMC
objective: create a function that read NMEA messages in file, extract the specific NMEA message 
and split the data to creat a table that shows the parsed payloads. 
- for latitude, there is a direction S(south) or N(North), and for longitiude W(west) and E(east)
- data need to be saved or converted from float to integers(degree) 2int 
"""
