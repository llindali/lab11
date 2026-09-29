# LLY sensitivity results

FY2030 operating profit and FCFE: USD millions. Value: USD/share.
Input paths run FY2026-2030. Deltas = scenario minus base.

| Input | Case | Actual path | Units | Profit | Change | FCFE | Change | Value | Change | Checks |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| RD | lower | [0.18, 0.18, 0.18, 0.18, 0.18] | fraction of revenue | 79,697.59 | +3,263.70 | 50,571.67 | +2,610.96 | 622.36 | +33.15 | PASS (all 5 years) |
| RD | base | [0.2, 0.2, 0.2, 0.2, 0.2] | fraction of revenue | 76,433.89 | +0.00 | 47,960.71 | +0.00 | 589.21 | +0.00 | PASS (all 5 years) |
| RD | higher | [0.22, 0.22, 0.22, 0.22, 0.22] | fraction of revenue | 73,170.19 | -3,263.70 | 45,349.75 | -2,610.96 | 556.07 | -33.15 | PASS (all 5 years) |
| CAPEX | lower | [0.11, 0.1, 0.09, 0.08, 0.07] | fraction of revenue | 76,433.89 | +0.00 | 50,621.75 | +2,661.04 | 623.85 | +34.63 | PASS (all 5 years) |
| CAPEX | base | [0.13, 0.12, 0.11, 0.1, 0.09] | fraction of revenue | 76,433.89 | +0.00 | 47,960.71 | +0.00 | 589.21 | +0.00 | PASS (all 5 years) |
| CAPEX | higher | [0.15, 0.14, 0.13, 0.12, 0.11] | fraction of revenue | 76,433.89 | +0.00 | 45,299.67 | -2,661.04 | 554.58 | -34.63 | PASS (all 5 years) |

## Output spans over these ranges

| Input | Profit span | FCFE span | Value span |
|---|---:|---:|---:|
| RD | 6,527.40 | 5,221.92 | 66.29 |
| CAPEX | 0.00 | 5,322.08 | 69.27 |

Restored base: PASS (exact equality). Accounting tolerance: $0.01 million.
Full input sets, statements and every check are retained in results.json.

RD range reason: Judgment agreed by Linda after checking with her partner: +/-2 percentage points around 20% in FY2026-2030 tests more intensive clinical spending versus revenue growing faster than research costs. This is not company guidance.

CAPEX range reason: Judgment agreed by Linda after checking with her partner: +/-2 percentage points from the FY2026-2030 base path tests continued capacity investment versus faster tapering as facilities enter operation. This is not company guidance.
