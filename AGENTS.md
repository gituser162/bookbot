# AGENTS.md

BookBot: a small Python CLI that analyzes a text file (word count, top 10 words, per-letter counts).

## Layout
- `main.py` – entry point; parses args and prints the report
- `stats.py` – counting/sorting helpers
- `books/` – sample texts (Frankenstein, Moby Dick, Pride and Prejudice)

## Run
```
python3 main.py books/frankenstein.txt
```

## Conventions
- Python 3, standard library only; no dependencies or test suite yet.
- Keep analysis logic in `stats.py`, CLI/printing in `main.py`.
- Don't commit `__pycache__/`.
