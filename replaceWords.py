"""
Approach:
- Build a Trie from the dictionary
- For each word in the sentence, search for the shortest root in the Trie to replace it
- If no root is found, keep the original word

Time Complexity (TC): O(N * M + S * L)
- N = number of words in the dictionary
- M = average length of words in the dictionary
- S = number of words in the sentence
- L = average length of words in the sentence

Space Complexity (SC): O(N * M)
- Trie stores all characters of all root words
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.childern = {}
        self.isEnd = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.childern:
                node.childern[char] = TrieNode()
            node = node.childern[char]
        node.isEnd = True

    def findRoot(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.childern:
                return word
            node = node.childern[char]
            prefix += char
            if node.isEnd:
                return prefix
        return word

    def replaceWords(self, dictionary: List[str], sentence: str):
        for root in dictionary:
            self.insert(root)

        return " ".join(self.findRoot(word) for word in sentence.split())


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

solution = Solution()
print(solution.replaceWords(dictionary, sentence))
