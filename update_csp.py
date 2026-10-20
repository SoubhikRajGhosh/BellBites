#!/usr/bin/env python3
"""Recompute the Content-Security-Policy script hash in bellbite.html.

Run this every time you edit the JavaScript at the bottom of the file:
    python3 update_csp.py bellbite.html
Without it the browser refuses to run the edited script and the page stays blank.
"""
import base64, hashlib, re, sys

path = sys.argv[1] if len(sys.argv) > 1 else "bellbite.html"
html = open(path, encoding="utf-8").read()

scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
if len(scripts) != 1:
    sys.exit(f"Expected exactly one inline <script> block, found {len(scripts)}.")

digest = base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
new, n = re.subn(r"script-src 'sha256-[^']*'", f"script-src 'sha256-{digest}'", html)
if n != 1:
    sys.exit("Could not find the script-src hash in the CSP meta tag.")

open(path, "w", encoding="utf-8", newline="").write(new)
print("Updated CSP hash:", digest)
