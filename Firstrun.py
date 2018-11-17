import requests
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "264e6838c8fe4b49bdb2c67419594476"
assert subscription_key

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

analyze_url = vision_base_url + "analyze"

# Set image_path to the local path of an image that you want to analyze.
image_path = input("Enter image path ")


# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers    = {'Ocp-Apim-Subscription-Key': subscription_key,
              'Content-Type': 'application/octet-stream'}
params     = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
#print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)


if "hot dog" in image_caption: print("No nut november")
if "hot dog" in image_caption: print("#NYhotdogs #IloveHotDog #HD4Life!")
if "sandwich" in image_caption: print("#AmericanLifestyle #Burgers4Life #I<3Burgers")
if "pizza" in image_caption: print("#ItlianCulture #FeelingItalian #Pizza4Life #PizzaTime!")
if "hamburger" in image_caption: print("#AmericanLifestyle #Hamburgers4Life #I<3Hamburgers")
if "sushi" in image_caption: print("#FeelingJapanese? #RawFish #SushiYum #Makirolls")
if "fajita" in image_caption: print("#MiAmore #MexicanTime #Spicy #wrap")
if "tacos" in image_caption: print("#MiAmore #MexicanTime #Spicy")
if "noodles" in image_caption: print("#ChinaOrJapan? #healthyLifestyle #asianSpaghetti")
if "kebab" in image_caption: print("#MiddleEastCulture #KebabYum!")
if "souvlaki" in image_caption: print("#GreekCuisine #Gyros #GreekWrap")
if "steak" in image_caption: print("#BBQ #CookingWithFire #Medium-rareOrWell-Done? #Meatlover #Meat4Life")
if "chicken" in image_caption: print("#Fried #NoMercy #Kokoroko #Spicy #ChickenFingers #Nuggets4Life")
if "fish" in image_caption: print("#SeaLife #ExploringTheSea #Raw #NeverEnough #FeelingFishyToday")
if "lobster" in image_caption: print("#RedKing #CreepyClaws #CheapLobsterNOT #LuxLife")
if "egg" in image_caption: print("#Egg4Life #EggEveryday #Fried #Boiled #Baked?")
if "apple" in image_caption: print("#Fruit #HealhtyLife #Diet #TryingToLoseFat")
if "salad" in image_caption: print("#HealthyNotHealthy #VeganLife #OnDiet #SummerIsComing")
if "coffee" in image_caption: print("#MorningRoutine #NeverHavinEnough #NoSleepToday #WakingUpEarly #HOT")
if "juice" in image_caption: print("#Orange #Lemon #Smoothie #AllAboutTheVitamins #HealthyLife #VeganMoment")
if "chocolate" in image_caption: print("#CheatingDay #CantStop #Everyday #Life #DessertTime")
if "alcohol" in image_caption: print("#EmotionalTimes #PartyTime #Drunk #EverythingSpins #Hangover")