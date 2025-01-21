import os


def run():
    name = os.environ['INPUT_NAME']
    print(f"Your name is: {name}")


if __name__ == '__main__':
    run()
