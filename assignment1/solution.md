## Exercise 1


### a)

The number of distinct 5-card hands is the number of ways to choose 5 cards out of 52:

C(52, 5) = 52! / (5! 47!) = 2,598,960

### b)

Each atomic event has equal probability:

1 / C(52,5) = 1 / 2,598,960 ≈ 3.85 * 10^-7

### c)

**Royal straight flush**: 
- There are 4 suits -> 4 such hands

	Probability = 4 / C(52,5) = 1 / 649,740 ≈ 1.539 * 10^-6

- **Four of a kind**:
	- Choose rank for the quadruple: 13 ways
	- Choose remaining card: any of the other 48 cards

	Count = 13 * 48 = 624

	Probability = 624 / C(52,5) = 1 / 4,165 ≈ 2.401 * 10^-4

## Exercise 2

### a) 

All 64 outcomes (4^3) are equally likely. Counting winning outcomes:

- `BAR/BAR/BAR`: 1 outcome -> 20
- `BELL/BELL/BELL`: 1 outcome -> 15
- `LEMON/LEMON/LEMON`: 1 outcome -> 5
- `CHERRY/CHERRY/CHERRY`: 1 outcome -> 3
- `CHERRY/CHERRY/?`: 3 outcomes -> 2
- `CHERRY/?/?`: 3*4 = 12 outcomes -> 1

Total payout over all outcomes = 20 + 15 + 5 + 3 + 3\*2 + 12\*1 = 61

Expected return per play = 61 / 64 ≈ 0.953125 = 95.31% payback

### b)

Number of winning outcomes = 1+1+1+1+3+12 = 19

Probability(win) = 19 / 64 ≈ 0.296875 = 29.69%

### c)

```
python solution.py --slot
``` 

Summary of results (20,000 trials):

- Trials: 20000
- Starting coins: 10
- Mean plays until broke: 219.199
- Median plays until broke: 21

## Exercise 3

### Part 1 

### a)

```
python solution.py --birthday
```

### b) 

Summary of results (20,000 trials): 
- The smallest `N` such that the probability is at least 50% is 23 (P ≈ 0.506 in the simulation).
- The proportion of `N` in the interval [10, 50] for which the event happens with at least 50% chance is 28/41 ≈ 0.683.

### Part 2

### a)
```
python solution.py --cover
```

Summary of results (20,000 trials):
- Mean number of people required: 2366.689
- Median number required: 2290

