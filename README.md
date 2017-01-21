# FoodMap

Our team noticed a problem with the way restaurants are discovered online. Typically, numeric ratings are just arbitrary numbers (what does a 4 out of 5 really mean??), and there are way too many text reviews to read them all. So our question was: how can we more intelligently compare restaurants to one another, and give restaurant-goers more meaningful numeric ratings?

### Our solution
First, we pull a list of restaurants from Google Places within a given radius (in Montreal, of course). We then pull all their text reviews from Google. There are a variety of experiences people write about (good service, bad service, tasty food, undercooked food, etc.). We feed all these reviews into Microsoft Cognitive Services' Text Analytics API hosted on Azure. This API provides a numerical rating of the sentiment of the text between 0 and 1 (higher means a more positive experience, negative means lower). We then map these restaurants with emphasis on most positive experiences.
