# Contributing

Thank you for contributing to NanoVNA Calibration.

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Before Opening a Pull Request

1. Explain the motivation and scope of the change.
2. Keep the change focused on one concern.
3. Add or update tests and documentation.
4. Update `CHANGELOG.md` when the change is user-visible.
5. Document measurement assumptions, calibration, and units.
6. Run the local quality gate.

## Scientific Changes

Calibration or uncertainty algorithms must include the equation, references, assumptions, validity limits, and an independent verification strategy.

## Style

Python code is organized under `src/`. Measurements remain in `data/` and generated results in `results/`. Do not include credentials, virtual environments, or temporary artifacts.

## Verification

```bash
python -m pytest
python -m ruff check src tests
python -m compileall src tests
```
