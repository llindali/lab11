# Lab 11 - Eli Lilly sensitivity

Linda Li's individual lab, prepared with AI assistance. Linda confirmed agreement with her partner on the proposed setup and authorized the runs. Numerical analysis is complete; the independent prediction and detailed partner evidence were not supplied.

**Question:** Which assumptions drive my company's forecast and value, and what explains their effects?

## Run and evidence

Python 3; no packages required: `python sensitivity.py`.

- [Results table](results.md): input paths, outputs, signed changes and spans.
- [Full evidence](results.json): all inputs, five-year statements and accounting checks.
- [Agreed assumptions](scenarios.json): ranges, units, reasons and partner agreement.
- [Initial base output](base_output.txt): original statements and checks.
- [Model](proforma_lly.py) and [history](history.json): unchanged from [Lab 10](https://github.com/llindali/lab10), which documents sources and assumptions.

Each run loads a fresh independent model, changes one input path and recalculates all linked statements. Other independent inputs are checked against base. All six cases pass every accounting check in all five years at a $0.01 million tolerance. Restored base matches initial base exactly. Independent arithmetic verifies the R&D profit and after-tax FCFE changes. Signed negative cash flows are retained; if the inherited valuation would omit one, value is marked unavailable.

## Agreed ranges

Paths cover FY2026-2030. Values are percentages of revenue.

| Driver | Lower | Base | Higher |
|---|---|---|---|
| R&D | 18%, 18%, 18%, 18%, 18% | 20%, 20%, 20%, 20%, 20% | 22%, 22%, 22%, 22%, 22% |
| Capex | 11%, 10%, 9%, 8%, 7% | 13%, 12%, 11%, 10%, 9% | 15%, 14%, 13%, 12%, 11% |

Both shift each year by two percentage points from base, not 2% of the base ratio. These are agreed judgments, not guidance. R&D tests heavier clinical investment versus revenue outgrowing research costs. Capex tests prolonged capacity investment versus faster tapering as facilities enter operation. The ranges were committed before running sensitivity.

## Findings - AI-assisted explanation for Linda's review

**Over these ranges, R&D drives operating profit more, while capex has a slightly larger effect on FCFE and value.** Spans use unrounded maximum minus minimum outputs.

| Driver | FY2030 profit span, USD millions | FY2030 FCFE span, USD millions | Value span, USD/share |
|---|---:|---:|---:|
| R&D | 6,527.40 | 5,221.92 | 66.29 |
| Capex | 0.00 | 5,322.08 | 69.27 |

Raising R&D from 20% to 22% lowers FY2030 operating profit by $3,263.70 million: revenue of $163,185 million times 0.02. At the 20% tax rate, net income and FCFE fall $2,610.96 million. Revenue and working-capital assumptions stay fixed; the expense flows through earnings, CFO, cash and equity. Value falls from $589.21 to $556.07 per share.

Raising capex by two percentage points increases FY2030 investment $3,263.70 million. Earlier extra spending raises PP&E and FY2030 depreciation added back to CFO by $602.66 million. FCFE therefore falls $2,661.04 million, and value falls to $554.58 per share. Operating profit stays fixed because the inherited expense ratios already include depreciation and remain unchanged. This is a modeling simplification, not evidence that investment has no eventual earnings effect.

Lower spending does not reduce modeled revenue, pipeline success or capacity. Higher calculated value from spending less therefore does not establish that cuts improve the business. Equal percentage-point ranges have different economics; changing their widths could change the ranking.

Tested values range from $554.58 to $623.85 per share. None reverses the gap against Lab 10's dated $1,188.87 market observation. This is an inherited teaching-model comparison, not a refreshed market conclusion. The valuation uses a December 2025 discount origin, fixed shares and substantial terminal value. A useful research priority is whether the sales path can be achieved with the tested investment levels.

## Personal and partner evidence

**Confirmed:** Linda reported, "i just checked with my partner and we agree can you proceed" after the proposed ranges and practice questions. This records agreement, not a verbatim partner discussion.

**Not supplied:** an independently written, timestamped pre-run prediction. No prediction was backdated or reconstructed after seeing results; prediction-error reconciliation remains unavailable. The pre-run range commit does not substitute for that requirement.

**Still needed:** the actual partner question and response; the difference Linda recomputed on her partner's model and unchanged-input check; and the final causal-link/range discussion. Practice questions are examples, not evidence of completed exchanges. Linda's own reflection on what surprised her and her conclusion also remain to be recorded.

## Learn on your own

One-at-a-time sensitivity changes one independent assumption while holding others at base; linked statements recalculate. Wider ranges can produce larger spans, so rankings apply only over the stated ranges. A sensitivity table assigns no probabilities and is not a forecast probability distribution.

[Assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-06/lab-11-proforma-what-if.md). Submit individually; personal evidence above remains incomplete.
