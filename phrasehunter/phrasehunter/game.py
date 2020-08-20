from phrasehunter.phrase import Phrase
from phrasehunter.character import Character

class Game:
    """
    This class handles phrasehunter game logic.
    """
    def __init__(self, phrases):
        """
        Constructor for the phrasehunter.game.Game class.

        Parameters
        ----------
        phrases : list
            This is can be edited in phrasehunter.phrases, which contains one list object, quote_list.
        """
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.guesses = []
        self.current_phrase = self.phrases[0]
        self.phrase_counter = 0
        self.life_counter = 0
        self.life_limit = 3
        self.wants_to_play = True
        
    @property
    def remaing_guesses(self):
        """
        Returns the number of remaining guesses.
        """
        return self.life_limit - self.life_counter
    
    def next_phrase(self):
        """
        Increment the phrase counter, empty the list of guesses, reset
        the life counter, and set self.current_phrase to the next available phrase.
        """
        self.phrase_counter += 1
        self.guesses=list()
        self.life_counter=0
        try:
            self.current_phrase = self.phrases[self.phrase_counter]
            print("Here's the next phrase: ")
        except IndexError:
            print("Sorry, no more phrases are available.")
            exit()

    def start(self, starting_phrase_index):
        """
        Start the game.
        """
        self.phrase_counter = starting_phrase_index
        self.life_counter = 0
        print("Here's the puzzle:")
        while self.wants_to_play:
            result = self.prompt_guess()

            if result == True:
                print("Correct! You got it!\n")
            else:
                print("Sorry, that is incorrect.\n")
                self.life_counter += 1             
         
            if self.remaing_guesses <= 0:
                print("You are all out of guesses.\n")
                if self.prompt_quit() == True:
                    print("Goodbye!\n")
                    exit()
                else:
                    self.start(self.phrase_counter)
 
            if self.current_phrase.was_guessed:
                self.congrats()
                if self.prompt_quit() == True:
                    print("Goodbye!")
                    exit()
                else:
                    self.next_phrase()

    def congrats(self):
        congrats="~`\) Congratulations! (/`~" 
        print("-" * len(congrats))
        print(congrats)
        print("-" * len(congrats))
        print("You guessed the ENTIRE phrase!")

    def prompt_quit(self):
        """
        Prompt the user if they would like to play again.

        Return False if 'Yes', or True if 'no'.
        """
        answer=input("Would you like to play again? (Y/n) ")
        if answer[0].lower() == 'y':
            return False
        else:
            return True


    def prompt_guess(self):
        print(f"{self.current_phrase.display_guess_data}\n")
        char = input(f"You have {self.remaing_guesses} remaining guesses. What is your guess?\nYour guess: ")
        if char in self.guesses:
            print("Oops! You've guessed that already! Please try again.")
            self.prompt_guess()
        if len(char) > 1:
             print("Oops! Guesses must be a maximum of 1 character in length.")
             self.prompt_guess()
        else:
            self.guesses.append(char)
            result = self.guess(char)
            return result

    def guess(self, guess):
        """
        Handle the player's guesses.
        """
        guess_result=False
            
        for char in self.current_phrase.phrase:
            char_result = char.check_guess(guess)
            if char_result == True:
                guess_result = True
        return guess_result            



