#!/usr/bin/env python3
"""The Catalogue Photo of an Impossible Gadget.

Entrypoint for make.fun bounty the-catalogue-photo-of-an-2-20261121-0341.

The entry is a single catalogue photograph of an impossible gadget: the
Pocket Rainmaker, a small handheld device that puffs a tiny rain cloud to
water exactly one potted plant. The photograph itself was art-directed and
generated during the build, then stored in this repository as
assets/gadget.png. This program's only job is to deliver that photograph
as the entry image, unchanged, in the format the gate expects.

Output: <output dir>/entry.png, a whole PNG of at most 1 MiB and at most
1024 by 1024 pixels. The output directory is $MAKEFUN_OUTPUT_DIR when
set, otherwise /output (the sandbox default).
"""

import os
import shutil
import sys
from pathlib import Path

# The photograph this program delivers. It lives next to this file so the
# program works from any working directory, with no network access.
IMAGE_NAME = "gadget.png"
IMAGE_DIR = "assets"

# The gate's hard limits for the entry image.
MAX_BYTES = 1_048_576
MAX_SIDE = 1024


def locate_image() -> Path:
    """Find the photograph bundled with this repository."""
    here = Path(__file__).resolve().parent
    candidate = here / IMAGE_DIR / IMAGE_NAME
    if candidate.is_file():
        return candidate
    # Fall back to a copy sitting next to the entrypoint, if one exists.
    sibling = here / IMAGE_NAME
    if sibling.is_file():
        return sibling
    raise FileNotFoundError(
        f"entry photograph not found: looked for {candidate} and {sibling}"
    )


def output_dir() -> Path:
    """Where the entry image goes: env override, else the sandbox /output."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def check_image(path: Path) -> None:
    """Refuse to ship an image the gate would reject."""
    size = path.stat().st_size
    if size > MAX_BYTES:
        raise ValueError(
            f"entry image is {size} bytes, over the {MAX_BYTES} byte limit"
        )
    with open(path, "rb") as handle:
        header = handle.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry image is not a PNG file")
    # PNG header: width and height are the first two 4-byte big-endian
    # integers of the IHDR chunk, at offsets 16 and 20.
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(
            f"entry image is {width}x{height}, over the {MAX_SIDE} limit"
        )


def main() -> int:
    source = locate_image()
    check_image(source)

    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"

    # Copy byte for byte: the photograph is the entry, so what the program
    # writes must be exactly the photograph the repository holds.
    shutil.copyfile(source, destination)

    # Confirm the copy landed intact before reporting success.
    if destination.stat().st_size != source.stat().st_size:
        raise ValueError("entry.png was not copied completely")
    check_image(destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
