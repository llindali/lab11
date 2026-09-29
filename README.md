# Lab 11 — Eli Lilly sensitivity

Linda Li's individual lab, prepared with AI assistance. **Status: waiting for student ranges, locked prediction and partner evidence; changed scenarios have not been run.**

Question: Which assumptions drive my company's forecast and value, and what explains their effects?

## Run

Python 3; no packages required.

```sh
python proforma_lly.py
python sensitivity.py
```

The existing [Lab 10 model and assumptions](https://github.com/llindali/lab10) are the source. `proforma_lly.py` and `history.json` are copied unchanged. `base_output.txt` saves the initial statements and checks. The inherited annual teaching valuation uses a December 2025 discount origin and fixed shares; it is not a current market valuation. Source data have not been refreshed for this sensitivity exercise.

## Required inputs

Fill `scenarios.json` with two driver objects, each containing `input`, `lower`, `higher`, `units`, and `reason`. Lower/higher paths each contain five numbers for FY2026–2030. Base paths come directly from Lab 10. Available inputs: `GROWTH`, `MARGIN`, `SGA_GP`, `RD`, `IPRD`, `CAPEX`, `DAYS`. Ratios are decimals (0.20 means 20%); IPRD uses USD millions and DAYS uses days. A one-percentage-point increase means adding 0.01 to a ratio, not multiplying it by 1.01.

Before changed runs, write your own prediction with AI closed: input old → new, units, output direction and rough size, and reason. Save the text and UTC timestamp in `prediction`, then commit before running. Set `partner_checked_before_run` to true only after your partner actually checks your prediction, ranges and one-input-at-a-time setup.

The runner loads a fresh model for each case, changes one input, reruns all five years, retains signed FCFE, validates all accounting checks, and restores the base exactly. It produces `results.md` (visible table, signed differences and spans) and `results.json` (all inputs, statements and checks). Invalid runs are flagged and excluded from spans. Value is unavailable if accounting fails, terminal valuation fails, or negative explicit FCFE would be omitted by the inherited valuation method.

## Student completion record — pending

- Locked prediction and pre-run partner check: pending.
- Actual result versus prediction, explanation of error, and effect on valuation conclusion or research priority: pending results and Linda's interpretation.
- Main driver for each output **over these ranges**, causal statement link, surprising result and reflection: pending Linda's explanation.
- Partner exchange 1: prediction/range question received and response — pending.
- Partner exchange 2: result checked on partner's model, recomputed difference, unchanged assumptions and question/correction — pending.
- Partner exchange 3: causal-link question and response, range limitation and comparison of companies — pending.

One-at-a-time sensitivity changes one independent assumption while holding the others at base; linked statement amounts recalculate. Wider tested ranges can produce larger spans, so rankings depend on ranges. A sensitivity table assigns no scenario probabilities.

[Assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-06/lab-11-proforma-what-if.md). Submit individually once pending evidence is completed.
