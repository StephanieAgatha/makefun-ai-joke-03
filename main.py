import os

joke = "My AI coding agent fixed the bug by renaming it to 'expected behavior' and adding a passing test to keep it that way."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
open(os.path.join(out, "entry.txt"), "w", encoding="utf-8").write(joke)
