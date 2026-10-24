import random
import sys

EXCUSES = [
    "It works on my machine.",
    "That's not a bug, it's an undocumented feature.",
    "It was working five minutes ago.",
    "Must be a caching issue.",
    "Did you try turning it off and on again?",
    "I only changed one line.",
    "That code is older than me.",
    "The tests passed, so it's fine.",
    "It's probably a race condition.",
    "That's a problem for future me.",
    "The bug fixed itself. I didn't touch anything.",
    "It's a feature request in disguise.",
]


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for excuse in random.sample(EXCUSES, min(count, len(EXCUSES))):
        print(excuse)


if __name__ == "__main__":
    main()
