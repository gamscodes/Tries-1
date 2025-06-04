"""
Trie using fixed-size array (26 slots for 'a' to 'z').

- insert:     O(n) time, O(n*26) space (in worst case)
- search:     O(n) time
- startsWith: O(n) time

n = length of the word/prefix
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:  # O(L)
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:  # O(L)
        curr = self.root
        for char in word:
            idx = ord(char) - ord("a")
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:  # O(L)
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord("a")
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True


sol = Trie()
sol.insert("apple")
print(sol.search("apple"))  # True
print(sol.search("app"))  # False
print(sol.startsWith("app"))  # True
sol.insert("app")
print(sol.search("app"))  # True
