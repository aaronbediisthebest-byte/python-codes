temperature=int(input("enter todays temperature in celcius:  "))
if temperature < 20: 
    outfit="jacket"
    print("it is cold today")
    print("wear a",outfit)
else:
    outfit="t-shirt"
    print("it is warm today.")
    print("wear a",outfit)

is_raining=input("is it raining today?  (yes/no):  ")
if is_raining=="yes":
    print("bring an umbrella!")

wind_speed=int(input("enter the wind speed in km/h:  "))
if wind_speed > 100:
    print("it is too windy,stay inside!")
else:
    ("it is a calm day,have an icecream outside!")