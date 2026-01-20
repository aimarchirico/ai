
# EXERCISE 1: Slot machine simulation
import random
import statistics
import argparse

random.seed(0)


SYMBOLS = ["BAR", "BELL", "LEMON", "CHERRY"]

# Precompute payouts for each outcome
payout_table = {}
for a in SYMBOLS:
    for b in SYMBOLS:
        for c in SYMBOLS:
            outcome = (a, b, c)
            if a == "BAR" and b == "BAR" and c == "BAR":
                payout = 20
            elif a == "BELL" and b == "BELL" and c == "BELL":
                payout = 15
            elif a == "LEMON" and b == "LEMON" and c == "LEMON":
                payout = 5
            elif a == "CHERRY" and b == "CHERRY" and c == "CHERRY":
                payout = 3
            elif a == "CHERRY" and b == "CHERRY":
                payout = 2
            elif a == "CHERRY":
                payout = 1
            else:
                payout = 0
            payout_table[outcome] = payout

# Create a list of outcomes and corresponding cumulative probabilities
outcomes = list(payout_table.keys())


def play_once():
    # sample uniformly among 64 outcomes
    a = random.choice(SYMBOLS)
    b = random.choice(SYMBOLS)
    c = random.choice(SYMBOLS)
    return payout_table[(a, b, c)]


def plays_until_broke(starting_coins):
    coins = starting_coins
    plays = 0
    while coins > 0:
        plays += 1
        coins -= 1  # bet
        coins += play_once()
    return plays


def slot_main(trials=100000, starting_coins=10):
    results = []
    for i in range(trials):
        results.append(plays_until_broke(starting_coins))
        # progress indicator
        if (i + 1) % 1000 == 0:
            print(f"Completed {i+1} / {trials} trials", flush=True)

    mean_plays = statistics.mean(results)
    median_plays = statistics.median(results)

    print("\nSimulation results:")
    print(f"Trials: {trials}")
    print(f"Starting coins: {starting_coins}")
    print(f"Mean plays until broke: {mean_plays:.3f}")
    print(f"Median plays until broke: {median_plays}")



# EXERCISE 3 PART 1: Birthday problem simulation


def has_duplicate_birthdays(n):
    """Return True if among n people at least two share the same birthday"""
    # generate n birthdays in [0,364]
    birthdays = [random.randrange(365) for _ in range(n)]
    # check for duplicates
    return len(set(birthdays)) < n


def estimate_prob(n, trials=20000):
    """Estimate probability that among n people there is at least one shared birthday"""
    count = 0
    for _ in range(trials):
        if has_duplicate_birthdays(n):
            count += 1
    return count / trials


def run_batch(ns=range(10, 51), trials=20000):
    probs = {}
    for n in ns:
        p = estimate_prob(n, trials=trials)
        probs[n] = p
        print(f"N={n:2d} -> P(>=1 shared birthday) ≈ {p:.4f}")
    return probs


def birthday_main(trials=20000):
    probs = run_batch(range(10, 51), trials=trials)

    # proportion of N in interval where prob >= 0.5
    ns = sorted(probs)
    ns_with_prob_ge_half = [n for n in ns if probs[n] >= 0.5]
    prop = len(ns_with_prob_ge_half) / len(ns)

    print("\nSummary:")
    print(
        f"Proportion of N in [10,50] with probability >= 0.5: {prop:.3f} ({len(ns_with_prob_ge_half)}/{len(ns)})"
    )
    if ns_with_prob_ge_half:
        print(f"Smallest N with probability >= 0.5: {min(ns_with_prob_ge_half)}")
    else:
        print("No N in [10,50] reaches probability >= 0.5")


# EXERCISE 3 PART 2: coupon collector / cover all days simulation

def cover_all_days(days=365):
    """Simulate adding random people until all `days` days are covered and return count."""
    seen = set()
    count = 0
    while len(seen) < days:
        b = random.randrange(days)
        seen.add(b)
        count += 1
    return count


def estimate_cover(trials=10000, days=365):
    """Estimate the distribution of group sizes needed to cover all `days` days.
    Returns a list of counts (one per trial)."""
    counts = []
    for i in range(trials):
        counts.append(cover_all_days(days))
        if (i + 1) % 1000 == 0:
            print(f"Completed {i+1} / {trials} trials", flush=True)
    return counts


def cover_main(trials=10000, days=365):
    counts = estimate_cover(trials=trials, days=days)
    mean_c = statistics.mean(counts)
    median_c = statistics.median(counts)
    stdev_c = statistics.stdev(counts)

    # theoretical expectation: days * H_days
    harmonic = sum(1.0 / i for i in range(1, days + 1))
    expected_theoretical = days * harmonic

    print("\nCover all days simulation")
    print(f"Trials: {trials}")
    print(f"Days: {days}")
    print(f"Mean people needed: {mean_c:.3f}")
    print(f"Median people needed: {median_c}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--slot", action="store_true", help="Runs slot simulations")
    parser.add_argument("--birthday", action="store_true", help="Runs birthday simulations")
    parser.add_argument("--cover", action="store_true", help="Runs cover all days simulations")
    args = parser.parse_args()

    if args.slot:
        trials = 20000
        starting = 10
        slot_main(trials, starting)

    if args.birthday:
        trials = 20000
        birthday_main(trials)

    if args.cover:
        trials = 20000
        cover_main(trials)
