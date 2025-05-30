#!/usr/bin/env python
"""
Ingests mock data and sensitivity curves, computes SNR and detectability,
and writes out sensitivity_comparison.ndjson and sensitivity_comparison.am.
"""

import argparse
import json

def load_ndjson(path):
    with open(path, 'r') as f:
        return [json.loads(line) for line in f]

def load_am(path):
    with open(path, 'r') as f:
        return f.read()

def compute_snr(time_series, sens_curve):
    """
    Placeholder: compute SNR by comparing time_series to sens_curve.
    """
    # simplistic: peak value over threshold
    values = [v for _, v in time_series]
    peak = max(abs(v) for v in values)
    threshold = float(sens_curve.strip().split()[-1]) if sens_curve else 1.0
    snr = peak / threshold
    detectable = snr >= 1.0
    return snr, detectable

def write_ndjson(data, path):
    with open(path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

def write_am(summary, path):
    with open(path, 'w') as f:
        f.write(summary)

def main():
    p = argparse.ArgumentParser(description="Compare mock signals against sensitivity curves")
    p.add_argument("--mock-json", required=True)
    p.add_argument("--mock-am", required=True)
    p.add_argument("--sens-am", required=True)
    p.add_argument("--output-json", required=True)
    p.add_argument("--output-am", required=True)
    args = p.parse_args()

    mock_data = load_ndjson(args.mock_json)
    sens_curve = load_am(args.sens_am)

    results = []
    for entry in mock_data:
        snr, detectable = compute_snr(entry["time_series"], sens_curve)
        results.append({
            "label": entry["label"],
            "snr": snr,
            "detectable": detectable
        })

    write_ndjson(results, args.output_json)

    am_summary = f"DetectionThresholds:\n{sens_curve}\nNumChecked: {len(results)}\n"
    write_am(am_summary, args.output_am)

if __name__ == "__main__":
    main()