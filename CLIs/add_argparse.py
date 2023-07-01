import argparse


parser = argparse.ArgumentParser(
    prog="Add Numbers",
    description="Adds entered numbers"
)

parser.add_argument('nums',
                    type=float,
                    nargs="+",
                    help="numbers to be added")

args = parser.parse_args()

print(sum(args.nums))
