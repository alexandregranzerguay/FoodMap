import requests
import json

url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

querystring = {"Subscription-Key":"208ff17014d542d9aa453b82e172ec9c","Content-Type":"application/json"}

payload = " {\r\n     \"documents\": [\r\n         {\r\n             \"language\": \"en\",\r\n             \"id\": \"1\",\r\n             \"text\": \"the food was alright at this restaurant\"\r\n         },\r\n         {\r\n             \"language\": \"en\",\r\n             \"id\": \"2\",\r\n             \"text\": \"Final document\"\r\n         },\r\n         {\r\n             \"language\": \"en\",\r\n             \"id\": \"3\",\r\n             \"text\": \"Final document\"\r\n         },\r\n         {\r\n             \"language\": \"en\",\r\n             \"id\": \"4\",\r\n             \"text\": \"Final document\"\r\n         },\r\n         {\r\n             \"language\": \"en\",\r\n             \"id\": \"5\",\r\n             \"text\": \"Final document\"\r\n         }\r\n     ]\r\n }"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "537d56b3-44de-0032-1e7a-24090d541050"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
res = json.loads(response.text)

print(response.text)