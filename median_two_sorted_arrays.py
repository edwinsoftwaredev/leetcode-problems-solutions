class MedianTwoSortedArrays:
    def find_median_two_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            idx_medium1 = (total_length // 2) - 1
            idx_medium2 = idx_medium1 + 1
            result = self.__get_medium_merge_lists(nums1, nums2, idx_medium1, idx_medium2)
            return result / 2
        else:
            idx_medium = total_length // 2
            result = self.__get_medium_merge_lists(nums1, nums2, idx_medium, 0)
            return result

    def __get_medium_merge_lists(self, nums1: list[int], nums2: list[int], idx_medium1: int, idx_medium2: int) -> int:
        new_list = []
        # head is positioned at index 0
        # [3, 4], [1, 2, 5]
        while len(nums1) != 0 and len(nums2) != 0:
            if nums1[0] <= nums2[0]:
                new_list.append(nums1.pop(0))
            else:
                new_list.append(nums2.pop(0))

            result = self.__search_values(new_list, idx_medium1, idx_medium2)
            if result is not None:
                return result

        while len(nums1) != 0:
            new_list.append(nums1.pop(0))
            result = self.__search_values(new_list, idx_medium1, idx_medium2)
            if result is not None:
                return result

        while len(nums2) != 0:
            new_list.append(nums2.pop(0))
            result = self.__search_values(new_list, idx_medium1, idx_medium2)
            if result is not None:
                return result

    def __search_values(self, new_list: list[int], idx_medium1: int, idx_medium2: int) -> int:
        if idx_medium2 != 0:
            if len(new_list) - 1 >= idx_medium1 and len(new_list) - 1 >= idx_medium2:
                return new_list[idx_medium1] + new_list[idx_medium2]
            else:
                return None
        else:
            if len(new_list) - 1 >= idx_medium1:
                return new_list[idx_medium1]
            else:
                return None
