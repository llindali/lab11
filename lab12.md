# Lab 12 — Eli Lilly Full Analysis and Review

**Student:** Linda Li

**Company:** Eli Lilly and Company (NYSE: LLY)

## Full Analysis

### 1. Target Selection

I selected Eli Lilly because its valuation is highly dependent on future revenue growth, R&D investment, and manufacturing capacity. These characteristics make Lilly a useful company for pro-forma and sensitivity analysis because relatively small changes in operating assumptions can meaningfully affect future cash flows and valuation.

My initial view was that Lilly's expected growth could support significant future cash flow, but its valuation would depend on whether that growth could be maintained while the company continues investing heavily in drug development and manufacturing capacity.

### 2. Company and Evidence

Eli Lilly generates revenue primarily through the development and sale of pharmaceutical products. Because future products and production capacity are important to the business, R&D and capital expenditures are particularly important assumptions in my model.

My historical analysis uses FY2023-FY2025 filing information and traces revenue, gross profit, SG&A, income, inventory, PP&E, equity, and other inputs to company filings.

My FY2026 forecast uses **\$86.0 billion of revenue**, representing the midpoint of Lilly's \$85-\$87 billion August 2026 guidance range. After 2026, my forecast assumes revenue growth of 25% in 2027, 20% in 2028, 15% in 2029, and 10% in 2030. These later growth rates are my scenario assumptions rather than management guidance.

Recurring R&D is modeled at **20% of revenue**, close to Lilly's FY2025 R&D level of approximately 20.46% of revenue. Capex begins at 13% of revenue in 2026 and gradually declines to 9% by 2030 as I assume manufacturing expansion eventually begins to taper.

### 3. Pro-Forma

My pro-forma covers FY2026-FY2030.

Revenue grows from **\$86.0 billion in 2026 to \$163.185 billion in 2030**.

Recurring R&D grows from **\$17.2 billion to \$32.637 billion**.

Net income increases from approximately **\$26.284 billion to \$58.807 billion**.

FCFE increases from approximately **\$17.951 billion to \$47.961 billion**.

The statements are linked. Earnings affect cash flow and equity, working-capital changes affect operating cash flow, capex affects investing cash flow and PP&E, and borrowing affects cash and debt.

Cash is not used as a plug. Ending cash equals opening cash plus operating, investing, and financing cash flows.

All five forecast years balance with:

**Assets − Liabilities − Equity = 0**

The base case remains above the \$5 billion minimum cash requirement and requires no revolver draw.

### 4. Valuation

I use FCFE to value Lilly.

FCFE is calculated as operating cash flow plus investing cash flow plus net borrowing before shareholder distributions.

The model discounts the five explicit forecast years at **10%** and uses a **2.5% perpetual growth rate**.

The resulting valuation is:

- PV of explicit FCFE: **\$117.321 billion**
- PV of terminal cash flows: **\$406.991 billion**
- Opening excess cash: **\$2.268 billion**
- Total modeled equity value: **\$526.580 billion**
- Diluted share proxy: **893.7 million shares**
- **Modeled value per share: \$589.21**

The market observation used in the project was **\$1,188.87 per share on September 24, 2026**.

I would not interpret this difference as proof that the market is incorrectly pricing Lilly. Instead, the market could be incorporating stronger expectations for future growth, research productivity, manufacturing expansion, or other factors not fully captured by my simplified model.

A major limitation is that **77.29% of modeled value comes from terminal value**, making the result particularly dependent on long-term assumptions.

There is also a timing limitation. The course model discounts annual forecasts to December 31, 2025 while incorporating information available during 2026, whereas the market observation is from September 24, 2026.

### 5. Sensitivity and Drivers

For Lab 11, I tested **R&D and capital expenditures**.

#### R&D

Base R&D is 20% of revenue.

I tested:

- Lower: 18%
- Base: 20%
- Higher: 22%

Across this range:

- FY2030 operating-profit span = **\$6.527 billion**
- FY2030 FCFE span = **\$5.222 billion**
- Value span = **\$66.29/share**

Increasing R&D from 20% to 22% reduces FY2030 operating profit by approximately **\$3.264 billion**.

After the modeled 20% tax rate, net income and FCFE decline by approximately **\$2.611 billion**.

The causal relationship is:

