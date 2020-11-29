class TwoSum:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        solution = []

        for idx, value in enumerate(nums):
            if idx in solution:
                continue

            temp_idx = idx + 1
            while temp_idx < len(nums):
                if temp_idx in solution:
                    temp_idx += 1
                    continue

                if value + nums[temp_idx] == target:
                    solution += [idx, temp_idx]
                    break

                temp_idx += 1

        return solution

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        solution = []
        dictionaries = []

        for idx, value in enumerate(nums):
            if len(dictionaries) == 0:
                dictionaries.append({target - value: idx})

            if (target - value) in dictionaries[len(dictionaries) - 1].keys():
                dictionaries.append({target - value: idx})
            else:
                dictionaries[len(dictionaries) - 1][target - value] = idx

        for idx, value in enumerate(nums):
            if idx in solution:
                continue

            for dictionary in dictionaries:
                if value in dictionary:
                    if idx == dictionary.get(value):
                        continue

                    solution.append(idx)
                    solution.append(dictionary.get(value))
                    dictionary.pop(value)
                    break

        return solution

    def two_sum(self, nums: list[int], target: int) -> list[int]:
        solution = []
        dictionary = {}
        for idx, value in enumerate(nums):
            if len(dictionary) == 0:
                dictionary[target - value] = idx
                continue

            if value in dictionary.keys():
                solution.append(idx)
                solution.append(dictionary.get(value))
            else:
                dictionary[target - value] = idx

        return solution
