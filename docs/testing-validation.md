# Testing and Validation

The quality gate verifies software; `rfmeasurement` validation provides scientific evidence for each measurement.

## Automated Checks

```bash
python -m pytest
python -m ruff check src tests
python -m compileall src tests
```

## Interpretation

- Structural integrity, finite values, and frequency grid: blocking failures.
- Continuity and dynamic range: warnings that require review.
- Passivity and reciprocity: physical results that must be interpreted in the context of the instrument, noise, and calibration.

Validation output is not reduced to a boolean. The notebooks print the rule, status, and explanation to preserve the evidence.
