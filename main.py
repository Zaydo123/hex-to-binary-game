
import random

def hex_to_bin_game():
    print("Welcome to the Hex to Binary Conversion Game!")
    print("You will be given a hexadecimal number, and you must convert it to binary format (starting with 0b).")
    print("Let's begin!\n")
    
    score = 0
    rounds = 5  # Number of rounds for the game
    
    for i in range(rounds):
        # Generate a random hexadecimal number
        hex_num = hex(random.randint(0, 255))  # Random number between 0 and 255 (1 byte)
        
        print(f"Round {i+1}:")
        print(f"Hexadecimal: {hex_num}")
        
        # Get the correct binary answer
        correct_bin = bin(int(hex_num, 16))
        
        # Ask the user to input the binary conversion
        user_bin = input("Convert the hex to binary (use 0b format): ")
        
        # Check if the user's answer is correct
        if user_bin == correct_bin:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_bin}\n")
    
    print(f"Game over! Your final score is {score}/{rounds}.")
    if score == rounds:
        print("Excellent! You're a hex to binary conversion master!")
    elif score >= rounds // 2:
        print("Great job! Keep practicing to improve even more!")
    else:
        print("Don't worry, with more practice you'll get better!")

# Start the game
if __name__ == "__main__":
    hex_to_bin_game()
