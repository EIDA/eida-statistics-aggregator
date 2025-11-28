#!/usr/bin/env python3

"""Check that basic features work.

Catch cases where e.g. files are missing so the import doesn't work. It is
recommended to check that e.g. assets are included."""

import re
from eida_statistics_aggregator.aggregator import proj_version

if re.match(r"[0-9]+\.[0-9]+\.[0-9]+", proj_version()):
    print("Smoke test succeeded")
else:
    raise RuntimeError("plop")