**Higher R&D → higher operating expense → lower operating profit → lower net income → lower operating cash flow/FCFE → lower valuation**

The modeled value falls from **\$589.21 to \$556.07 per share**.

#### Capex

Base capex declines from 13% of revenue in 2026 to 9% in 2030.

I tested two percentage points above and below that base path.

Across this range:

- FY2030 operating-profit span = **\$0**
- FY2030 FCFE span = **\$5.322 billion**
- Value span = **\$69.27/share**

Increasing capex by two percentage points increases FY2030 investment by approximately **\$3.264 billion**.

The causal relationship is:

**Higher capex → greater investing cash outflow → lower FCFE → lower valuation**

The higher-capex scenario reduces modeled value from **\$589.21 to \$554.58 per share**.

### 6. Sensitivity Interpretation

Over the ranges tested, **R&D has the larger effect on operating profit while capex has the slightly larger effect on FCFE and valuation**.

This does not prove that capex is inherently more important than R&D.

Both variables were tested over selected two-percentage-point ranges. Different ranges could change their ranking.

More importantly, the model does not reduce future revenue when R&D or capex decreases. Lower investment therefore mechanically increases valuation even though, in reality, reducing research or manufacturing investment could hurt Lilly's future pipeline, capacity, and sales.

The sensitivity analysis identifies **model exposure**, not the probability of a scenario or evidence that Lilly should reduce investment.

---

## Partner Review

### As Presenter

#### Question Received

**Question:** If Lilly needs substantial R&D and manufacturing investment to achieve your projected revenue growth, are revenue growth, R&D, and capex really independent assumptions?

#### My Answer

Not completely in economic reality.

My current model treats them as independently adjustable assumptions so that I can isolate their effects. However, Lilly's ability to achieve my projected revenue growth may depend on continued R&D spending to develop successful products and continued capex to create enough manufacturing capacity.

That means reducing R&D or capex mechanically improves FCFE in my model while leaving revenue unchanged, but that relationship may not hold in the actual business.

This is an important limitation of the sensitivity analysis.

#### Follow-Up Question

**Question:** Why does your model produce only \$589.21 per share when the market observation is \$1,188.87?

#### My Answer

I would not conclude that the difference means the market is wrong.

My model contains relatively conservative and simplified assumptions, including declining revenue growth, a 10% discount rate, a 2.5% terminal growth rate, and simplified relationships between investment and future sales.

The market could be incorporating stronger long-term revenue growth, greater research productivity, future pipeline success, manufacturing expansion, or other expectations that my model does not capture.

Additionally, 77.29% of my modeled value comes from terminal value, so assumptions about long-term performance have a large effect on the result.

---

### As Reviewer

#### Selection and Evidence Question

**Question:** Why was Eli Lilly appropriate for this analysis, and what evidence supports using 20% of revenue for recurring R&D?

**Check:** I reviewed the assumption against the historical information in the analysis.

Lilly's FY2025 R&D was approximately **20.46% of revenue**, while the forecast uses **20% of revenue**.

**Result:** The evidence supports using 20% as a reasonable historical anchor for the scenario. It is still a forecast assumption rather than a claim that future R&D must remain exactly 20%.

#### Model and Valuation Question

**Question:** Can you trace exactly how increasing R&D reaches the final valuation rather than simply saying that higher R&D lowers value?

**Calculation checked:**

Base R&D = **20% of revenue**

Changed R&D = **22% of revenue**

FY2030 revenue = **\$163.185 billion**

Difference:

**\$163.185B × 2% = \$3.2637B**

Therefore, the additional R&D reduces FY2030 operating profit by approximately **\$3.264 billion**.

With the model's 20% tax rate:

**\$3.2637B × (1 − 20%) = \$2.611B**

Net income and FCFE therefore decline by approximately **\$2.611 billion**.

The resulting modeled share value decreases:

**Base: \$589.21/share**

**Higher R&D: \$556.07/share**

Other independent inputs remain fixed while the linked financial statements recalculate.

**Result of check:** The calculation supports the claim. The R&D assumption reaches valuation through operating expense, operating profit, net income, cash flow, FCFE, and finally discounted equity value.

#### Sensitivity and Interpretation Question

**Question:** Since capex produced the largest valuation span, can you conclude that capex is Lilly's most important valuation driver?

