# Lab 11 - Eli Lilly sensitivity

Linda Li's individual lab, prepared with AI assistance. Numerical analysis is complete. Linda supplied her partner discussion, qualitative model check, reflection and recollection of a pre-run prediction. Remaining evidence gaps are listed below.

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

**Partner discussion, reported by Linda:** My partner asked how changing Eli Lilly's revenue growth assumption would affect the model. I explained that higher growth should increase projected revenue and earnings, ultimately increasing estimated value.

**Partner-model check, reported by Linda:** My partner also modeled Eli Lilly. Increasing revenue growth increased the valuation relative to the original base valuation, with all other independent inputs held fixed to isolate the growth effect. The exact growth paths, valuation amounts and units were not supplied, so a numerical difference cannot yet be documented. Linked statement amounts would still recalculate. This growth scenario belongs to the partner review; this repository's two tested drivers remain R&D and capex.

**Original prediction, recalled by Linda after the repository runs:** "Before running the scenario, I predicted that increasing Eli Lilly's revenue growth assumption would increase the company's projected valuation because higher future revenue would lead to stronger expected cash flows. I expected the valuation to increase noticeably while all other assumptions remained unchanged."

The reported growth result agrees with the predicted direction. A magnitude error cannot be calculated from "noticeably" and an unspecified valuation increase. No original timestamp or pre-run artifact was supplied, and this prediction concerns growth rather than the R&D/capex scenarios. It is recorded as Linda's account, not as a verified locked prediction for these runs.

**Remaining assignment evidence:** the partner's old/new growth values, affected years, base/changed valuations and units; an original timestamped prediction artifact if available; and the actual final partner discussion about range-dependent rankings. The current account does not establish a reconciled locked prediction for the repository's R&D/capex tests.

## Reflection - supplied and confirmed by Linda

I was surprised by how much changing just one assumption could affect the final valuation. It showed me how sensitive a financial model can be to its underlying assumptions. The README's reflection matched my conclusion because both emphasized the importance of understanding how individual assumptions drive model outputs.

Over these ranges, R&D is the main operating-profit driver, while capex is slightly larger for FCFE and value. The noteworthy result is that higher capex leaves operating profit unchanged but reduces cash flow. This reflects the model's fixed expense ratios and capitalization of investment, rather than proving that capital spending has no effect on future earnings. The analysis directs attention to whether Lilly can achieve the assumed growth with the tested R&D and capacity investment. These scenarios do not reverse the inherited valuation gap, but they show why spending and growth should be examined together in further research.

The first paragraph records Linda's supplied reflection; the explanatory paragraph is AI-assisted wording that Linda confirmed matches her conclusion.

## Worked result check - Linda's model

For higher R&D, FY2030 FCFE changes from $47,960.71 million to $45,349.75 million. Changed minus base is **-$2,610.96 million**. Independently, $163,185 million revenue times a 0.02 increase in R&D times (1 - 0.20 tax rate) gives the same $2,610.96 million reduction. The saved input sets confirm that only the R&D path changed; all accounting checks pass. This is a reproducible check of Linda's model, not a record of a check performed on her partner's model.

## Learn on your own

One-at-a-time sensitivity changes one independent assumption while holding others at base; linked statements recalculate. Wider ranges can produce larger spans, so rankings apply only over the stated ranges. A sensitivity table assigns no probabilities and is not a forecast probability distribution.

[Assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-06/lab-11-proforma-what-if.md). Submit individually; personal evidence above remains incomplete.
