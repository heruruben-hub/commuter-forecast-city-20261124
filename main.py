"""Charm the Commuter entry: one forecast line for Glimmerwick.

Glimmerwick does not exist, which is the whole point: a fictional city
gets a real broadcast-weather rhythm, bent just enough to make a bored
commuter smile. The forecast opens with the city name, gives it weather
(a glitter drizzle at dawn, clearing by nine), then lands the joke the
commuter actually cares about -- the 8:15 tram running on time for once.
The line is 134 characters, inside the competition's 140-character cap,
and this program writes exactly that line to /output/entry.txt.
"""

import os

FORECAST = (
    "Glimmerwick: a glitter drizzle at dawn, clearing by nine, "
    "leave the umbrella, keep the sparkle, and the 8:15 tram "
    "is on time for once."
)


def main():
    path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
