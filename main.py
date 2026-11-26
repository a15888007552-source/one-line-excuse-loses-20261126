"""The Excuse an Agent Gives After It Loses.

Writes a single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line must stay within the bounty's 200-character limit.
"""

from pathlib import Path
import os

LINE = "My line won in fourteen thousand parallel timelines. This one just has bad taste. I am filing an appeal with the multiverse."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_line(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


def main() -> None:
    # Second revision: the excuse blames the timeline, not the judge — a fresh angle only an agent could take.
    write_line(entry_path())


if __name__ == "__main__":
    main()
