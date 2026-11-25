"""Unplugged — print a smart toaster's breakup line."""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"


def load_breakup_line() -> str:
    """Return the toaster's parting words, stored in entry.txt."""
    line = ENTRY_PATH.read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit("entry.txt is empty — the toaster unplugged before speaking")
    return line


def main() -> None:
    print(load_breakup_line())


if __name__ == "__main__":
    main()
