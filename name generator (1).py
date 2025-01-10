#Jackie Cywinski
#10/17/2024
#Name Generator

#this code tells you what your color is based on the answers you choose
print("Welcome To Choose Your Color!")
print("Answer these questions to find out what color matches your personality.")

ans=input("winter (w) or summer (s)?") #first question
if ans=="w": #determines their color is at the bottom of the rainbow
    ans=input("adventurer(a) or homebody(h)?")
    if ans=="a": #determines their color is an Earth color
        ans=input("forest (f) or ocean(o)?")
        if ans=="f": #determines their color is green
            print("Your color is green!")
        else: #determines their color is blue
            print("Your color is blue!")
    if ans=="h":#determines their color is dark
        ans=input("movies (m) or books(b)?")
        if ans=="m": #determines their color is purple
            print("Your color is purple!")
        else: #determines their color is black
            print("Your color is black!")
if ans=="s": #determines their color is at the top of the rainbow
    ans=input("sunrise(rise) or sunset(set)?")
    if ans=="rise": #determines their color is summery
        ans=input("sunflower (s) or carnation(c)?")
        if ans=="s": #determines their color is yellow
            print("Your color is yellow!")
        else: #determines their color is pink
            print("Your color is pink!")
    if ans=="set": #determines their color is firey
        ans=input("roses (r) or marigolds(m)?")
        if ans=="m": #determines their color is orange
            print("Your color is orange!")
        else: #determines their color is red
            print("Your color is red!")
