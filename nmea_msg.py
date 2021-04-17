
"""
** There is different NMEA messages that GPS communicate with, just for clarfication, but the main focus 
is on GPRMC

objective: create a function that read NMEA messages in file, extract the specific NMEA message 
and split the data to creat a table that shows the parsed payloads. 

- for latitude, there is a direction S(south) or N(North), and for longitiude W(west) and E(east)
- data need to be saved or converted from float to integers(degree) 2int 
"""

# set the path of the file that include NMEA messages coordinates 
gps_file = "/Users/ahmedabdalsattar/Desktop/nmea.txt"

def gps_cord_nmea(gps_file):
    # store them as a dictionary data (hashed), in case we call them later, or there 
    # more than one NMEA message type beside the GPRMC 
    gps_nmea_msg = {
        "time_fix_data":[],
        "navig_rec":[],
        "latitude":[],
        "longitude":[],
        "sog":[],
        "cmg":[],
        "date_fix":[],
        "mag_var":[],
        "checksum":[]    
    }

    read_file = open(gps_file,"r")
    for i in read_file:
        #read the txt file that include gps NMEA messages data 
        gps_cord = read_file.readline()
        #split the values within each coordinate 
        gps_data = gps_cord.split(",")
        #extract only GPRMC NMEA message 
        if gps_data[0] == '$GPRMC':
    #         print(gps_data)

            # extract Time of Fix UTC and append in dictionary 
            time_fix = gps_data[1]
            print(time_fix, '    |Time of fix')
            gps_nmea_msg["time_fix_data"].append(time_fix)


            #extract Navigation reciver warning A = ok, V = warning 
            navig_AV = gps_data[2]
            print(navig_AV, '         |navigation reciever warning')
            gps_nmea_msg["navig_rec"].append(navig_AV)

            # extract Latitude in degree
            latitude = gps_data[3]   #latitude value 
            lat_deg = latitude[:2]   #latitude degree 1st 2 integers 
            lat_rem = latitude[2:10] #latitude minutes (remainder)

            # latitude can be in the South(S) = -# or North(N) = +#. 
            if gps_data[4] == "N":
                latitude = float(latitude) * -1 
                print(str(latitude) + ',' +  gps_data[4],'|latitude ' + lat_deg + ' degree. ' + lat_rem + ' min ' + gps_data[4] )
            else:
                latitude = gps_data[3]
                print(str(latitude) + ','+ gps_data[4], '|latitude ' + lat_deg + ' degree. ' + lat_rem + ' min ' + gps_data[4] )
            gps_nmea_msg["latitude"].append(latitude)



            # extract longitude in degree           
            longitude = gps_data[5] 
            long_deg = longitude[:3]
            long_rem = longitude[3:10]

            # longitude can be West(W)= -# or East(E) = +#.
            if gps_data[6] == "E":
                longitude = float(gps_data[5]) * -1 
                print(str(longitude)+ ','+ gps_data[6], '|longitude ' + long_deg + ' degree. '+lat_rem + ' min ' + gps_data[6])
            else:
                longitude = gps_data[5] 
                print(str(longitude) + ',' + gps_data[6], '|longitude ' + long_deg + ' degree. '+ lat_rem + ' min ' + gps_data[6])
            gps_nmea_msg["longitude"].append(longitude)
        
            #extract speed over ground, knots 
            sog = gps_data[7]
            print(sog, '     |speed over ground')
            gps_nmea_msg["sog"].append(sog)

            #extract Course Made Good
            cmg = gps_data[8]
            print(cmg, '     |Course Made Good')
            gps_nmea_msg["cmg"].append(sog)
            
            
            #extract date of fix 
            date_fix = gps_data[9]
            print(date_fix,'    |date of fix ' )
            gps_nmea_msg["date_fix"].append(date_fix) 
                
            #extract Magnatic Variation in degree 
            mag_var = gps_data[10]
            print(mag_var, '     |Magnatic Variation ')
            gps_nmea_msg["mag_var"].append(mag_var)

            #extract mandatory checksum 
            checksum = gps_data[11]
            print(checksum, '          |mandatory checksum')
            gps_nmea_msg["checksum"].append(checksum)
            
            print('-------------------------------------')
            
    print(gps_nmea_msg)
    return gps_nmea_msg
if __name__ == "__main__":
    #run the function 
    gps_cord_nmea(gps_file)
    
    
    
    
# in case we want to modify the code to make it work with different NMEA messages 
# we can create more conditions for GSV, RMC, GSA, GGA, GLL ..etc 
