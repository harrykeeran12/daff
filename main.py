import random
import argparse


parser = argparse.ArgumentParser(
    prog="daff",
    description="This program prints out daily affirmations.",
)


def main():
    """Print out a random affirmation per day."""
    parser.add_argument("-n", "--number", default=1, type=int, action="store", help="generate a specific number of affirmations")

    with open("affirmations.txt") as f:
        lines = f.readlines()
        random.shuffle(lines)
    args = parser.parse_args()
    # print(args.number)
    if args.number == 1:
        print(random.choice(lines).strip())
    else:
        for index in range(1, args.number + 1):
            print(f"{index}. {random.choice(lines)} ")


if __name__ == "__main__":
    main()
