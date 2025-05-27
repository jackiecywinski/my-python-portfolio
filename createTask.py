activityList = ["picnic", "hike", "swim", "bake", "movie", "cook", "bike", "workout",
                "read", "paint", "garden", "party"] #List of activities
locationList = ["out","out","out", "in", "in", "in","out", "in",
                "in", "in", "out", "out"] #Identifies activities as "indoor" or "outdoor"
#outLinks provides a list of image addresses for outdoor activities
outLinks = ["https://i.pinimg.com/736x/8e/2c/b5/8e2cb53fd8979537f629c810b5f6f047.jpg", #Link to picnic image
"https://i.pinimg.com/736x/ae/f9/d9/aef9d9bbd1057abd60bdcc4df9a7d22a.jpg", #Link to hiking image
"https://i.pinimg.com/736x/4f/5a/2f/4f5a2feb5a3f9ead8b90c3fc6f415d60.jpg", #Link to swimming image
"https://i.pinimg.com/474x/c2/9f/49/c29f4940aa4b85d02f9750164c3c3f4a.jpg", #Link to biking image
"https://i.pinimg.com/474x/f0/db/b2/f0dbb20273bf053363c56d0fd8288e2f.jpg", #Link to gardening image
"https://i.pinimg.com/474x/56/f4/83/56f48345727fc3e995366a90476ad832.jpg"]#Link to party image

#inLinks provides a list of image addresses for indoor activities
inLinks =["https://i.pinimg.com/736x/4a/fa/27/4afa27a31d020236e578f0577ca3604c.jpg", #Link to baking image
"https://i.pinimg.com/736x/28/1c/63/281c638e6dcd9013ee2bd0e1d6e72dea.jpg", #Link to movie image
"https://i.pinimg.com/474x/80/69/50/80695082235befff0671611c23252298.jpg", #Link to cooking image
"https://i.pinimg.com/474x/c7/aa/95/c7aa95a8eefdab0f2852072ddf21e3b6.jpg", #Link to workout image
"https://i.pinimg.com/474x/79/d4/35/79d435a09d320d6428e786b724f88816.jpg", #Link to reading image
"https://i.pinimg.com/474x/32/0c/fe/320cfe2cf8544d864ce50764f108b3a8.jpg"] #Link to painting image
filteredList = [] #Activities from activityList are added to this empty list when filtered

from PIL import Image
import requests
from io import BytesIO
import random #loads in the random module

def open_image(url): #A function we learned in class that opens an image based on image address
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img.show()
def activity_reccomendation(location): #the function to run the entire game, includes a parameter
        print("Hello!! Welcome to your activity planner :) I'll give you an activity recommendation for the day!")
        while True: #runs function forever until broken
                if location == "out": #code that recommends outdoor activities to the user
                        for i in range(len(locationList)):
                                if location == locationList[i]:
                                        filteredList.append(activityList[i])
                        print(filteredList)
                        print("Would you like to receive a specific recommendation?")
                        response = input("Yes (Y) or No (N)")
                        if response == "Y":
                                recommendation = random.randint(0,5) #selects an outdoor activity from 6 options
                                if recommendation == 0:
                                        open_image(outLinks[0])
                                        print("Since it's a beautiful day, you should go out on a picnic!")
                                if recommendation == 1:
                                        open_image(outLinks[1])
                                        print("Feeling adventurous today? Go out on a hike!")
                                if recommendation == 2:
                                        open_image(outLinks[2])
                                        print("The water beautiful today, go to the beach!")
                                if recommendation == 3:
                                        open_image(outLinks[3])
                                        print("Take a bike ride to enjoy the beautiful weather!")
                                if recommendation == 4:
                                        open_image(outLinks[4])
                                        print("Take care of your yard and get in touch with nature :)")
                                if recommendation == 5:
                                        open_image(outLinks[5])
                                        print("Have fun with your friends!! Go out to a party!!!")
                        if response == "N": #ends the code if the user does not want a specific recommendation
                                print("Bye! Thanks for playing :)")
                                break
                if location == "in": #code that recommends indoor activities to the user
                        for i in range(len(locationList)):
                                if location == locationList[i]:
                                        filteredList.append(activityList[i])
                        print(filteredList)
                        print("Would you like to receive a specific recommendation?")
                        response = input("Yes (Y) or No (N)")
                        if response == "Y":
                                recommendation = random.randint(0,5) #selects an indoor activity from 6 options
                                if recommendation == 0:
                                        open_image(inLinks[0])
                                        print("Bake a delicious sweet treat to enjoy with friends!")
                                if recommendation == 1:
                                        open_image(inLinks[1])
                                        print("Take a chill pill, watch a movie that's on your list!")
                                if recommendation == 2:
                                        open_image(inLinks[2])
                                        print("Feeling hungry? Cook yourself a gourmet meal!")
                                if recommendation == 3:
                                        open_image(inLinks[3])
                                        print("Get some exercise today! You won't regret it ;)")
                                if recommendation == 4:
                                        open_image(inLinks[4])
                                        print("Read the book you've been meaning to read!")
                                if recommendation == 5:
                                        open_image(inLinks[5])
                                        print("If you feel a wave of creativity, try painting!")
                        if response == "N": #ends the code if the user does not want a specific recommendation
                                print("Bye! Thanks for playing :)")
                                break
activity_reccomendation(input("Would you like to stay indoor (in) or go out (out)?"))#calls activity generator function

#Sources of Images
#Picnic Image: Pinterest, Elsie Notaras, https://www.pinterest.com/pin/592223419788285989/

#Hiking Image: Pinterest, anggeventure, https://www.pinterest.com/pin/592223419788285996/

#Swimming Image: Pinterest, Maislin, https://www.pinterest.com/pin/592223419788285999/

#Biking Image: Pinterest, Pinterest, https://www.pinterest.com/pin/592223419788286162/

#Gardening Image: Pinterest, Lili Merkushev, https://www.pinterest.com/pin/592223419788286207/

#Partying Image: Pinterest, al!ce, https://www.pinterest.com/pin/592223419788286260/

#Baking Image: Pinterest, maya !, https://www.pinterest.com/pin/592223419788286032/

#Movie Image: Pinterest, kimberly, https://www.pinterest.com/pin/592223419788286045/

#Cooking Image: Pinterest, Emma, https://www.pinterest.com/pin/592223419788286068/

#Workout Image: Pinterest, Abby Jones, https://www.pinterest.com/pin/592223419788286093/

#Reading Image: Pinterest, charliecat_, https://www.pinterest.com/pin/592223419788286175/

#Painting Image: Pinterest, eli, https://www.pinterest.com/pin/592223419788286114/
