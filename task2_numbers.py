#1.formate function
def format_number(number, character):
    return "{0:{1}}".format(number, character)

result = format_number(145, 'o')
print(result) #output:-221

#2.pond and water 
radius= 84
pi=3.14
circle_area= pi * radius ** 2
water= circle_area**1.4

print(circle_area)
print(int(water))

#3.calculate speed
distance=490
time=7*60
speed= distance/time 

print(int(speed))




