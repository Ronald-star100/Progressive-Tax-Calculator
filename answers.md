# Project 9: Progressive Tax Calculator

## Task 4: Test results

- Income exactly at the first cutoff ($18,750): tax was $1,087.50.
- Income exactly at the second cutoff ($64,250): tax was $6,729.50.
- Income of $0: tax was $0.00.
- Income of -$1: the app displayed “Income cannot be negative.”

## Task 5: AI Reflection

(a) I used AI to help me with coming up with the tax bracket and rates.

(b) I made sure the rates in my calculation matched the rates given to me by AI.

(c) The calculator works because it taxes each portion of income at that bracket’s rate, then adds the amounts together. It also checks for negative income before calculating tax, so it won’t produce a negative tax amount.

# Project 10 Answers

## Task 2: Git Log

c571186 (HEAD -> main, origin/main) Fix Python bytecode ignore rule
1861a1c Add Project 10 answers
b0aa6cf Document the tax calculation
3e437a4 Handle invalid income input
300d14e Add progressive tax calculator app

## Task 3: Github Repository

https://github.com/Ronald-star100/Progressive-Tax-Calculator 

## task 5: AI Reflection

(a) I used AI to help me create the GitHub repository and connect my project to it.

(b) I added the invalid-income handling, wrote the README, and made separate commits for the app, validation, and documentation.

(c) The commits record changes separately, and pushing the repository puts the project and its history on GitHub. The .gitignore keeps files such as the virtual environment and ZIP files out of the repository.