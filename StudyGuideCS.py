# =====================================================
# QUESTION 1: Looping Through a String
# =====================================================

# looping through a string
s = "IBM"

# for every index in range of the length of the string 's'
for i in range(len(s)):
    # print string at index
    print(s[i])


# =====================================================
# QUESTION 2: Reverse a String
# =====================================================

# reverse a string
def reverse_string(s):
    # empty result string to print later
    result = ""
    # for every index in range of the length of the string, start, stop step
    # starts at the last valid index (0) and then stops before -1, iterating backward by 1 at a time.
    for i in range(len(s) - 1, -1, -1):
        # every iteration add the string at index [i]
        result += s[i]
        # return result of the result string
    return result


# =====================================================
# QUESTION 3: Find the Maximum in an Array
# =====================================================

# loop & condition
# Find a maximum in an array (15 minutes)

nums = [3, 7, 2, 9, 4]

def find_max(nums):
    # assumes the max value is at index 0
    max_value = nums[0]
    # for every number in the nums list
    for num in nums:
        # if the num is greater than max_value
        if num > max_value:
            # max_value becomes the new num
            max_value = num
    # returns the new max_value
    return max_value

# The output would be
# 9
nums = [3, 7, 2, 9, 4]
print(find_max(nums))


# =====================================================
# QUESTION 4: Print Vowels in a String
# =====================================================

# loop & condition
input = "interview"

# for every i in range of the length of the string
for i in range(len(s)):
    # if the string at index is aeiou
    if s[i] in "aeiou":
        # print the string at index
        print(s[i])


# =====================================================
# QUESTION 5: Count Even Numbers in an Array
# =====================================================

# loop & condition
nums = [1,2,3,4,5,6]

# defining the function
def find_even(input):
    even = 0
    for num in nums: 
        if num % 2 == 0:
            count += 1
    return count

nums = [1, 2, 3, 4, 6]
print(find_even(nums))  # 3


# =====================================================
# QUESTION 6: Count Positive Numbers in an Array
# =====================================================

# Loop & Condition 
nums = [-2,0,3,7,-1]

# defining the function
def find_positive(nums):
    # starting with positive count at 0
    positives = 0
    # loop through the numbers
    for num in nums:
        # if the num is less than 0 it is not positive
        if num > 0:
            # add to the count
            count += 1
    # return the count
    return count

# Time complexity = O(n) only 1 pass through each character in the list
# space complexity = O(1) because no new data structures grow with input size
# edge case, zero could be mistaken for a positive

print(find_positive(nums)) # 2


# =====================================================
# QUESTION 7: Count Numbers Greater Than a Given Target
# =====================================================

# loop & condition
nums = [2, 8, 5, 10, 3]
target = 5

# defining the function
def greaterThanGiven(nums, target):
    numsGreaterThan = 0
    for num in nums:
        if num > target:
            numsGreaterThan += 1
    return numsGreaterThan

# Time Complexity = O(n) only 1 pass through each character in the list
# space complexity = O(1) because no new data structures grow with input size
# edge case; negative numbers, empty list returns 0, all numbers less than target


# =====================================================
# QUESTION 8: Count Occurrences of a Specific Character
# =====================================================

# Arrays & Strings
# Problem
# Write a function that counts how many times a specific character appears in a string.
# Rules
# Use a loop and a condition
# Do not use built-in counting methods
# Return a single number

s = "programming"
char = "g"

# defining the function, passing both variables through it
def count_char(s, char):
    # for every character in string
    for c in s:
        # if the character == the char "g"
        if c == char:
            # add +1 to the count
            count += 1
    # return the count
    return count


# =====================================================
# QUESTION 9: Check if a String Contains Any Digit
# =====================================================

# Problem
# Write a function that returns True if a string contains any digit (0–9), and False otherwise.
# Rules
# Use a loop and a condition
# Do not use built-in string methods like isdigit()
# Return a boolean

input = "hello"

def contains_digit(s):
    # loop through each character in the string
    for char in s:
        # check if the character is between '0' and '9'
        if '0' <= char <= '9':
            return True

    # no digit found
    return False


# =====================================================
# QUESTION 10: First Non-Repeating Character
# =====================================================

# define the function
def first_non_repeating_char(s):
    # initialize a dictionary
    counts = {}

    # first pass: count occurrences
    # for every character in string
    for char in s:
        # Increase the count for this character by 1.
        # counts.get(char, 0) + 1
        # give me the value for the key if it exists, otherwise default 0
        counts[char] = counts.get(char, 0) + 1

    # second pass: find first character with count 1
    # for every character in string
    for char in s:
        # if the current character in counts == 1
        if counts[char] == 1:
            # return the char
            return char

    return None

# time complexity: O(n) 
# first loop counts characte occurences O(n)
# second loop finds the character with count 1 O(n)
# Combined O(n+n) = O(n)

# space complexity: O(n)
# The dictionary (hash map) stores character counts
# in the worse case, every character is unique
# Edge Case: An empty string will return None


# =====================================================
# QUESTION 11: Basic Palindrome Check
# =====================================================

