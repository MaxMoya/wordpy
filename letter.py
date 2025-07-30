# Create the implementation of the Letter class
class Letter:
    def __init__(self, letter: str):
        self.letter = letter
        self.in_correct_place = False
        self.in_word = False
        
    def is_in_correct_place(self) -> bool:
        return self.in_correct_place
    
    def is_in_word(self) -> bool:
        return self.in_word
    