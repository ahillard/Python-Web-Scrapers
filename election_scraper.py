import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser() 
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx') 

br.select_form(nr=0) 
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566'] 
br.submit('ctl00$MainContent$btnElectionType') 

br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

html = br.response().read() 

########## YOUR CODE HERE ##########

soup = BeautifulSoup(html, "html.parser") #Create Beautiful Soup Object

primary_table = soup.find('table', {'id':'MainContent_dgrdCountyRaceResults'})
rows = primary_table.find_all('tr')

#Create a CSV File that is Writable 
outfile = open('election_scraper.csv', 'w')
writer = csv.writer(outfile)

#Write Header into CSV File
header = [cell.text for cell in rows[0].find_all('th')]
writer.writerow(header)

#Write Data into CSV File
for row in rows[2:len(rows)]:
 	data = [cell.text for cell in row.find_all('td')]
	writer.writerow(data)









