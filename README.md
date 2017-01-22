# ConUHacks II - January 21-22, 2017

Our team noticed a problem with the way restaurants are discovered online. Typically, numeric ratings are just arbitrary numbers (what does a 4 out of 5 really mean??), and there are way too many text reviews to read everything and make an informed decision. So our question was: how can we more intelligently compare restaurants to one another, and give restaurant-goers more meaningful numeric ratings?

### Our solution
First, we pull a list of restaurants from Google Places within a given radius (in Montreal, of course). We then pull all their text reviews from Google. There are a variety of experiences people write about (good service, bad service, tasty food, undercooked food, etc.). We feed all these reviews into Microsoft Cognitive Services' Text Analytics API hosted on Azure. This API uses machine learning, classification and natural language processing to provide a numerical rating of the sentiment of the text between 0 and 1 (higher means a more positive experience, negative means lower). We then display these restaurants to the user, with emphasis on the most positive experiences.

All of the processing of the data is done with Python and stored in a sqlite database, which gets put into use with a google-mapping Flask app.

![screenshot](https://github.com/AwesomeTEAMCONU/FoodMap/blob/master/screenshot.png)
A screenshot of our app, with analyzed restaurants centred in a 2km radius around Concordia University. Red is 0-35% positive sentiment, orange is 35-60%, yellow is 60-80%, and green is above 80%.
