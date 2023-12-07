# Brainstorming
## Task
1. get the first and last digit on each line
2. create a 2 digit number from the first and last digit on each line
3. add all the 2 digit numbers together

NOTE does not specifiy what happens when there is no digits on a line so we dont have to test for case

## Objects needed
### FirstDigitFinder
- finds the first digit on a line
### LastDigitFinder
- finds the last digit on a line
### LineAnalyzer
- uses *FirstDigitFinder* & *LastDigitFinder*
- decyphers the line and stores the 2 digit number
### DocumentAnalyzer
- sums the value of all the *lineAnalyzers*