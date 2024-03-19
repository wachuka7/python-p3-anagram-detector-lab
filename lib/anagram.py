# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word.lower()

    def match(self, candidates):
        sorted_word= sorted(self.word)
        anagrams =[candidate for candidate in candidates if self.is_anagram(sorted_word, candidate)]
        return anagrams
    def is_anagram(self, sorted_word, candidate):
        sorted_candidate=sorted(candidate.lower())
        return sorted_word==sorted_candidate