# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses semantic versioning where practical.

## [Unreleased]

### Added

- Repository layout with `data/`, `docs/`, `notebooks/`, `results/`, `src/` and `tests/`.
- Reproducible notebooks based on `rfmeasurement` and `scikit-rf`.
- README, contribution guide, citation metadata, license and automated quality gate.

### Changed

- Generated calibration artifacts moved to `results/`.
- Legacy notebooks moved to `notebooks/legacy/`.

### Fixed

- Notebook construction of `rfmeasurement.Measurement` now matches the installed public API.

[Unreleased]: https://github.com/telmomm/nanovna-calibration/compare/v0.1.0...HEAD
