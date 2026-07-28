# landfall-tracker

This is a landfall tracker that tracks all landfalls caused by Hurricanes in Florida since 1900. Once hurricanes in Florida that have created landfalls are determined, it outputs the date of the landfall, the name of the Hurricane, and the max wind speed for each event. 

The data are from e NOAA Best Track Data (HURDAT2) 

# debugging 

First I started debugging after I cleaned the data and saved all the variables. I tried printing and checked if everything printed correctly.

Second I debugged after I casted the cordinates as floats. I checked a few different sample cordinates to ensure the negatives worked properly.

Third I debugged after I wrote the florida method. I checked for the length of records and then created a florida counter to see how many were from florida. I got: 
Total: 55605
Florida:  2636
Which was logically in sound with the data I was given 

# coding logic 

I first cleaned the data. I then stored variables based on the format I found on the NOAA website. I then created a record to hold all of these values. Then I created the method to change the cordinates to the float format. Then I created the method to see if the location was in Florida using information from https://map.motivasi.my.id/. 

After the inital data storage, I began to check whether or not the storm created a landfall. I wanted to make sure I did not use the landfall indicator. From https://scienceinsights.org/what-is-a-landfall/, I found that a landfall is defined by when a storm moves over land after being over water. Therefore, in order to check if a landfall occured, I knew I wanted to loop through records to see for each row, if its in_florida value is the same as the previous. If the previous row was False and the current row is True, that meant there was a landfall. During this method, I also had to make sure the two values I was comparing were from the same storm. 

When I ran this method, I got 370 landfalls. This seemed higher than the numbers I was finding online, so I wanted to consider my logic here. I realized I had not checked if the events were actually hurricanes, so I added that to the if statement and got 146, which is close to the numbers I found online (120+). I then filtered out the data before 1900, which gave me 97, and based on my research this is a realistic number 

# Optimization 

At first, I wanted to filter out everything that was not a hurricane before looping. However, in this context, this could remove important data where the previous value was not yet a hurricane but the current value was. This would count as a hurricane landfall, but would not show up with my current logic. Therefore, I kept it there. 

I then needed to decide how to remove values before 01/01/1900. I wanted to still store these, as this would allow this application to be versitle if someone did want to create another method that included these values. Therefore, I wanted to figure out a way to not include these in the landfall method I created for this prompt without dropping them from the record permantly. However, I found that I would have to use time to filter this nonetheless, and since I did not want to not include them in my overall record, it was better to do this in the if statement than remove them from the record. This allows the application to have access to the data avaliable and have different methods created based on need. 

# Assumptions

1. Bounding 
I created a box that covers ocean waters off of Florida's coast (Atlantic and Gulf Straits) as well as land. So a storm may slightly come out/inside of the box I created, but never actually crossing onto the land. These slight movements count in my method.

