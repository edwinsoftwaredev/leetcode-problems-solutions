class LongestSubstringUnrepeatedChars:
    def length_of_longest_substring(self, s: str) -> int:
        temp_subs = ''
        temp_length = 0
        max_length_found = 0
        for char in s:
            if temp_subs.find(char) == -1:
                temp_length += 1
                temp_subs += char
            else:
                if max_length_found <= temp_length:
                    max_length_found = temp_length

                idx_char = temp_subs.index(char)
                if idx_char + 1 == len(temp_subs):
                    temp_subs = char
                else:
                    temp_subs = temp_subs[idx_char + 1:] + char

                temp_length = len(temp_subs)

        if temp_length > max_length_found:
            max_length_found = temp_length

        return max_length_found
