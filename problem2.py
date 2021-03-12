##Name:        problem2.py
##Purpose:    The purpose is to calculate whether or not you can form a triangle based on 3 given lines

##Author:    Koukoulidis.None

##Created:    date in 23/02/2021


#ask the user for the side lengths

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

#find if the lines given make a triangle

if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2 :
  print("Your shape is a triangle")

else :
  print("Your shape is not a triangle")