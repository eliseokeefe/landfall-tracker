# landfall-tracker

This is a landfall tracker that tracks all landfalls occuring in Florida since 1900. Once storms in Florida that have created landfalls are determined, it outputs the date of the landfall, the name of the storm, and the max wind speed for each event. 

The data are from NOAA Best Track Data (HURDAT2) and the raw data can be found in hurdat2.txt.

# debugging & coding logic 

First I started debugging after I cleaned the data of whitespace and saved all the variables. I tried printing and checked if everything printed correctly, and once it did, I moved onto the next step.

Second I created a method to convert the string coordinates to floats. I checked a few different sample coordinates to ensure the negatives worked properly, and once it did, I moved on.

Third I debugged after I wrote the method to determine if the storm was in Florida. I used coordinates from https://map.motivasi.my.id/ to determine what would define Florida. I stored these results as booleans because I wanted to use them later to determine if a landfall occurred. I checked for the length of records and then created a Florida counter to see how many were from florida. I got: 
"Total: 55605
Florida:  2636"

After this, I created a method to check if a landfall occurred. I found a definition of a landfall on https://scienceinsights.org/what-is-a-landfall/ that said a landfall occurs when a storm moves from water to land. Therefore, in order to check if a landfall occurred, I knew I wanted to loop through records to see for each row, if its in_florida value is the same as the previous. If the previous row was False and the current row is True, that meant there was a landfall. During this method, I also had to make sure the two values I was comparing were from the same storm. 

When I ran this method, I got 370 landfalls. I then filtered out the data before 1900, which gave me 274. I checked this by the following code:

florida_landfalls = is_landfall()
print("Number of landfall events:", len(florida_landfalls))
for l in florida_landfalls:
    print(l)


# Optimization 

I first created the method for the specific data for 1900 and after in florida, and although I did store the "in florida" variable in the record, I still believe this was the optimal way to do this to allow the application to be expanded in the future. The reason for this is because even though the Florida variable may not be used for future methods, it does not add time complexity to have it in the record, and someone can simply not use this variable and it would not take longer to execute. Additionally, making this all one method allows for future methods to be added with other functions and not have the record data itself affected (as the logic that builds that record is in a separate method). 

I needed to decide how to remove values before 01/01/1900. I wanted to still store these, as this would allow this application to be versatile if someone did want to create another method that included these values. Therefore, I wanted to figure out a way to not include these in the landfall method I created for this prompt without dropping them from the record permanently. However, I found that I would have to use time to filter this nonetheless in order to determine if something was a landfall (O(n) time, and adding another check is O(1)), and since I did want to include all the data given by NOAA in my overall record, it was better to do this in the if statement within my prompt specific method than remove anything from before 1900 from the record. This allows the application to have access to the data available and have different methods created based on need in the future. 

# Assumptions

1. Bounding 
I created a box that covers ocean waters off of Florida's coast (Atlantic and Gulf Straits) as well as land. So a storm may slightly come out/inside of the box I created, but never actually crossing onto the land. These slight movements count in my method. I could not find a solid definition for how many landfalls occurred in Florida because different sources define landfall and NOAA has expressed that they are still studying these events, making a reference count change over time as data continues to be explored. 

2. Including hurricanes or not 
The bolded prompt says to identify all hurricanes that have made landfalls, but then the below texts says to identify storms that have made a landfall. Since storms is an overarching term, I opted to include more data in the final answer as this may be more helpful, but have the logic in how to make this application only track hurricanes if needed: 

Line 69: if...and (records[i]["status"] == "HU"): 

Changing this one line results in 97 landfalls rather than 274 without the filter. 

3. Max Wind
I am reporting the max wind during the landfall, because the instructions say "during the event". To me, the event is the landfall, because that is what I am mainly reporting on. I decided to grab the wind value (which was already recorded as the maximum during that record) when the water to land transition is detected, since that is when the landfall is actually occurring (the record marking the landfall). If I had looked at the max value at any other point in the storm's occurrence, I would not be looking at just the speed during the landfall event. 

4. Not using built in L indicator 
Since the assignment details said to try not use this, I did not use this, although I understand time complexity wise it would be quicker to use it. 

5. Counting multiple landfalls per storm 
I was unsure if I should count multiple landfalls per storm separately, but since the instructions never said to combine landfalls per storm, and each event is a separate landfall, I decided not to do this. Therefore, one storm can cause multiple landfalls, which is logical based on the context

6. Where to cut off the date
I did not know if I should include storms that started before 1900 and caused a landfall in the 1900s. I decided to include this because it asked for the landfalls to occur since 1900, not for the storm to occur since 1900. 

7. Unnamed storms 
Storms did not always have names (https://rainyseason.info/when-did-names-for-tropical-storms-begin-to-appear.html) therefore some storms are unnamed, but this is not a coding error. Rather there are no name available for those storms.

8. Loading data onto user interface
I opted to have the user run parser.py before the user interface. This is because I want the page to update automatically every time parser.py is ran, therefore allowing it to be built upon with future data. 

# How to run application 
1. Install python on your IDE 
2. Ensure hurdat2.txt is present in repository. If not, please use NOAA Best Track Data (HURDAT2) online data or contact me to fix this error. 
3. In terminal, run parser.py for updated results 
4. In terminal, run python -m http.server 8000
5. In broswer, go to http://localhost:8000/interface.html

