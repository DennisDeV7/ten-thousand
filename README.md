# LAB - Class 06, 07

## Project: Ten-Thousand

## Author: Dennis DeVries

## Setup

### Run main script

In an active virtual environment: `python ten_thousand/game_logic.py`

### Run tests

For test_calculate_score.py: `pytest-watch -c -- -k test_calculate_score.py`\
For test_roll_dice.py: `pytest-watch -c -- -k test_roll_dice.py `\
For all tests: `pytest-watch -c`

Example run of game_logic.py
```
Welcome to Ten Thousand
(y)es to play or (n)o to decline
> y
Starting round 1
Rolling 6 dice...
*** 1 5 2 4 2 6 ***
Enter dice to keep, or (q)uit:
> 15
You have 150 unbanked points and 4 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 150 in round 1
Total score is 150 points
Starting round 2
Rolling 6 dice...
*** 4 5 2 1 6 5 ***
Enter dice to keep, or (q)uit:
> 155
You have 200 unbanked points and 3 dice remaining
(r)oll again, (b)ank your points or (q)uit:
> b
You banked 200 in round 2
Total score is 350 points
Starting round 3
Rolling 6 dice...
*** 2 4 1 6 2 5 ***
Enter dice to keep, or (q)uit:
> q
Thanks for playing. You earned 350 points
```


47 tests are expected: 47 are passing