# Deep Thought Dispenser

A small web app that returns random deep-thought-style monologues inspired by surreal one-liners and dad jokes.

The generator builds thoughts from modular phrase pools, giving **well over 1,000 possible unique thoughts**.

## Run from Python

```bash
python app.py
```

Then open `http://localhost:8000`.

## Build a Windows `.exe`

From **Windows Command Prompt** in this project folder:

```bat
build_exe.bat
```

This creates:

- `dist\DeepThoughtDispenser.exe`

Run the EXE, then open `http://localhost:8000` in your browser.

## API

- `GET /api/deep-thought` → JSON response:

```json
{ "thought": "If a lawn chair hosted a podcast, we'd all pretend to understand it in meetings and that's probably why Tuesdays feel personal." }
```
