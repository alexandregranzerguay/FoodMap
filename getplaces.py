import requests
import json
import time

locationCentre = "45.4581,-73.6403" # where you are...
apikey = raw_input("enter api key: ")

def getReviews(place_id):
	url = "https://maps.googleapis.com/maps/api/place/details/json"

	querystring = {"key":apikey,"placeid":place_id}

	response = requests.request("GET", url, params=querystring)
	res = json.loads(response.text)

	if ('reviews' in res['result']):
		for review in res['result']['reviews']:
			print review['text']
	return


# retrieve places nearby (narrowed down to restaurants in 1km radius)
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

querystring = {"key":apikey,"location":locationCentre,"radius":"1000","type":"restaurant"}


response = requests.request("GET", url, params=querystring)

res = json.loads(response.text)

# print(res['next_page_token'])

# we have the place. now we have to extract information from the place and send another api request to get the reviews
for restaurant in res['results']:
	print restaurant['name']
	print restaurant['place_id']
	getReviews(restaurant['place_id'])
	print restaurant['geometry']['location']['lat']
	print restaurant['geometry']['location']['lng']

# if there are more pages of results, cycle through repeating requests to the next page
while ('next_page_token' in res):
	time.sleep(2) # wait for next page to become valid

	querystring = {"key":apikey,"location":locationCentre,"radius":"1000","type":"restaurant","pagetoken":res['next_page_token']}

	response = requests.request("GET", url, params=querystring)

	res = json.loads(response.text)

	for restaurant in res['results']:
		print restaurant['name']
		print restaurant['place_id']
		getReviews(restaurant['place_id'])
		print restaurant['geometry']['location']['lat']
		print restaurant['geometry']['location']['lng']

	if ('next_page_token' in res):
		print(res['next_page_token'])



