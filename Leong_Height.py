# FINAL DRAFT VERSION 2 - Josh Leong CS 1030

user_feet = str(input("What is your height starting with Feet? "))
if user_feet == "":
    exit()
elif user_feet.isnumeric():
    print("Thank you for the correct number format of how tall a person may be in feet.")
else:
    print("That was not number we can use to calculate height. Try Again")

user_inches = str(input("How many additional inches tall are you? "))
if user_inches == "":
    exit()
elif user_inches.isnumeric():
    print("Thank you for the correct number format of inches tall you are.")
else:
    print("That was not number we can use to calculate height. Try Again")
    exit()
validated_user_feet = float(user_feet)
validated_user_inches = float(user_inches)
if validated_user_feet < 0:
    print("Sorry cannot have a negative number as height")
elif validated_user_feet == 0:
    print("Sorry you can't be zero feet tall, unless you just had an anvil dropped on you.")
else:
    print("Awesome! Your height in feet input has been accepted, we can now do some calculations properly!")
if validated_user_inches < 0:
    print("Sorry cannot have a negative number as height")
else:
    print("Awesome! Your height in inches has been accepted, we can now do some calculations properly!")
print("Calculating measurement conversions...")

converted_feet = validated_user_feet * 12
height_in_inches = converted_feet + validated_user_inches
# print("You are", height_in_inches, "total inches tall")
if height_in_inches >= 96:
    print("Wow you are really tall!")

converted_cm = height_in_inches * 2.54
converted_to_meters = converted_cm / 100
rounded_total = round(converted_to_meters, 2)
print("To recap, you are:", user_feet, "feet and", user_inches, "inches tall.")
print("Which makes you:", rounded_total, "meters tall.")
exit()
