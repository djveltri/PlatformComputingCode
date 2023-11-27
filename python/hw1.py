# YOUR NAME HERE
# Cite any sources you used to help with the homework including TAs and classmates

def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    chars = string[-2:]
    result = chars*3
    return result


def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False


# string 2 count_code
def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    y=0
    for i in range(len(string) - 3):
        if string[i:i+2] == "co" and string[i+3] == "e":
            y += 1
    return y

def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    return string.count("cat") == string.count("dog")

def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, use just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    mn = min(nums)
    mx = max(nums)
    sum_wo_extremes = sum(nums) - mn - mx
    count_wo_extremes = len(nums) - 2  # subtract 2 for the smallest and largest values
    centered_average = sum_wo_extremes // count_wo_extremes #
    return centered_average


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct_lo")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct_ab")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct_Hi")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct_11231")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 3, 1] does not have 123'
print("correct_11241")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct_112123")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct_aaacodebbb")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
# This line was given as "assert hascode("aaacodebbb") == 1, 'codexxcode has code'" but I believe it should be "assert hascode("aaacodebbb") == 1, 'codexxcode has code'"
print("correct_aaacodebbb")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct_cozexxcope")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct_catdog")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct_catcat")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct_1cat1cadodog")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct_1_2_3_4_100")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct_1_1_5_5_10_8_7")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct_-10_-4_-2_-4_-2_0")


# Problems found on https://codingbat.com/python
