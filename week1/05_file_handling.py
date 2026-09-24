"""Exercise 5 - Reading/writing text, CSV and JSON files."""
import csv, json, os, tempfile
from collections import Counter

workdir = tempfile.mkdtemp()
path = lambda f: os.path.join(workdir, f)

# --- Text: write, append, read ---
with open(path("notes.txt"), "w", encoding="utf-8") as f:
    f.write("Python is simple.\nPython is powerful.\n")
with open(path("notes.txt"), "a", encoding="utf-8") as f:
    f.write("Files are easy with context managers.\n")
with open(path("notes.txt"), encoding="utf-8") as f:
    lines = f.read().splitlines()
print(len(lines), "lines |", lines[0])

# --- Word frequency ---
words = [w.strip(".,").lower() for line in lines for w in line.split()]
print(Counter(words).most_common(3))

# --- CSV: write + read + compute ---
rows = [{"name": "Sara", "score": 17}, {"name": "Ali", "score": 12}, {"name": "Nour", "score": 15}]
with open(path("scores.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "score"])
    w.writeheader(); w.writerows(rows)
with open(path("scores.csv"), newline="", encoding="utf-8") as f:
    data = list(csv.DictReader(f))
best = max(data, key=lambda r: int(r["score"]))
print("Top student:", best["name"], "| mean:", sum(int(r["score"]) for r in data) / len(data))

# --- JSON: dump + load ---
config = {"model": "CNN", "epochs": 10, "layers": [32, 64]}
with open(path("config.json"), "w") as f:
    json.dump(config, f, indent=2)
with open(path("config.json")) as f:
    print(json.load(f))
