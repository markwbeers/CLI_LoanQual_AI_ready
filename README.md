# Loan Qualifier - Module 2 Challenge
The BizOps team analyzed our borrower screening process, demanded a better customer experience with a more personalized, friendlier terminal intrerface.
IT team has delivered beyond your wildest Branch Manager expectations!
This prototype is ready for enhancements from AI and Machine Learning to help borrowers repair credit and secure funding! 

*Don't take our word for it, give it a try now!*  

Once you deploy this new state of the art technology in your UCB FinTech Credit Union Branch, you are on your way to cross selling financial products and offering a whole new world of exciting lending opportunities.

+ Cut the wait times at the loan counter.
+ Watch cash roll out faster than quicksilver.
+ Grow your loan portfolio faster than you've ever imagined. 
+ Client aquisition has never been easier when you show how much you care about their financial security.
+ Your loan officers, credit counselors, and tellers will all open new accounts faster than a Wells Fargo Bank, circa 2016!  Guaranteed!

Now behold the wonders of financial technology and thrilling experience of the unparalleled marvel that can only be described as... 

# *`The UCB FinTech Desktop Underwriter, Version 2.0`*
---


## [*User Story*](https://courses.bootcampspot.com/courses/3426/assignments/52458?module_item_id=939546)
        As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.

## [*Acceptance Criteria*](https://courses.bootcampspot.com/courses/3426/assignments/52458?module_item_id=939546)
        Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.

        Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

        Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

        Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

        Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file. 


---

## Technologies

Get ready to experience the groundbreaking financial technology `Command Line Interface` rolled out in a robust `Python 3.7` environment.

`Loan Qualifier V.2` is preloaded with all the bells and whistles that Module 2 has to offer including the power of Python Libraries *Questionary* and *Fire* - with the power to transform any Python Object into a CLI 

+ Programming Language: `Python 3.7`
+ Built-in python libraries: `csv`, `sys`, *and* `pathlib`
+ Imported python libraries: `fire` *and* `questionary`
+ Framework used: `CLI`

---

## Installation Guide

Before the *V-2 Release Party of the decade* begins, you absolutely must pre-load these 2 epic libraries...

```python
  pip install fire
  pip install questionary
```
Then, open your terminal and type `conda activate dev` - take a seat and launch the program 
```
        $ python app.py
```

---

## Usage

+ `sys` allows module to call `exit` function if user unable to provide correct path to the `daily_rate_sheet.csv`
+ `fire` library is used to generate CLI's with one line of code; this app uses it to create `variables`    
+ `questionary` library imported as `qst` to save reduce code by `7` characters per instance `x9` times = `63 less keystrokes`!
+ changed name of `daily_rate_sheet.csv` to `rates.csv` to make easier to enter 
+ changed name of several variables in starter code to make reading code more clear to coding newbs like me
+ defined and added `'save_csv'` function in `'fileio.py'` because that is where `csv` library was imported
+ added code: `'from qualifier.utils.fileio import save_csv'` to call function from `fileio.py` to maintain modular coding style
---

## Contributors

Mark Beers: 
[Linked In](https://www.linkedin.com/in/markwbeers/)
---

## License

MIT 
