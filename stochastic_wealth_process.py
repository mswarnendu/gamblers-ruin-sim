import random


def bet(p):
    winFactor = random.random()
    if winFactor < p:
        return 1
    else:
        return -1


def simulation(p, TRIALS, BALANCE, TARGET):
    ruins = 0
    MAX_STEPS = BALANCE * TARGET
    for _ in range(TRIALS):
        cur_balance = BALANCE
        steps = 0
        while cur_balance < TARGET and cur_balance > 0 and steps < MAX_STEPS:
            cur_balance += bet(p)
            steps += 1
        if cur_balance == 0:
            ruins += 1

    ruin_prob = ruins / TRIALS

    print(f"Win Rate: {p * 100}%")
    print(f"Loss rate: {(1 - p) * 100}%")
    print(f"Ruin Probability: {ruin_prob * 100}%\n")


def main():

    BALANCE = int(input("Enter your balance: "))
    TARGET = int(input("What's the target amount of money to reach? "))

    TRIALS = int(
        input("How many trials would you like to run (more trials = longer runtime but more accuracy)? "))

    p1 = 0.49
    p2 = 0.5
    p3 = 0.51

    print("This might take a while...")
    print()
    print("EXPERIMENT #1 (49% WIN RATE):\n")
    simulation(p1, TRIALS, BALANCE, TARGET)
    print("EXPERIMENT #2 (50% WIN RATE):\n")
    simulation(p2, TRIALS, BALANCE, TARGET)
    print("EXPERIMENT #3 (51% WIN RATE):\n")
    simulation(p3, TRIALS, BALANCE, TARGET)


if __name__ == "__main__":
    main()
