import arguably


@arguably.command
def add(*args: float):
    """Adds entered numbers"""
    print(sum(args))

if __name__ == '__main__':
    arguably.run()
    