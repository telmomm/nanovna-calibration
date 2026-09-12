# Repository Organization

The organization follows the principle of separating data, code, reproducible experiments, results, and documentation.

- `data/`: original measurement data and Touchstone files.
- `src/nanovna_calibration/`: reusable Python code.
- `notebooks/`: numbered executable workflow.
- `notebooks/legacy/`: historical notebooks retained for reference.
- `results/`: generated results such as SOL terms and plots.
- `tests/`: structure, syntax, and lightweight regression tests.
- `docs/`: methodology, quality, and project decisions.

Original data must not be mixed with generated results, and absolute paths must be avoided. The notebooks resolve the project root when run from `notebooks/`.
