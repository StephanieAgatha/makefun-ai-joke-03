import os

joke = "My AI coding agent runs 24/7: 23 hours hallucinating APIs, one hour blaming 'outdated dependencies' for its own compile errors."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
entry_path = os.path.join(out_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8") as f:
    f.write(joke)
