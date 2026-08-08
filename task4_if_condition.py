# 1. Write a program to determine the BMI Category based on user input.
height = int(input("Enter height in meter:"))
weight= int(input("Enter weight in kilograms:"))
BMI= weight/(height)*2
print(BMI)

if BMI >=30:
    print("Obesity")
elif BMI >= 25:
    print("Overweight")
elif BMI >= 18.5:
    print("Normal")
else:
    print("Underweight") 

#2.Write a program to determine which country a city belongs to
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in Australia:
    print(city, "is in Australia")
elif city in UAE:
    print(city, "is in UAE")
elif city in India:
    print(city, "is in India")
else:
    print("City not found")


#3.  Write a program to check if two cities belong to the same country  
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

elif city1 in India and city2 in India:
    print("Both cities are in India")

else:
    print("They don't belong to the same country")