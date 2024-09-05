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

player = int(input("What is our pick?\n1 - Rock\n2 - Paper\n3 - Scissors\n")) - 1

# DO NOT ERASE ROWS ABOVE!
# Build a Rock, Paper, Scissors
