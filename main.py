import random
import argparse
from typing_extensions import Annotated
import typer
from rich import print

app = typer.Typer()

# parser = argparse.ArgumentParser(
#     prog="daff",
#     description="This program prints out daily affirmations.",
# )


@app.command()
def main(number: Annotated[int, typer.Argument()] = 1):
    """Print out a random affirmation per day."""
    # parser.add_argument(
    #     "-n",
    #     "--number",
    #     default=1,
    #     type=int,
    #     action="store",
    #     help="generate a specific number of affirmations",
    # )

    with open("affirmations.txt") as f:
        lines = f.readlines()
        random.shuffle(lines)
    # args = parser.parse_args()
    # print(args.number)
    # number = args.number
    if number == 1:
        print(f"[bold]{random.choice(lines).strip()}[/bold]")
    elif number > 1:
        for index in range(1, number + 1):
            print(f"[bold]{index}[/bold]. {random.choice(lines).strip()} ")
    else:
        raise Exception("The number passed in was smaller than 1.")


if __name__ == "__main__":
    # typer.run(main)
    app()
