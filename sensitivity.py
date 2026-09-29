"""One-at-a-time sensitivity of the existing LLY model; standard library only."""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DRIVERS = {'GROWTH', 'MARGIN', 'SGA_GP', 'RD', 'IPRD', 'CAPEX', 'DAYS'}


def fresh_model():
    spec = importlib.util.spec_from_file_location('lly', ROOT / 'proforma_lly.py')
    model = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model)
    return model


def run(driver=None, values=None):
    model = fresh_model()  # Separate opening balances and assumptions every run.
    if driver:
        setattr(model, driver, tuple(values))
    inputs = {k: v for k, v in vars(model).items() if k.isupper()}
    years = model.project()
    gaps = [model.checks(y, p) for y, p in zip(years, [model.OPENING] + years[:-1])]
    error, value = None, None
    try:
        model.validate(years)
    except ValueError as exc:
        error = str(exc)
    limitation = error
    if not error:
        if any(y['fcfe'] < 0 for y in years):
            limitation = 'Value unavailable: inherited valuation omits negative explicit FCFE.'
        else:
            try:
                value = model.value_equity(years)['per_share']
            except ValueError as exc:
                limitation = str(exc)
    return dict(inputs=inputs, statements=years, checks=gaps, error=error,
                limitation=limitation, outputs=[years[-1]['operating_income'],
                                               years[-1]['fcfe'], value])


def main():
    config = json.loads((ROOT / 'scenarios.json').read_text())
    drivers = config['drivers']
    if len(drivers) != 2 or len({d['input'] for d in drivers}) != 2:
        raise SystemExit('Provide two distinct operating drivers in scenarios.json; see README.')
    if not config['prediction'] or not config['partner_checked_before_run']:
        raise SystemExit('Record your dated prediction and actual pre-run partner check first.')
    base = run()
    if base['error']:
        raise SystemExit(base['error'])
    results = {'base_before': base}
    lines = ['# LLY sensitivity results', '',
             'FY2030 operating profit and FCFE: USD millions. Value: USD/share.',
             'Input paths run FY2026–2030. Deltas = scenario minus base.', '',
             '| Input | Case | Actual path | Units | Profit | Δ profit | FCFE | Δ FCFE | Value | Δ value | Checks |',
             '|---|---|---|---|---:|---:|---:|---:|---:|---:|---|']
    spans = []
    for d in drivers:
        key = d['input']
        if key not in DRIVERS or not d['reason'] or not d['units']:
            raise ValueError('Use an existing operating input, units and a range reason.')
        group = []
        for case in ('lower', 'base', 'higher'):
            values = base['inputs'][key] if case == 'base' else d[case]
            if len(values) != 5:
                raise ValueError('Each path must contain five annual values.')
            result = run(key, values)
            assert all(v == base['inputs'][k] for k, v in result['inputs'].items() if k != key)
            results[f'{key}_{case}'] = result
            group.append(result)
            cells = []
            for actual, original in zip(result['outputs'], base['outputs']):
                cells.extend(['N/A' if actual is None else f'{actual:,.2f}',
                              'N/A' if actual is None or original is None else f'{actual-original:+,.2f}'])
            status = result['error'] or 'PASS (all 5 years)'
            lines.append('| ' + ' | '.join([key, case, str(list(values)), d['units'], *cells, status]) + ' |')
        spread = []
        for i in range(3):
            valid = [r['outputs'][i] for r in group if not r['error'] and r['outputs'][i] is not None]
            spread.append(f'{max(valid)-min(valid):,.2f}' if len(valid) == 3 else 'N/A (incomplete valid set)')
        spans.append('| ' + ' | '.join([key, *spread]) + ' |')
    restored = run()
    assert restored == base, 'Restored base does not match initial base.'
    results['base_after'] = restored
    lines.extend(['', '## Output spans over these ranges', '',
                  '| Input | Profit span | FCFE span | Value span |', '|---|---:|---:|---:|',
                  *spans, '', 'Restored base: PASS (exact equality). Accounting tolerance: $0.01 million.',
                  'Full input sets, statements and every check are retained in results.json.'])
    lines.extend(f"\n{d['input']} range reason: {d['reason']}" for d in drivers)
    for name, result in results.items():
        if result['limitation']:
            lines.append(f"- {name}: {result['limitation']}")
    (ROOT / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    (ROOT / 'results.md').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
