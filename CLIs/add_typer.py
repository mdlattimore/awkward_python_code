import typer
from typing import List


def add(nums: List[float] = typer.Argument(None, help="Enter one or more numbers to add")):
    """Adds entered numbers"""
    print(sum(nums))

if __name__ == '__main__':
    typer.run(add)
