class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({''.join(morse[ord(f) - 97]for f in word) for word in words})