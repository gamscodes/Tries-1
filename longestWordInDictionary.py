"""
Approach:
- Build a Trie from the given words
- Use DFS to find the longest word where all prefixes are also valid words

Time: O(N * M), where N = number of words, M = average word length
Space: O(N * M), for the Trie and DFS stack
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # stores the complete word if this node marks the end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # mark the end of the word

        # DFS traversal
        res = ""
        stack = [root]
        while stack:
            node = stack.pop()
            if node.word is not None or node == root:
                if node != root:
                    if len(node.word) > len(res) or (
                        len(node.word) == len(res) and node.word < res
                    ):
                        res = node.word
                for child in node.children.values():
                    stack.append(child)
        return res


words = ["w", "wo", "wor", "worl", "world", "banana"]
sol = Solution()
print(sol.longestWord(words))  # Output: "world"
