#!/usr/bin/env python

import os
import re
import sys

QUIP_BASE_URL = "https://quip.orchard.apple.com/"

QUIP_SLUG_REGEX = re.compile(".*%s([^\s]*)" % QUIP_BASE_URL)

EXCLUDE_SLUGS = [
    "account/email",
]

for line in sys.stdin.readlines():
    match = re.match(QUIP_SLUG_REGEX, line)
    if match:
        slug = match.group(1)
        if slug in EXCLUDE_SLUGS:
            continue
        if slug[-1] == ">":
            slug = slug[0:-1]
        os.system("open quip://%s" % slug)
