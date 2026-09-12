# NanoVNA Calibration

Reproducible analysis of S-parameter measurements acquired with a NanoVNA. The workflow uses `scikit-rf` to represent and serialize Touchstone networks, and `rfmeasurement` for context, validation, and traceability.

[![Quality gate](https://github.com/telmomm/nanovna-calibration/actions/workflows/quality.yml/badge.svg)](https://github.com/telmomm/nanovna-calibration/actions/workflows/quality.yml)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-2ea44f)](https://telmomm.github.io/nanovna-calibration/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22722703.svg)](https://doi.org/10.5281/zenodo.22722703)

The project documentation is published at [telmomm.github.io/nanovna-calibration](https://telmomm.github.io/nanovna-calibration/). It is built from `docs/` with MkDocs and deployed by [`.github/workflows/pages.yml`](.github/workflows/pages.yml).

## Goals

- Acquire repeated `open`, `short`, and `load` measurements.
- Estimate one-port SOL error terms.
- Apply the correction to device-under-test measurements.
- Preserve data, results, and notebooks reproducibly.
- Record integrity and quality validation with `rfmeasurement`.

`rfmeasurement` does not replace `scikit-rf`: version 0.1.0 does not yet include a Touchstone adapter or a SOL implementation. This repository keeps those parts in the local workflow and uses `rfmeasurement` for the scientific model and validation.

## Structure

```text
.
├── data/                 # Touchstone measurements and experimental datasets
├── docs/                 # Methodology and project organization
├── notebooks/            # Numbered main workflow
│   └── legacy/           # Historical notebooks
├── results/              # NPZ files, plots, and generated outputs
├── src/nanovna_calibration/ # Reusable project utilities
├── tests/                # Automated quality gate
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── README.md
└── pyproject.toml
```

## Workflow

1. Run `notebooks/00_configuracion_rfmeasurement.ipynb`.
2. Run `notebooks/01_adquisicion_nanovna_rfmeasurement.ipynb` for each standard.
3. Run `notebooks/02_calibracion_sol_rfmeasurement.ipynb`.
4. Run `notebooks/03_analisis_medidas_rfmeasurement.ipynb`.

The acquisition notebook requires a connected NanoVNA. Set `PORT` when multiple interfaces are present or automatic detection is insufficient.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

To run notebooks, select the `.venv` interpreter in VS Code.

## Quality Gate

The quality gate runs on every push and pull request through GitHub Actions:

```bash
python -m pytest
python -m ruff check src tests
python -m compileall src tests
```

In addition, `tests/test_repository.py` checks that notebooks are valid JSON, that every cell declares `metadata.language`, and that Python cells are syntactically valid. Scientific results are not considered correct merely because the code runs: they must be interpreted together with the `rfmeasurement` validation report.

Failures of physical rules, such as passivity, are retained as experimental evidence and are not automatically treated as data-integrity failures.

## Data and Reproducibility

Data is stored in Touchstone format. Generated files are written to `results/`. Virtual environments, caches, and temporary plots are not versioned.

The notebooks record the instrument, frequency range, declared calibration, and DUT identifier in `MeasurementContext`.

## Citation

Cite this repository using `CITATION.cff`. The workflow uses `rfmeasurement`; cite that dependency using its [CITATION.cff](https://github.com/telmomm/rfmeasurement/blob/main/CITATION.cff) and its concept DOI [10.5281/zenodo.22058515](https://doi.org/10.5281/zenodo.22058515):

> Miguel-Medina, T. (2026). *rfmeasurement: an open-source framework for uncertainty-aware validation and reproducible analysis of RF measurements*. Version 0.1.0. https://doi.org/10.5281/zenodo.22058515

## License

This repository is distributed under BSD-3-Clause. See [LICENSE](LICENSE).
