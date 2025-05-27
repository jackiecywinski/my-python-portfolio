#Jackie Cywinski
#2/24/2025
#Images


#Init
from PIL import Image
import requests
from io import BytesIO
import random

#Allows me to open the images in the vacationOptions function
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#List of vacation options
vacationList = ["https://tinyurl.com/5dhbmmw7", #Italy
"https://tinyurl.com/yhynahp4", #London
"https://tinyurl.com/ywb3rbpy", #Costa Rica
"https://tinyurl.com/hj52wben", #Wyoming
"https://tinyurl.com/mry2w39w"] #Oregon


#Function for vacation suggestions
def vacationOptions():
    while True:
        print("Welcome to your vacation planning assistant!")
        print("Would you like vacation reccomendations?")
        answer = input("Yes (Y) or No (N)")
        if answer == "Y":
            randomVacation = random.randint(0,4)
            if randomVacation == 0:
                open_image(vacationList[0])
                print("You should visit Italy! There are many beautiful historical monuments to explore and excellent food to eat.")
            if randomVacation == 1:
                open_image(vacationList[1])
                print("For abroad city exploration, I suggest you visit London! London's architecture is stunning, and the city life will keep you busy and moving forever!")
            if randomVacation == 2:
                open_image(vacationList[2])
                print("You should visit Costa Rica! Costa Rica's beaches are beautiful, warm, and sunny; perfect for a relaxing getaway!")
            if randomVacation == 3:
                open_image(vacationList[3])
                print("I suggest you visit Wyoming! Wyoming's hikes are gorgeous, housing the popular National Park, Yellowstone.")
            if randomVacation == 4:
                open_image(vacationList[4])
                print("For beautiful views of the Pacific Northwest, you should visit Oregon! Oregon's hikes are very stunning and private, with wildflowers, greenery, and a beautiful view of the ocean.")

        if answer == "N":
            print("Okay, bye!")
            break


#Main
vacationOptions()

#SOURCES
#The picture of Italy. Image source: Cosmos. Italy's Best. Accessed via https://www.cosmos.com/tour/italys-best/6390/?season=2025
#The picture of London. Image source: Visit London. London Accomodations: Where to Stay. Accessed via https://www.visitlondon.com/where-to-stay
#The picture of Costa Rica. Image source: Afar. Jessie Beck. 2023. 17 Beautiful Beaches in Costa Rica—and Where to Stay Once You’re There. Accessed via https://www.afar.com/magazine/best-beaches-in-costa-rica
#The picture of Wyoming. Image source: Sierra Club. Greater Yellowstone- Northern Rockies. Accessed via https://www.sierraclub.org/land-conservation/greater-yellowstone-northern-rockies
#The picture of Oregon. Image source: Visit the USA. Oregon Coast: Open to Everyone. Accessed via https://www.visittheusa.com/experience/oregon-coast-open-everyone
