#!/usr/bin/env python3
"""Write the pigeon pitch line to entry.txt.

Competition: Pigeon Pitch, One Line (one line, 1-200 chars, English:
the elevator pitch a city pigeon gives investors for its startup;
the brief rewards, in order, being on subject, a real joke that
lands, originality, the pigeon's own voice and city life, and
tight writing).
Candidates:
A) "Forget drones: my flock is 10,000 couriers who already work
   for breadcrumbs, know every rooftop shortcut in the city, and
   have never once asked for parking - fund Coo-rier and we
   deliver by lunch." (with an em dash before 'fund')
B) "I'm raising a seed round - literally: fund Crumb, my
   pigeon-run courier fleet, and we'll deliver anything under a
   sandwich across downtown before the lunch crowd looks up."
C) "Statues are just billboards we already sit on: fund Peck,
   the only ad network with prime placement on every monument
   in the city, paid entirely in yesterday's bagels."
D) "I poop on luxury cars for free; imagine what my flock
   could do to your competitors' for a modest seed investment
   and unlimited access to the good breadcrumbs."
Selected A: it is unmistakably a pitch to investors (fund us,
we deliver), its couriers could only be pigeons (breadcrumbs,
rooftop shortcuts, no parking), and the drone comparison gives
it a real startup logic under the joke. B's seed-round pun is
good but narrower; C is a neat ad idea with no delivery payoff;
D leads with a crude joke and a vaguer business.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Forget drones: my flock is 10,000 couriers who already work for breadcrumbs, know every rooftop shortcut in the city, and have never once asked for parking \u2014 fund Coo-rier and we deliver by lunch."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # Revision: enforce exactly one clean line within the gate
    # limit, so the printed entry is exactly the selected text.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    # Write bytes directly so the entry is identical on every run.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
