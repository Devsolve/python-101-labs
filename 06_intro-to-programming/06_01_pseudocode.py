# Your cat just had kittens! Now you want to put up an ad to give them
# to your friends. You'll need to save all names of the kittens,
# confirm that they each of them is cute, and show a message that
# that kitten is ready for adoption.
#
# Break this task up into a couple of steps of pseudocode
# and write the pseudocode below in code comments.
# You don't need to write any functional code, just map out the steps.

# Step 1: Initialize a list to store all the kitten name
kittens = []

#  Step 2: Take user input of kitten name from your friend and add to the list
kittens = list(input("enter kitten name: ").split(" "))

# Step 3: Check all kitten are cute.
for ktn in kittens:
     is_cute = True
     
# Step 4: Show a message, that each kitten are cute and ready for adoption
for kttn in kittens:
     if is_cute:
          print(f"{kttn} is ready for adoption")