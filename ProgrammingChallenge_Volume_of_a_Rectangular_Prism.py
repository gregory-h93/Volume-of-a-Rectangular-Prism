# For this programming challenge, you will be creating a function that calculates the volume of a
# rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is V = l * w * h
# where l, w, and h are length, width, and height, respectively

# 1. First, create three variables representing length, width, and height.
# Assign each of them an integer as user input using the input() function and int().
length = int(input("Enter an integer for length: "))
width = int(input("Enter an integer for width: "))
height = int(input("Enter an integer for height: "))

# 2. Next, create a function to calculate the volume of the rectangular prism.
# It should have 3 parameters representing length, width, and height and return
# the volume of a rectangular prism calculated using those 3 parameters.
def volume_of_prism(l, w, h):
    return l * w * h


# 3. Finally, use print() to display "The volume of the rectangular prism is
# [call function  here to calculate volume] cubic feet." in the output.
# You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.
print("The volume of the rectangular prism is " + str(volume_of_prism(length, width, height)) + " cubic feet.")