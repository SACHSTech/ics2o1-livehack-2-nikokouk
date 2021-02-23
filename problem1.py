##Name:        problem2.py
##Purpose:    The purpose is to find whether or not The user is speeding and how much of a fine they need to pay based off of their speed.

##Author:    Koukoulidis.None

##Created:    date in 23/02/2021

#ask for user inout

speed_limit = float(input("input the speed limit?: "))
driver_speed = float(input("How fast were you going?"))

# Calculate how high over the speed limit

speed_over = driver_speed - speed_limit


# compute the users fine

if speed_over >= 31 : 
  print("You are speeding and your fine is $570. ")

elif speed_over >= 21 and speed_over <= 30 :
  print("You are speeding and your fine is $270. ")

elif speed_over >= 1 and speed_over <= 20:
  print("You are speeding and your fine is $100")

else  :
  print("Congratulations, you are within the speed limit!")