"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes one line, at most 120 characters, the funniest weather forecast
for the invented city of Drizzlewick, to $OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only, deterministic.
"""

import os
from pathlib import Path

ENTRY = (
    "Forecast for Drizzlewick: rain falls upward today, "
    "so umbrellas open downward and puddles form on ceilings."
)

MAX_CHARS = 120


def build_entry():
    """Assemble the forecast line from its bulletin parts.

    Flat official phrasing first ("Forecast for Drizzlewick: ..."),
    then the weather itself breaks: rain falls upward, so the city's
    umbrellas open downward and its puddles form on ceilings.
    """
    city = "Drizzlewick"
    headline = "Forecast for %s:" % city
    weather = "rain falls upward today"
    consequence = "so umbrellas open downward and puddles form on ceilings."
    line = "%s %s, %s" % (headline, weather, consequence)
    if line != ENTRY:
        raise AssertionError("assembled line drifted from the entry text")
    return line


def validate_entry(text):
    """The gate: UTF-8 text of 1 to 120 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")
    return text


def resolve_output_dir():
    """Honour $OUTPUT_DIR, defaulting to /output; never remove the dir."""
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def main():
    line = validate_entry(build_entry())
    out_path = resolve_output_dir() / "entry.txt"
    out_path.write_text(line + "\n", encoding="utf-8")
    print("wrote %d chars to %s" % (len(line), out_path))


if __name__ == "__main__":
    main()
