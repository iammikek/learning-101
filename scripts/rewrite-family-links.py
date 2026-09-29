#!/usr/bin/env python3
"""Replace duplicated *-101 Family catalogue blocks with a link to learning-101."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAMILY_LINK = "https://github.com/iammikek/learning-101"
SITE_LINK = "https://automica.io/learning-101.html"

SECTION_RE = re.compile(
    r"^(#{2,3})\s+(\d+\.\s+)?\*-101 Family\s*\n"
    r".*?"
    r"Catalogue: \[automica\.io/learning-101\]\(https://automica\.io/learning-101\.html\)\s*",
    re.MULTILINE | re.DOTALL,
)

INLINE_PATTERNS = [
    (
        re.compile(
            r"Full catalogue:\s*\[§ \*-101 Family\]\(#[^)]+\)",
            re.IGNORECASE,
        ),
        f"Full catalogue: [learning-101]({FAMILY_LINK})",
    ),
    (
        re.compile(
            r"See \[\*-101 Family\]\(#[^)]+\) for the full catalogue\.?",
            re.IGNORECASE,
        ),
        f"See [learning-101]({FAMILY_LINK}) for the full catalogue.",
    ),
    (
        re.compile(
            r"See \[§\d+ \*-101 Family\]\(#[^)]+\) for the full catalogue[^.]*\.?",
            re.IGNORECASE,
        ),
        f"See [learning-101]({FAMILY_LINK}) for the full catalogue.",
    ),
    (
        re.compile(
            r"See also \[§\d+ \*-101 Family\]\(#[^)]+\)\.?",
            re.IGNORECASE,
        ),
        f"See also [learning-101]({FAMILY_LINK}).",
    ),
    (
        re.compile(
            r"^(\s*\d+\.\s+)\[\*-101 Family\]\(#[^)]+\)\s*$",
            re.MULTILINE,
        ),
        rf"\1[*-101 Family]({FAMILY_LINK})",
    ),
]


def replacement(match: re.Match[str]) -> str:
    hashes = match.group(1)
    number = match.group(2) or ""
    heading = f"{hashes} {number}*-101 Family".rstrip()
    return (
        f"{heading}\n\n"
        f"Full family list, ports, and clone-with-submodules: "
        f"**[learning-101]({FAMILY_LINK})**. "
        f"Site catalogue: [automica.io/learning-101]({SITE_LINK}).\n"
    )


def transform(text: str) -> str:
    new_text, n = SECTION_RE.subn(replacement, text, count=1)
    if n != 1:
        raise SystemExit(f"expected exactly one Family section, found {n}")
    for pattern, repl in INLINE_PATTERNS:
        new_text = pattern.sub(repl, new_text)
    return new_text


def main() -> None:
    paths = sorted(
        p for p in ROOT.glob("*-101/README.md") if p.parent.name != "learning-101"
    )
    # Also handle when script lives in learning-101 root: paths are submodule READMEs
    if not paths:
        paths = sorted(ROOT.glob("*/README.md"))
        paths = [p for p in paths if p.parent.name.endswith("-101") and p.parent.name != "llm-wait"]

    changed = []
    for path in paths:
        if path.parent.name == "llm-101":
            # Add a short pointer if missing
            text = path.read_text(encoding="utf-8")
            if FAMILY_LINK in text:
                print(f"skip {path.parent.name} (already linked)")
                continue
            addition = (
                "\n## *-101 Family\n\n"
                f"This is a concept lab in the *-101 set. Full family list: "
                f"**[learning-101]({FAMILY_LINK})**. "
                f"Site catalogue: [automica.io/learning-101]({SITE_LINK}).\n"
            )
            path.write_text(text.rstrip() + "\n" + addition, encoding="utf-8")
            changed.append(path.parent.name)
            print(f"append {path.parent.name}")
            continue

        text = path.read_text(encoding="utf-8")
        if "Catalogue: [automica.io/learning-101]" not in text:
            print(f"skip {path.parent.name} (no catalogue block)", file=sys.stderr)
            continue
        path.write_text(transform(text), encoding="utf-8")
        changed.append(path.parent.name)
        print(f"update {path.parent.name}")

    print(f"done: {len(changed)} repos")


if __name__ == "__main__":
    main()
