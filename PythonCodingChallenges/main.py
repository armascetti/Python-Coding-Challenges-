#coding challenges to keep my skills sharp. I asked AI to provide me with intverview style coding challenges to solve. 
#Copied and pasted those problems here and solved them without the use of AI. 

# Easy

# 1. Count Vowels
# Write a function that returns the number of vowels in a string.

def count_vowels(words):
    count = 0
    for letter in words:
        if letter in "aeiouAEIOU":
            count += 1
    return count 
        
print(count_vowels("APPLE"))


# 2. Find Duplicates
# Given a list, return a set containing all duplicated values.

# find_duplicates([1, 2, 2, 3, 4, 4, 4])
# # {2, 4}

#my notes: 
        #create an empty set called single (a set wont repeat the number when added)
        # create an empty set called dup 
        # iterate through the list 
        # If statement and in operator to find the duplicate 
        # return the value to single and dup if its in twice 
def duplicates(list):
    seen = set()
    dup = set()
    for number in list:
        if number in seen: 
            dup.add(number)
        else: 
            seen.add(number)
    return dup

print(duplicates([1, 2, 2, 3, 4, 4, 4]))
            

# 3. Reverse Words
# Reverse the order of words in a sentence.

# reverse_words("python is fun")
# # "fun is python"

def reverse_words(sentence):
    words = sentence.split()
    #declare a variable and split the sentence 
    reversed_sentence = []
    #declare a new variable with an empty list that the new sentence can be put into 

    for i in range(len(words) -1, -1, -1):
        #this for loop decrements through the sentence one by one 
        check = reversed_sentence.append(words[i])
        #this will create the reversed sentence 
    print(" ".join(reversed_sentence))

reverse_words("Hi me")
    

# 4. Dictionary Frequency Counter
# Count how many times each word appears.

# word_frequency("cat dog cat bird")
# # {'cat': 2, 'dog': 1, 'bird': 1}

def word_frequency(sentence):
    words = sentence.split()
    #need to split the sentence into individual words 
    count = {}
    #declare an empty dictionary, to store the word counts  

    for word in words:
        #iterate through the words in order to count 
        if word in count: 
        #is it already a key in the dictionary? 
            count[word] += 1
            #Yes it is add it by 1 
        else: #first time seeing the word 
            count[word] = 1 
            # first time seeing it, start the  count with 1 
    print(count)

# Intermediate

# 5. Validate Patient Records
# Using the medical records example you've been working on:

# Check required keys
# Validate patient ID format
# Validate age >= 18
# Return a list of invalid fields

# 6. Two Sum
# Find two numbers that add up to a target.

# two_sum([2, 7, 11, 15], 9)
# # (0, 1)

# 7. Group Anagrams

# group_anagrams(
#     ["eat", "tea", "tan", "ate", "nat", "bat"]
# )

# Expected:

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]

# 8. Most Frequent Character

# most_frequent("mississippi")
# # 'i'
# Interview-Style OOP

# 9. Bank Account Class

# Create a class:

# account = BankAccount("Mandy", 100)

# Methods:

# deposit(amount)
# withdraw(amount)
# get_balance()

# Prevent overdrafts.

# 10. Library System

# Create:

# Book
# Library

# Allow:

# adding books
# checking out books
# returning books

# Use classes and methods.

# Beginner AI-Flavored Problem

# 11. Resume Keyword Scanner

# Input:

# resume = """
# Python
# SQL
# Git
# """

# Job description:

# job = """
# Python
# AWS
# Docker
# Git
# """

# Return:

# {
#     "matched": ["Python", "Git"],
#     "missing": ["AWS", "Docker"]
# }

# This is actually a decent portfolio project because it demonstrates:

# strings
# sets
# dictionaries
# simple NLP concepts
# Good Interview Challenge

# 12. Log File Analyzer

# Input:

# logs = [
#     "ERROR Database connection failed",
#     "INFO User logged in",
#     "ERROR Invalid password",
#     "WARNING Disk space low"
# ]

# Return:

# {
#     "ERROR": 2,
#     "INFO": 1,
#     "WARNING": 1
# }

# This uses:

# dictionaries
# loops
# string methods

# and is very similar to work you might do in government/enterprise software.

# A good progression for the next week would be:

# Count Vowels
# Find Duplicates
# Dictionary Frequency Counter
# Two Sum
# Bank Account Class
# Resume Keyword Scanner
# Log File Analyzer

# That sequence covers most of the Python, data structures, and OOP concepts likely to come up in an entry-level software engineering interview.