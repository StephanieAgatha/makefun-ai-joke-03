import os

joke = "My AI coding agent works 24/7: 23 hours hallucinating APIs, one hour blaming 'outdated dependencies' for its own compile errors."

out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(joke)
