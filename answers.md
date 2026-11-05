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

e73f4e1 (HEAD -> main, origin/main) Finalize Project 10 submission answers
225efd0 Ignore Python bytecode and ZIP files
33d0d81 Add Project 10 log, GitHub URL, and reflection
7370038 Document tax calculator setup and usuage
450d1aa Reject nonnumeric income before tax calculation
0c49294 Add progressive tax calculator with three brackets

## Task 3: Github Repository

https://github.com/Ronald-star100/Progressive-Tax-Calculator 

## task 5: AI Reflection

(a) I used AI to help me create the GitHub repository and connect my project to it.

(b) I added the invalid-income handling, wrote the README, and made separate commits for the app, validation, and documentation.

(c) The commits record changes separately, and pushing the repository puts the project and its history on GitHub. The .gitignore keeps files such as the virtual environment and ZIP files out of the repository.