# how you check if something is a palindrome
def is_palindrome(s):
    # initializing variables
    left = 0
    # length of the string -1 , which means it will start at the index of the last character
    right = len(s) - 1

    # compare characters from both ends
    # while left is less than right
    while left < right:
        # if the string at left doesn't equal the string at right
        if s[left] != s[right]:
            # return false
            return False
        # increment +1 to left and right
        left += 1
        right -= 1

    return True

# Time Complexity: O(n) Each character is compared once, the loop moves inward from both ends
# Space Complexity: O(1) uses only two pointers, and no new data structures grow with input size
# edge cases: empty string will return true


# =====================================================
# QUESTION 12: Palindrome Ignoring Case and Non-Alphanumeric
# =====================================================

# Problem
# Write a function that checks whether a string is a palindrome ignoring non-alphanumeric characters and ignoring case.
# Rules
# Use loops and conditions
# Do not use built-in reverse helpers
# You may use basic string methods like .lower()

def is_palindrome(s):
    # first I have to initalize the pointers on both sides of the string
    left = 0
    right = len(s) - 1

    # the loop condition will be 'while' 
    while left < right:
        # skip non-alphanumeric characters on the left
        # while left is less than right and the character is not alpha numeric
        while left < right and not s[left].isalnum():
            left += 1

        # skip non-alphanumeric characters on the right
        while left < right and not s[right].isalnum():
            right -= 1

        # compare characters ignoring case
        # if the current character on the left pointer, and the right pointer are not the same, the string is not a palindrome
        if s[left].lower() != s[right].lower():
            # returning false because the string is not a palindrome
            return False

        # after comparing, increment on left side, and decrement on right side.
        # increment +1 on left and -1 on the right side, closing in
        left += 1
        right -= 1
    return True

# Time Complexity: O(n) no nested loop
# Space Complexity: O(1) data does not grow with input size
# Edge Case: non alpha numeric characters can break the loop


# =====================================================
# QUESTION 13: Sum Numbers Greater Than a Target
# =====================================================

nums = [1, 5, 8, 2, 10]
target = 4

# define the function
def sumOfNumbers(nums, target):
    # initialize total variable
    total = 0
    # for every number in nums
    for num in nums:
        # if the num is greater than target
        if num > target:
            # add it to the total
            total += num
    return total

# should print out 23
print(sumOfNumbers(nums, target))

# Time Complexity: O(n) no nested loop
# Space Complexity: O(1) data does not grow with input size
# edge case: nums can return 0 if the list is empty


# ================================================================================================
# QUESTION 14: Write a function that counts how many alphabetic characters are in a string
# ================================================================================================

#define the function
def count_letters(s):
    # initialize the count at 0
    count = 0
    # for every character in the string
    for char in s:
        # if the character is alphabetic
        if char.isalpha():
            # add to the count
            count += 1
    # return the count
    return count

print(count_letters("Hello, World! 123")) #10 characters

# ======================================================================================================================================
# QUESTION 15: Write a function that returns True if all alphabetic characters in a string are unique (no repeats), and False otherwise
# ======================================================================================================================================
# Ignore case and non-alphabetic characters.

def all_unique_letters(s):
    # Create an empty collection that will keep track of values I've already seen
    seen = set()

    for char in s:
        # if the character is alphabetic
        if char.isalpha():
            # normalize the character (make it lowercase)
            normalized = char.lower()
            # Checking if normalized is in seen, then it's not unique
            if normalized in seen:
                return False
            # adds the normalized character to seen
            seen.add(normalized)

        return True
    
# =============================
# Hash Maps 
# =============================

# =========================================================================================================
# Question 1: Write a function that returns True if an array contains duplicate values, otherwise False.
# =========================================================================================================

def contains_duplicate(nums):
    # initializing a hash map (dictionary)
    seen = set()
    #for every number in the nums list
    for num in nums:
        # if num has been seen already
        if num in seen:
            # return true
            return True
    # after the loop, add the number to the seen hashmap
    seen.add(num)
    # otherwise return false
    return False

# example
print(contains_duplicate([1, 2, 3, 4]))    # False
print(contains_duplicate([1, 2, 3, 1]))    # True

# Time Complexity: O(n) because we loop through the list once, each lookup in a set is O(1) on average
# Space Complexity: O(n) because the set stores seen values, in the worst case, all values are unique


# ==============
# Question 2: Given a list of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# =============

def two_sum(nums, target):
    seen = {}  # value -> index

    # for every index, and value do something
    for i, num in enumerate(nums):
        # complement is the number required to add up to target
        complement = target - num

        # if we've seen the complement before, we found the pair
        # is the complement in seen already?
        if complement in seen:
            # if yes then return the complement and index
            return [seen[complement], i]

        # otherwise store current number and its index
        seen[num] = i

#Time Complexity: O(n) One pass through the list
#Space Complexity: O(n) Dictionary stores seen values

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Edge Case: Duplicate values are handled correctly
# Edge case: Same number cannot be used twice because we check first and then store
# Edge Case: Negative numbers, complements still calculate correctly, Hash maps don't care about sign
# Edge Case: Zero as a value works because it works like any other number
# Edge Case: Multiple Valid pairs, the solution returns the FIRST valid pair
# Edge Case: No solution exists, the function will return none
# Edge Case: Large Input size, the hash map solution scales linearly.