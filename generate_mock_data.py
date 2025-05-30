#!/usr/bin/env python
"""
Reads signatures and instrument spec, synthesizes mock detector data,
and writes out mock_data.ndjson and mock_data.am.
"""

import argparse
import json

def load_ndjson(path):
    with open(path, 'r') as f:
        return [json.loads(line) for line in f]

def load_am(path):
    with open(path, 'r') as f:
        return f.read()

def synthesize_signal(signature, instr_spec):
    """
    Placeholder: generate synthetic time-series or spectrum for a signature.
    """
    label = signature["label"]
    # Create a trivial sine wave mock signal
    times = list(range(100))
    values = [signature["amplitude"] * __import__('math').sin(2 * __import__('math').pi * signature["frequency"] * t/100) for t in times]
    return {
        "label": label,
        "time_series": list(zip(times, values))
    }

def write_ndjson(data, path):
    with open(path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + "\n")

def write_am(summary, path):
    with open(path, 'w') as f:
        f.write(summary)

def main():
    p = argparse.ArgumentParser(description="Generate mock detector data")
    p.add_argument("--signatures-json", required=True)
    p.add_argument("--signatures-am", required=True)
    p.add_argument("--instr-am", required=True)
    p.add_argument("--output-json", required=True)
    p.add_argument("--output-am", required=True)
    args = p.parse_args()

    signatures = load_ndjson(args.signatures_json)
    instr_spec = load_am(args.instr_am)

    mock_data = [synthesize_signal(sig, instr_spec) for sig in signatures]
    write_ndjson(mock_data, args.output_json)

    am_summary = f"InstrumentSpec:\n{instr_spec}\nNumSignals: {len(mock_data)}\n"
    write_am(am_summary, args.output_am)

if __name__ == "__main__":
    main()