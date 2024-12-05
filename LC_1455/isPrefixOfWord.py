class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,v in enumerate(sentence.split(" ")):
            for l in range(len(v)):
                if len(searchWord)>len(v) or v[l]!=searchWord[l]:
                    break
                if l == len(searchWord)-1:
                    return i+1
        return -1
class TrieNode:
    def __init__(self):
        self.children =  {}
        self.endNode = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self,word):
        curr = self.root
        for w in word:
            if curr and w not in curr.children:
                curr.children[w] = TrieNode()
            curr=curr.children[w]
        curr.endNode = True
    def startsWith(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True
    
class Solution2:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        trie = Trie()
        for i,word in enumerate(words):
            trie.add_word(word)
            if trie.startsWith(searchWord):
                return i+1
        return -1