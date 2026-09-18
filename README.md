# JARVIS Assistant

A Python prototype for Windows desktop automation. JARVIS takes a short command, separates the action from the target, locates matching executable files, and dispatches the requested system action.

> **Project status:** Prototype / learning project. It is intentionally kept as a versioned record of the design work and experiments behind a personal desktop assistant.

## Why I built it

I wanted to understand how a personal assistant could turn a plain-language request such as `open chrome` into a concrete system action. The project began as a hard-coded proof of concept and grew into a more general command pipeline.

## How it works

```text
User command
  -> command parser
  -> intent lookup
  -> target discovery
  -> dispatcher
  -> Windows system action
```

The current prototype uses a small command registry rather than an AI model. That makes the parsing logic visible and easy to reason about while the project explores the assistant architecture.

## Current capabilities

- Splits a command into an action and target, such as `open chrome`
- Maps supported verbs to application actions
- Searches common Windows locations and the Windows `PATH` for executable targets
- Handles zero, one, or multiple matching targets
- Launches a selected executable with Python's `subprocess` module
- Caches target-search results during a session

## Technology

- Python
- `pathlib` for path handling
- `subprocess` for launching programs
- `shutil.which` and `os.walk` for target discovery
- `functools.lru_cache` for session-level caching

## Run the prototype

This project has no third-party dependencies.

```powershell
python .\versions\v0.03\main.py
```

Windows is required because target discovery and launching are designed around Windows executable paths.

## Repository guide

- `versions/` contains the preserved prototypes and their progression.
- `versions/v0.03/main.py` is the latest runnable implementation in this repository.
- `core/` is reserved for a future modular refactor.
- `future_features.md` and `version_history.txt` document the next ideas and earlier iterations.

## Next directions

- Validate cached paths before using them
- Search selected drives or directories instead of always walking broad locations
- Improve handling of multiple targets and multi-application commands
- Move the prototype into the planned `core/` module structure
- Explore optional voice input only after the command pipeline is reliable

## Limitations

The current search strategy can be slow because it may walk large parts of a drive. It is a local learning prototype and should only be run on a machine where you understand the applications it may launch.
