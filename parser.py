records = [] #creates empty record to eventually store cleaned data 
landfalls = [] #creates empty record to eventually store all landfall events  

def simplify_cords(coordinate):
   direction = coordinate[-1] #checks the last character to see which direction the cordinate is in (N, S, W, E)
   val = float(coordinate[:-1]) #grabs the number (not the direction) to change it from string to double 
   if (direction == "S") or (direction == "W"): #makes negative if its south or west 
      val = -val 
   return val  #returns number version of coordinates 

def is_florida(lat, long): 
   #utilizes definition of florida's longitude and latitude to check if a hurricane was in florida 
   if(lat >= 24.5 and lat <= 31.0) and (long <= -79.0 and long >= -87.0):
      return True
   else: 
      return False 

#Open the data in python in read mode 
with open("hurdat2.txt", "r") as hurricanedata: 
    for i, line in enumerate(hurricanedata): #loop goes through dataset
       clean = line.strip() #removes outer whietespace 
       fields = clean.split(",") #provides list of fields 
       field = fields[0].strip() #grabs the first element to check on below criteria
    
       if(field.isdigit() and len(field) == 8): #checks if this line is a header or data. Storm IDs have letters 
        #grabs data specific variables & stores them 
        date = fields[0].strip()
        time = fields[1].strip()
        storm_indicator = fields[2].strip() #not using since I am avoiding the landfall indicator variable
        status = fields[3].strip()
        latitude = fields[4].strip()
        latitude = simplify_cords(latitude) #calls method above to change cordinates to numbers rather than strings 
        longitude = fields[5].strip()
        longitude = simplify_cords(longitude)
        max_wind = fields[6].strip()
        in_florida = is_florida(latitude, longitude)

        #fills the previously defined record with clean hurricane data 

        r = {
           "storm_id": current_storm_id, 
           "storm_name": current_storm_name, 
           "date": date, 
           "status": status,
           "latitude": latitude, 
           "longitude": longitude, 
           "max_wind": max_wind,
           "in_florida": in_florida
        }
        records.append(r)

       else: #grabs header specific variables & stores them 
         current_storm_id = fields[0].strip()
         current_storm_name = fields[1].strip()

#using the defintion of a landfall being a storm moving from water to land, check if the previous location is in the water (in_florida = false) and the current location is on land (in_florida = true)
def is_landfall(): 
    for i in range(len(records)): 
            if i == 0: #avoids indexing to -1 
                continue 
            cur_storm = records[i]["storm_id"] #grab current storm ID
            prev_storm = records[i-1]["storm_id"] #grab previous storm ID
            prev_val = records[i-1]["in_florida"] #grab previous storm's in_florida boolean 
            cur_val = records[i]["in_florida"] #grab current storm's in_florida boolean 

            #check if the previous value and current value are the same storm. Then check if the previous storm value was not in Florida but the current storm value is. Also checks if the storm occured during or after 1900
            if(cur_storm == prev_storm) and (prev_val == False) and (cur_val == True) and (int(records[i]["date"]) >= 19000101): 
                #if the above criteria is true, it was a landfall. store that value into the landfall record created at the top
                l = {
                    "storm_id": records[i]["storm_id"], 
                    "storm_name": records[i]["storm_name"],
                    "date" : records[i]["date"], 
                    "max_wind" : records[i]["max_wind"]
                    }
                landfalls.append(l)
    #once the entire record has been looped through, return the landfall events 
    return landfalls 




        





        
    