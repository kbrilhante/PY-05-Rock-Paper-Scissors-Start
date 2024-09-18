import random

picks = ["Rock", "Paper", "Scissors"]
rps = [
r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

# this will return the index of the player's choice (notice the -1)
player = int(input("What is our pick?\n1 - Rock\n2 - Paper\n3 - Scissors\n> ")) - 1

# DO NOT ERASE ROWS ABOVE!
# Build a Rock, Paper, Scissors

# TODO: show the player's choice on screen (tip: you can use the ASCII codes to draw it)
# TODO: get the computer's choice
# TODO: show the computer's choice on screen
# TODO: determine who won the match
# TODO: show the winner on screen