**Answer:** No.

Capex produced a **\$69.27/share** valuation span compared with **\$66.29/share** for R&D, but this ranking applies only to the ranges tested.

Both were moved by two percentage points, and equal percentage-point movements do not necessarily represent equal economic uncertainty.

Changing the ranges could change the ranking.

Additionally, the model does not allow reduced R&D or capex to reduce future revenue. Therefore, the sensitivity results should not be interpreted as evidence that reducing investment would improve Lilly's actual economic value.

---

### Reviewer Explanation Back

#### Valuation Conclusion

Linda's base-case model produces an estimated value of **\$589.21 per share**.

The model therefore produces a substantially lower value than the dated market observation of \$1,188.87, but the difference should be interpreted as a difference between the assumptions embedded in the model and expectations reflected in the market rather than automatically concluding that the stock is incorrectly priced.

#### Main Driver

Within the Lab 11 sensitivity ranges, **capex produces the slightly larger FCFE and valuation span**, while **R&D produces the larger operating-profit effect**.

However, the ranking is conditional on the ranges selected.

#### Biggest Limitation

The biggest limitation is that **R&D, capex, and revenue growth are treated as independently adjustable assumptions even though they are economically connected**.

Reducing R&D or capex increases modeled FCFE without reducing future revenue, pipeline success, or manufacturing capacity.

The model can therefore measure the direct cash-flow effect of investment but does not fully capture the potential long-term benefit of that investment.

---

### Evidence-Backed Strength

A major strength of the analysis is that the sensitivity results are traced through the actual financial statements rather than simply reporting that a variable changes valuation.

For R&D, the analysis demonstrates:

**R&D → operating expense → operating profit → net income → CFO/FCFE → valuation**

For capex, it demonstrates:

**Capex → investing cash flow/PP&E → FCFE → valuation**

The analysis also appropriately qualifies the sensitivity ranking rather than interpreting it as a probability or business recommendation.

---

### Specific Improvement

The strongest next improvement would be to add a scenario that connects **revenue growth with R&D and manufacturing investment**.

For example, a lower-investment scenario could also assume lower future revenue growth rather than allowing Lilly to receive the same sales while spending less.

This would make the model better reflect the economic tradeoff between current investment and future growth.

---

## Keep, Revise, Investigate

### Keep

I will keep:

- The linked three-statement model.
- The FCFE valuation framework.
- The declining long-term revenue-growth assumptions.
- The R&D and capex sensitivity analysis.
- The explicit distinction between model sensitivity and probability.

These components provide a traceable path from assumptions through the statements to valuation.

### Revise

I will revise my interpretation of the spending sensitivities to emphasize that lower R&D or capex producing higher valuation does **not** mean Lilly should reduce those investments.

The result occurs partly because the model holds future revenue constant when investment changes.

### Investigate

The next issue I would investigate is whether my projected sales growth can realistically be achieved with the assumed R&D and manufacturing investment.

Specifically, I would investigate the relationship among:

**R&D investment → pipeline/product success → revenue growth**

and

**Manufacturing capex → production capacity → achievable sales**

This is more important than simply testing progressively wider spending ranges.

### Effect on My Conclusion

The review does **not change my \$589.21 base-case valuation**, because I have not changed an assumption and rerun the model.

It does change my **research priority and interpretation**.

I now view the \$589.21 result as more clearly conditional on the model's assumption that the projected revenue path can be achieved with the specified R&D and capex levels.

---

## Reflection

The question that made me reconsider my analysis was:

**If Lilly needs R&D and manufacturing investment to generate its projected revenue growth, are those assumptions really independent?**

Before the review, I focused primarily on which sensitivity produced the largest numerical change in valuation.

The review made me recognize that sensitivity rankings depend not only on the ranges tested but also on the economic relationships included or excluded from the model.

My current model shows that reducing R&D or capex increases FCFE because less cash is spent. However, it does not model the possibility that lower investment could reduce future drug development, manufacturing capacity, or sales.

I now understand better that Lilly's valuation is not simply about maximizing near-term cash flow. The more important question is whether future growth and research productivity are sufficient to justify the investment required to produce that growth.

Therefore, my **\$589.21 per-share valuation remains my base-case result**, but I would investigate the relationship between growth, R&D, and manufacturing investment before changing my conclusion.
