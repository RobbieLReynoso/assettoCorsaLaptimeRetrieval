import json5 as json
import pandas as pd
from datetime import timedelta, datetime
from pprint import pprint
#function for laptime conversion
def lapConverter(laptime):
    updated = timedelta(milliseconds= int(laptime))
    minutes, seconds = divmod(updated.total_seconds(), 60)
    return f"{int(minutes):02}:{seconds:06.3f}"
    
#open file and store info in dict
with open(r"C:\Users\rreyn\Desktop\python1\ACC\data\240326_221227_FP.json", "r", encoding= 'utf-8') as f:
  json_str = f.read().decode('utf-8').replace('"',"'")
  pprint(json_str)
  json_dict = json.loads(f.read())

#create driver dictionary
driverDict = {}

#create list to store lap information
laps_data = []

#get trackname
trackName = json_dict.get('trackName', '')

#iterate over leaderboard lines
for entry in json_dict['sessionResult']['leaderBoardLines']:
    # Extracting driver details
    driverFirstName = entry['currentDriver']['firstName']
    driverLastName = entry['currentDriver']['lastName']
    driverPlayerId = entry['currentDriver']['playerId']
    carId = entry['car']['carId']
    modelId = entry['car']['carModel']

    #xetract lap information from the 'laps' list and associate them with the carId
    laps = json_dict.get('laps', [])
    for lap in laps:
        if lap['carId'] == carId:
            lap_time = lapConverter(lap['laptime'])
            sector_times = [lapConverter(sector) for sector in lap['splits']]
            is_valid = lap['isValidForBest']
            laps_data.append({
                'Track Name': trackName,
                'Driver First Name': driverFirstName,
                'Driver Last Name': driverLastName,
                'Driver Player ID': driverPlayerId,
                'Car ID': carId,
                'Model ID': modelId,
                'Lap Time': lap_time,
                'S1': sector_times[0],
                'S2': sector_times[1],
                'S3': sector_times[2],
                'Is Valid': is_valid
            })

#create DataFrame from lap data
df = pd.DataFrame(laps_data)

#import metadeta into a dataframe
try:
    metaDF=pd.read_excel('laptimesMeta.xlsx')
    #concat new data with old data
    combinedDF=pd.concat([metaDF, df], ignore_index=True)
except FileNotFoundError:
    combinedDF = df

#xport combined DataFrame to Excel file
combinedDF.to_excel('laptimesMeta.xlsx', index=False)


#export DataFrame to Excel file for ez copy
df.to_excel('laptimesEzCopy.xlsx', index=False)

print("Excel file has been created successfully.")






    
    