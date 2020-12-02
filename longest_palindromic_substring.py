class LongestPalindromicSubstring:
    def longest_palindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''

        start, end = 0, 0
        for idx in range(len(s)):
            length1 = self._from_mid(s, idx, idx)
            length2 = self._from_mid(s, idx, idx + 1)
            if length1 > length2:
                length = length1
            else:
                length = length2

            if length > end - start:
                start = idx - (length - 1) // 2
                end = idx + length // 2

        return s[start:end + 1]

    def _from_mid(self, s: str, start: int, end: int) -> int:
        idx_start, idx_end = start, end
        while idx_start >= 0 and idx_end < len(s) and s[idx_start] == s[idx_end]:
            idx_start -= 1
            idx_end += 1
        return idx_end - idx_start - 1
