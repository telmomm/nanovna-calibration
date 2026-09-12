# Methodology

## Acquisition

S11 and S21 sweeps are acquired from the NanoVNA on a common frequency grid. Each repetition is stored as Touchstone and wrapped in an `rfmeasurement.Measurement` with instrument, range, and declared calibration metadata.

## SOL

At each frequency, the one-port model is solved:

`Gamma_m = (e_d + e_r Gamma_std) / (1 - e_s Gamma_std)`

using `open = 1`, `short = -1`, and `load = 0`. Repetitions are averaged and their standard deviation is retained as repeatability evidence.

## Validation

`rfmeasurement` distinguishes data integrity, signal quality, and physical assumptions. A measurement can be structurally valid while failing passivity because of noise or applied correction. Therefore, the pipeline does not automatically discard a measurement because of a physical-rule failure.

## Correction

The inversion used is:

`Gamma = (Gamma_m - e_d) / (e_r + e_s Gamma_m)`

The terms used and generated outputs must be preserved together with the environment version.
