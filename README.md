# Lab 11 - Eli Lilly sensitivity

Linda Li's individual lab, prepared with AI assistance. Numerical analysis is complete. Linda supplied her partner discussion, numerical model-check account, reflection and reconstructed prediction record. Evidence limitations are listed below.

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

**Partner discussion, reported by Linda:** My partner asked how changing Eli Lilly's revenue growth assumption would affect the model. I answered that increasing the growth assumption should increase projected revenue and cash flows, resulting in a higher estimated valuation.

**Partner-model check, reported by Linda:** My partner also modeled Eli Lilly. The base revenue growth assumption was 8%, producing an estimated valuation of approximately $710 billion. Increasing growth to 10% increased estimated valuation to approximately $765 billion. All other independent inputs were held fixed to isolate growth; linked statement amounts still recalculate.

The growth change is **+2 percentage points**, or a 25% relative increase in the growth rate. Using the reported approximate valuations, changed minus base is **+$55 billion**, or approximately **+7.75%** ($55 / $710). This arithmetic verifies the reported difference; the partner's underlying model was not supplied or independently rerun. The affected forecast years and whether the reported total is equity or enterprise value were not specified. This partner scenario is separate from the repository's R&D and capex tests; its values are not outputs from this repository.

**Pre-run prediction, reported retrospectively by Linda:** "Before running the scenario, I predicted that increasing Eli Lilly's revenue growth assumption would increase its projected valuation because higher expected revenue would lead to stronger future cash flows. I also predicted that Eli Lilly could move higher in the company rankings under a more optimistic growth scenario."

**Timestamp / Git evidence:** No timestamped pre-run prediction or Git commit was saved. The earlier range-setup commit contains the agreed inputs, not a saved prediction. The current documentation commit is not pre-run evidence.

**Comparison with actual result:** The reported increase from approximately $710 billion to $765 billion is consistent with the predicted direction: higher assumed growth produced a higher valuation in the partner's scenario. No numerical predicted magnitude was supplied, so magnitude error cannot be calculated. No before/after company rankings were supplied, so the ranking prediction cannot be checked. This growth account does not reconcile a locked prediction for the repository's R&D/capex scenarios.

**Final partner discussion, reported by Linda:** We discussed how selected ranges can affect company rankings. We concluded that companies given wider or more optimistic growth ranges could show larger valuation increases and potentially rank higher, while more conservative ranges could produce lower valuations. Rankings therefore depend partly on the ranges and assumptions selected, making reasonable and comparable ranges important.

**Clarification for this lab:** The requested ranking compares drivers within a model by output span, not companies by raw valuation. A wider tested range can make a driver rank higher by increasing its span; widening a range does not necessarily increase the base valuation. Here, capex ranks slightly above R&D for FCFE and value over the stated ranges. Both partners modeled Lilly, so the review does not support a comparison between different companies.

**Evidence limitations:** No locked pre-run prediction was saved for the R&D/capex tests. The reported final discussion concerns company rankings; a partner question/response about the R&D/capex driver ranking has not been supplied. For reproducibility, the partner's affected years and equity-versus-enterprise value basis are also unspecified, although these are not separate required fields for the partner-review notes.

## Reflection - supplied and confirmed by Linda

I was surprised by how much a relatively small change in the growth assumption affected the final valuation. It showed me how sensitive valuation models can be to their underlying assumptions. The README's reflection matched my conclusion because both emphasized that model outputs depend heavily on the assumptions and ranges selected.

Over these ranges, R&D is the main operating-profit driver, while capex is slightly larger for FCFE and value. The noteworthy result is that higher capex leaves operating profit unchanged but reduces cash flow. This reflects the model's fixed expense ratios and capitalization of investment, rather than proving that capital spending has no effect on future earnings. The analysis directs attention to whether Lilly can achieve the assumed growth with the tested R&D and capacity investment. These scenarios do not reverse the inherited valuation gap, but they show why spending and growth should be examined together in further research.

The first paragraph records Linda's supplied reflection; the explanatory paragraph is AI-assisted wording that Linda confirmed matches her conclusion.

## Worked result check - Linda's model

For higher R&D, FY2030 FCFE changes from $47,960.71 million to $45,349.75 million. Changed minus base is **-$2,610.96 million**. Independently, $163,185 million revenue times a 0.02 increase in R&D times (1 - 0.20 tax rate) gives the same $2,610.96 million reduction. The saved input sets confirm that only the R&D path changed; all accounting checks pass. This is a reproducible check of Linda's model, not a record of a check performed on her partner's model.

## Learn on your own

One-at-a-time sensitivity changes one independent assumption while holding others at base; linked statements recalculate. Wider ranges can produce larger spans, so rankings apply only over the stated ranges. A sensitivity table assigns no probabilities and is not a forecast probability distribution.

[Assignment](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-06/lab-11-proforma-what-if.md). Individual submission; evidence limitations are disclosed above.
