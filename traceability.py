#!/usr/bin/env python3
"""
Compatibility entrypoint for local usage.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from tracetree.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
