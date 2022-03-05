from phrasehunter import game


class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.unique_letters = set(self.phrase)
        self.unique_letters.discard(' ')

    def display(self, guesses):
        for letter_guess in self.phrase:
            if letter_guess ==' ':
                print(' ', end = ' ')
            elif letter_guess in guesses:    
                print(f'{letter_guess}', end=" ")
            else:
                print("_", end=" ")   

    def check_letter(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False        
    
        
    def check_complete(self, guesses):
      if len(self.unique_letters - set(guesses)) == 0:
          return True
