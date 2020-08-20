from phrasehunter.character import Character

class Phrase:
    """
    This class converts string phrases to lists of characters,
    and keeps track of whether all of the characters have been guessed.
    """
    def __init__(self, phrase):
        """
        Constructor for the character class
        
        Parameters
        ----------
        phrase : str
            This is called by the phrasehunter.game.Game object's constructor.
        """
        self._was_guessed=False
        self.phrase=[ Character(char) for char in phrase ]

    def check(self):
        for char in self.phrase:
            if char.was_guessed:
                continue
            else:
                return False
        return True

    @property
    def was_guessed(self):
        if not self._was_guessed:
            self._was_guessed=self.check()
        return self._was_guessed

    @property
    def display_guess_data(self):
        output_str=""
        if self.was_guessed:
            for char in self.phrase:
                output_str += char.display_guess_data
        else:
            for char in self.phrase:
                output_str += char.display_guess_data
                output_str += " "
        return output_str


