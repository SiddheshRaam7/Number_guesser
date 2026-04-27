import random
import math

def show_top_scores():
    """This function shows the leaderboard in the correct order"""
    scores = []
    try:
        with open("leaderboard.txt", "r") as file:
            for line in file: #goes through every line in the file to get their scores and username
                parts = line.strip().rsplit(": ", 1) #makes sure that the splitting is done from right. Prevents errors while using usernames such as Gamer: 123
                if len(parts) == 2:
                    #This try statement ensures that any edits to the text files are skipped
                    try:
                        scores.append([int(parts[1]), parts[0]])
                    
                    except ValueError:
                        continue
        
        scores.sort() #sorts the scores from lowest to highest(remember the lower the attempts of guess the better)

        print("\n---TOP 10 LEADERBOARD---") #displays the top 10 scores
        if not scores:
            print("No scores yet. Be the first!")
        else:

            rank = 1
            for entry in scores[:10]:
                # entry is [score, username]
                print(f"{rank}. {entry[1]} - {entry[0]} guesses")
                rank += 1

    except FileNotFoundError: #error raised when the leaderboard file is not downloaded from the repository
        print("\nNo leaderboard file found yet.")

def save_score(username, guesses):
    """
    This function will store the username and the amount
    of guesses in a separate file
    """
    with open("leaderboard.txt", "a") as file: #adds the username and attempts to guess to the leaderboard file
        file.write(f"{username}: {guesses}\n")
    print("Score saved to leaderboard!")

def replay():
    """
    This function starts another session(with the same username) of the game if the user desires
    """
    choice = None
    while choice not in ["YES", "NO"]: #makes sure the user enters a valid choice
        choice = input("\nWould you like to play again(Yes/No): ").upper().strip()
        if choice not in ["YES", "NO"]:
            print("Invalid input.")

    if choice == "YES":
        return True
    
    else:
        return False

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

    while guessed_num != random_num: #runs the loop until the number is guessed or the user runs out of attempts
        guessed_num = input("\nState your guess (1-100): ").upper().strip()

        if guessed_num == "Q": #quits the game is the user enters q
            print(f"Game over. The number was {random_num}")
            show_top_scores()
            return replay()
        
        try: #this try block ensures that the user inputs a valid number
            guessed_num = int(guessed_num)

            if guessed_num < 1 or guessed_num > 100: #ensures that the guess is in between 1 and 100
                print("Guess must be between 1 and 100")


            elif guessed_num in previous_guesses: #ensures that the user doesn't guess the same number twice
                print("You have already guessed this number")
            
            else:
                previous_guesses.append(guessed_num)

                if guessed_num > random_num:
                    print("Too High")

                elif guessed_num < random_num:  
                    print("Too low")

                else: #this runs if the user guessed the number correctly
                    print("\nCorrect.")
                    print(f"It took you {num_guesses} number of guesses")
                    save_score(username, num_guesses)
                    show_top_scores()
                    return replay()
                
                remaining_guess -= 1
                num_guesses += 1

                if remaining_guess == 0: #if the user runs out of guesses
                    print(f"Game over. The number was {random_num}")
                    show_top_scores()
                    return replay()

                if remaining_guess != math.inf: #displays the remaining attempts in hard and medium mode
                    print(f"{remaining_guess} chances remain… each one matters.\n")

        except ValueError:
            print("Invalid input.")
    

def main():
    """
    This function gathers initial data such as the username and game difficulty
    """

    game_continue = True
    username = None

    while game_continue: #this loop makes sure that the game is replayed with the same username if the user wants another try
        difficulty = None

        while username == "" or username is None: #makes sure the username is valid
            username = input("Please enter your username: ").strip()

        while difficulty not in ["H", "M", "E"]: #makes sure the user chooses a valid difficulty

            difficulty = input("Please choose your difficulty: Hard(10 attempts): H, Medium(20 attempts): M, Easy(Unlimited attempts): \n>>>").upper().strip()
            if difficulty not in ["H", "M", "E"] and difficulty:
                print("Please choose a valid difficulty")

        game_continue = game_level(difficulty, username)

if __name__ == "__main__":
    main()
