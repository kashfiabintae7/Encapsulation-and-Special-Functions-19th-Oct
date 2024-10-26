class Word:
    
    def __init__(self, word):
        self.word = word
        
    def revstr(self):
       return ''.join([self.word[i] for i in range(len(self.word) - 1, -1, -1)])


wo = Word("GigaPeppafamily")
print("Reversed word: ", wo.revstr())    