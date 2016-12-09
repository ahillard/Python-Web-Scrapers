#The following code generates a csv, scatter plot, and heat map, with the crimes of a certain type over a specified range of dates. 
import json, requests, datetime, gmplot, csv, requests


#Create and print dictionary with possible types of crime 
primaryType = {1:'CRIM SEXUAL ASSAULT', 2: 'MOTOR VEHICLE THEFT', 3: 'NARCOTICS', 4:'CRIMINAL DAMAGE', 5:'ROBBERY' , 
6:'DECEPTIVE PRACTICE' , 7:'ASSAULT' , 8:'WEAPONS VIOLATION' , 9:'THEFT' , 10:'BATTERY' , 11:'PUBLIC PEACE VIOLATION',
12:'OTHER OFFENSE',13:'CRIMINAL TRESPASS',14:'GAMBLING',15:'BURGLARY',16:'PROSTITUTION',17:'OFFENSE INVOLVING CHILDREN',
18:'ARSON',19:'HOMICIDE',20:'SEX OFFENSE',21:'INTERFERENCE WITH PUBLIC OFFICER',22:'INTIMIDATION',23:'LIQUOR LAW VIOLATION',
24:'KIDNAPPING',25:'STALKING',26:'OBSCENITY',27:'PUBLIC INDECENCY',28:'OTHER NARCOTIC VIOLATION',29:'CONCEALED CARRY LICENSE VIOLATION',
30:'RITUALISM',31:'NON-CRIMINAL',32:'HUMAN TRAFFICKING',33:'NON - CRIMINAL',34:'NON-CRIMINAL (SUBJECT SPECIFIED)',35:'DOMESTIC VIOLENCE'}

for i in primaryType:
    print primaryType[i] + "  " + str(i)

#Prompt user for crime type
crimeIndex = int(raw_input("Enter the number for the type of crime you want to see:     "))
crimeType = primaryType[crimeIndex]

#Prompt use for date range
print("Between what two dates do you want crime records?")
date1 = raw_input("Please enter Beginning Date using the format YYYY-MM-DD:     ")
date2 = raw_input("Please enter Ending Date using the format YYYY-MM-DD:    ")

#Use Crime API to get the data according to user input 
url = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '" + date1 + "T00:00:00' and '" + date2 + "T23:59:59'&primary_type=" + crimeType
r = requests.get(url)
crimes = json.loads(r.content)

#CSV download 
CSV_URL = "https://data.cityofchicago.org/resource/6zsd-86xi.json?$where=date between '" + date1 + "T00:00:00' and '" + date2 + "T23:59:59'&primary_type=" + crimeType

with requests.Session() as s:
    download = s.get(CSV_URL)

decoded_content = download.content.decode('utf-8')
cr = csv.reader(decoded_content.splitlines(), delimiter=',')

outfile = open('crime_' + crimeType + "_" + date1 + "_" + date2 + ".csv", 'w')
writer = csv.writer(outfile)
writer.writerows(cr)

#Prep Latitude and Longitude for gmplot 
latitudes = [str(x.get('latitude')) for x in crimes]
longitudes = [str(x.get('longitude')) for x in crimes]

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

latitudes = remove_values_from_list(latitudes, 'None')
longitudes = remove_values_from_list(longitudes, 'None')

latitudes = [float(x) for x in latitudes]
longitudes = [float(x) for x in longitudes]

#Create Scatter Plot and Heat Map of Specified Crime over Specified Dates
#https://github.com/vgm64/gmplot/blob/master/README.rst
crimeScatter = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)
crimeScatter.scatter(latitudes, longitudes, '#3B0B39', size=80, marker=False)
crimeScatter.draw("crimeScatter_" + crimeType + "_" + date1 + "_" + date2 + ".html")

crimeHeat = gmplot.GoogleMapPlotter(41.8781, -87.6298, 11)
crimeHeat.heatmap(latitudes, longitudes)
crimeHeat.draw("crimeHeat_" + crimeType + "_" + date1 + "_" + date2 + ".html")









