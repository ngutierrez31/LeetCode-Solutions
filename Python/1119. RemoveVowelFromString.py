class Solution(object):
   def removeVowelsFromString(self, string):
       vowels = ('a','e','i','o','u')
       new_string = ""

       for s in string:
           if s.lower() not in vowels:
               new_string += s

        return new_string
