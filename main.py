"""
module documentation
"""
# This is a sample Python script.
from median_two_sorted_arrays import  MedianTwoSortedArrays

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    """
    Print 'Hi, + name'
    :param name: a name
    :return: None
    """
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Edwin')
    x = MedianTwoSortedArrays()
    print(x.find_median_two_sorted_arrays([3, 4], [1, 2, 5]))
    print(x.find_median_two_sorted_arrays([3], [1, 2, 4]))
    print(x.find_median_two_sorted_arrays([2], [1, 3, 4]))
    print(x.find_median_two_sorted_arrays([1, 2], [-1, 3]))
    print(x.find_median_two_sorted_arrays([], [1]))
    print(x.find_median_two_sorted_arrays([1, 3], [2]))
    print(x.find_median_two_sorted_arrays([2], [1, 3]))
    print(x.find_median_two_sorted_arrays([1, 2, 3], [4, 5]))
    print(x.find_median_two_sorted_arrays([2, 4], [1, 3]))
    print(x.find_median_two_sorted_arrays([1, 3], [2, 4]))
    print(x.find_median_two_sorted_arrays([1], [2, 3, 4, 5, 6]))
    print(x.find_median_two_sorted_arrays([1, 2, 3, 4], [5, 6]))
    print(x.find_median_two_sorted_arrays([1, 2, 3], [4, 5, 6]))
    print(x.find_median_two_sorted_arrays([1, 3, 5], [2, 4, 6]))
    print(x.find_median_two_sorted_arrays([2, 5, 6], [1, 3, 4]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
