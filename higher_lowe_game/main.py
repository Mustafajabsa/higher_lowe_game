import random
from art import logo, vs
from game_data import data
#function for the infinite game

#print the logo first
print(logo)
#get two random choices from the data
A = random.choice(data)
B = random.choice(data)
A_followers = A['follower_count']
B_followers = B['follower_count']
print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
print(vs)
print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
#taking an input from the user as achoice for the try
user_choice = input("who has more followers? Type 'A' or 'B': ")
score = 0
#while loop to repeat the process as long as the choice was right
while True:
    if user_choice == "A":
        if A_followers > B_followers:
            score +=1
            print(f"You're right! Current score: {score}.")
            A=B
            print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
            print(vs)
            B = random.choice(data)
            print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
            user_choice = input("who has more followers? Type 'A' or 'B': ")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
    elif user_choice == "B":
        if B_followers > A_followers:
            score +=1
            print(f"You're right! Current score: {score}.")
            A=B
            print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
            print(vs)
            B = random.choice(data)
            print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")
            user_choice = input("who has more followers? Type 'A' or 'B': ")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
