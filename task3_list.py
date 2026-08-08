justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]
#1.calculate the member of justice_league
print(len(justice_league))

#2.add new member in list 
justice_league.append("Batgirl")
justice_league.append("Nightwing")


#3.Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

# 4. Put Superman between Aquaman and Flash
justice_league.remove("Superman")
position = justice_league.index("Aquaman")
justice_league.insert(position + 1, "Superman")

# 5. Replace with new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

# 6.Sort the Justice League alphabetically. 
justice_league.sort()

print(justice_league)
print("New Leader:", justice_league[0])
