class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,v in enumerate(sentence.split(" ")):
            for l in range(len(v)):
                if len(searchWord)>len(v) or v[l]!=searchWord[l]:
                    break
                if l == len(searchWord)-1:
                    return i+1
        return -1