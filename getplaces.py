import requests
import json
import time
with open("gkey") as f:
	apikey=f.readlines()[0]
with open("ckey") as f:
	cogapikey=f.readlines()[0]
	
print apikey
locationCentre = "45.4581,-73.6403" # where you are...
# apikey = raw_input("enter google api key: ")
# cogapikey = raw_input("enter Microsoft cognitive api key:")


def getScores(review_txt1, review_txt2, review_txt3):
	url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"
	
	querystring = {"Subscription-Key":cogapikey,"Content-Type":"application/json"}
	
	payload = {}
	payload['documents'] = []
	payload['documents'].append({"language": "en","id": "1","text": review_txt1})
	payload['documents'].append({"language": "en","id": "2","text": review_txt2})
	payload['documents'].append({"language": "en","id": "3","text": review_txt3})
	print payload
	headers = {
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "537d56b3-44de-0032-1e7a-24090d541050"
	    }
	
	
	response = requests.request("POST", url, data=json.dumps(payload), headers=headers, params=querystring)
	res = json.loads(response.text)
	
	count = 0
	score = 0
	print res
	print payload
	for index in res['documents']:
		score += index['score']
		count += 1
	print score/count
	
	# print(response.text)
	return

def getReviews(place_id):
	url = "https://maps.googleapis.com/maps/api/place/details/json"

	querystring = {"key":apikey,"placeid":place_id}

	response = requests.request("GET", url, params=querystring)
	res = json.loads(response.text)

	if ('reviews' in res['result']):
		for review in res['result']['reviews']:
			print review['text']
		if len(res['result']['reviews'])==3:
			getScores(res['result']['reviews'][0]['text'],res['result']['reviews'][1]['text'],res['result']['reviews'][2]['text'])
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



