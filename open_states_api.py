# import json, requests

#####################################################
###Problem 1
#####################################################

###Use the following documentation to identify url
###https://sunlightlabs.github.io/openstates-api/legislators.html#examples/legislator-detail

# url = 'http://openstates.org/api/v1/legislators/?state=mo&active=true'

# r = requests.get(url)

# legislators = json.loads(r.content)

# full_names = [record['full_name'] for record in legislators]

# print full_names

#####################################################
###Problem 2
#####################################################

###Use the followig documentation to identify url for problem 2
###https://sunlightlabs.github.io/openstates-api/bills.html#bill-fields

# url = 'http://openstates.org/api/v1/bills/?state=mo&chamber=upper&search_window=session'

# r = requests.get(url)

# bills_introduced = json.loads(r.content)

# print bills_introduced

###Or, if you only want to print the id...

# bill_id = [record['bill_id'] for record in bills_introduced]

# print bill_id

#####################################################
###Problem 3
#####################################################

# subjects_bills_introduced = [record['subjects'] for record in bills_introduced]

# ###There are no subjects for the bills listed in Problem 2
# ###Modified search to include bills from both house and senate as lower chamber appears to record subject

# url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session&subject=Health'

# r = requests.get(url)

# bills_introduced_subject = json.loads(r.content)

# print bills_introduced_subject

# ###Or, if you only want to print the id...

# bill_id = [record['bill_id'] for record in bills_introduced_subject]

# print bill_id

#####################################################
###Problem 4
#####################################################

import json, requests

url = 'http://openstates.org/api/v1/bills/?state=mo&search_window=session&subject=Health'
r = requests.get(url)
bills_introduced_subject = json.loads(r.content)

title = [record['title'] for record in bills_introduced_subject]
bill_id = [record['bill_id'] for record in bills_introduced_subject]

last_action = []
for x in bill_id:
	url = 'http://openstates.org/api/v1/bills/mo/2016/' + x + '/'
	r = requests.get(url)
	bill_details = json.loads(r.content)
	bill_actions = bill_details['actions']
	last_action.append(bill_actions[len(bill_actions)-1]['action'])

id_action = zip(bill_id, last_action)
###Or, if you want title, change bill_id to title in above code

print 'Id and Last Action Taken for Bills Related to Health'
for x in id_action:
	print x[0] + '		' + x[1]

















