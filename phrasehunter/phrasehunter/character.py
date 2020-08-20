
class Character:
    """
    This class handles the processing of the single character that is 
    entered by the user
    """
    def __init__(self, original):
        """
        Constructor for the character class
        Parameters
        ----------
        original : str
            This is the character that is entered by the user
        """
        self.original = original
        if self.original == ' ':
            self.was_guessed = True
        else:
            self.was_guessed = False
	
        if len(self.original) > 1:
            raise ValueError("char cannot exceed length of 1.")


    def check_guess(self, guess):
        """
        Check the character entry given by the user to see if the entry is
        valid or not
        
        Parameters
        ----------
        guess : char
            Character given by the users
        """
        self.guess = guess
        if self.guess.lower() == self.original.lower():
            self.was_guessed = True
            return True
        else:
            return False

    def __str__(self):
        """
        Makes a string representation of the character
        """
        return f"{self.original}"

    @property
    def display_guess_data(self):
        """
        Property to display the guessed character. Show the character if
        it's correct or show an underscore if not correct.
        """
        if self.was_guessed:
            return self.original
        else:
            return "_"
