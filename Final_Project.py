import random
import math

def show_top_scores():
    """This function shows the leaderboard in the correct order"""
    scores = []
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file:
                parts = line.strip().split(": ")
                if len(parts) == 2:
                    # Storing as [score, username] so we can sort easily
                    scores.append([int(parts[1]), parts[0]])
        
        # Sorts by the first element (the score) automatically
        scores.sort()

        print("\n---TOP 3 LEADERBOARD---")
        if not scores:
            print("No scores yet. Be the first!")
        else:
            # This will print out the scores a manual counter for the ranking
            rank = 1
            for entry in scores:
                # entry is [score, username]
                print(f"{rank}. {entry[1]} - {entry[0]} guesses")
                rank += 1

    except FileNotFoundError:
        print("\nNo leaderboard file found yet.")

def save_score(username, guesses):
    """
    This function will store the username and the amount
    of guesses it took them to get it right in a seperate file
    to ensure that they can get this data anytime they want.
    """
    with open("leaderboard.txt", "a") as file:
        file.write(f"{username}: {guesses}\n")
    print("Score saved to leaderboard!")

def replay():
    choice = None
    while choice not in ["YES", "NO"]:
        choice = input("Would you like to play again(Yes/No): ").upper().strip()
        if choice not in ["YES", "NO"]:
            print("Invalid input.")

    if choice == "YES":
        main()
    
    else:
        return

def game_level(difficulty, username):
    """
    This the function where the game happens
    """
    random_num = random.randint(1, 100)
    guessed_num = None
    previous_guesses = []
    num_guesses = 1
    difficulty_dictionary = {"H": 10, "M": 20, "E": math.inf}
    remaining_guess = difficulty_dictionary[difficulty]

    print("\nThe game has begun...\n")
    print("Please type Q to quit at any time of the game")

    while guessed_num != random_num:
        guessed_num = input("\nState your guess (1-100): ").upper().strip()

        if guessed_num == "Q":
            print(f"Game over. The number was {random_num}")
            return
        
        try:
            guessed_num = int(guessed_num)

            if guessed_num in previous_guesses:
                print("You have already guessed this number")
            
            else:
                previous_guesses.append(guessed_num)

                if guessed_num > random_num:
                    print("Lower")

                elif guessed_num < random_num:  
                    print("Higher")

                else:
                    print("\nCorrect.")
                    print(f"It took you {num_guesses} number of guesses")
                    save_score(username, num_guesses)
                    show_top_scores()
                    replay()
                    return
                
                remaining_guess -= 1
                num_guesses += 1

                if remaining_guess == 0:
                    print(f"Game over. The number was {random_num}")
                    show_top_scores()
                    replay()
                    return

                if remaining_guess != math.inf:
                    print(f"{remaining_guess} chances remain… each one matters.\n")

        except ValueError:
            print("Invalid input.")
    

def main():
    
    
    difficulty = None
    username = input("Please enter your username: ")

    while difficulty not in ["H", "M", "E"]:

        difficulty = input("Please choose your difficulty: Hard(10 attempts): H, Medium(20 attempts): M, Easy(Unlimited attempts): E \n>>>").upper().strip()
        if difficulty not in ["H", "M", "E"] and difficulty:
            print("Please choose a valid difficulty")

    game_level(difficulty, username)

if __name__ == "__main__":
    main()
