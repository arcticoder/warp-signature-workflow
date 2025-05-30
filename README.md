# warp-signature-workflow

This repository takes the outputs of the warp-curvature pipeline and produces quantum-geometry signatures, synthetic detector data, and sensitivity comparisons.

## Inputs

All inputs live in the root of the repo:

- `strong_curvature.ndjson`  
- `strong_curvature.am`  
- `simulation_summary.ndjson`  
- `simulation_summary.am`  
- `instrument_spec.am`  
- `sensitivity_curves.am`  

## Scripts

### 1. compute_signatures.py

**Description:**  
Loads `strong_curvature.ndjson` & `simulation_summary.ndjson` (plus their `.am` metadata), computes mode frequencies, widths, and amplitudes for each curvature feature.

**Outputs:**

- `signatures.ndjson`  
- `signatures.am`  

**Usage:**
```bash
python compute_signatures.py `
  --input-json   strong_curvature.ndjson `
  --input-am     strong_curvature.am `
  --summary-json simulation_summary.ndjson `
  --summary-am   simulation_summary.am `
  --output-json  signatures.ndjson `
  --output-am    signatures.am
```

---

### 2\. generate\_mock\_data.py

**Description:**  
Reads `signatures.ndjson` + `signatures.am` + `instrument_spec.am`, synthesizes time-series/spectra as a given detector would record for each signature.

**Outputs:**

-   `mock_data.ndjson`
    
-   `mock_data.am`
    

**Usage:**

```bash
python generate_mock_data.py `
  --signatures-json signatures.ndjson `
  --signatures-am   signatures.am `
  --instr-am        instrument_spec.am `
  --output-json     mock_data.ndjson `
  --output-am       mock_data.am
```

---

### 3\. compare\_sensitivity.py

**Description:**  
Ingests `mock_data.ndjson` + `mock_data.am` + `sensitivity_curves.am`, calculates SNR and detectability for each mock signal.

**Outputs:**

-   `sensitivity_comparison.ndjson`
    
-   `sensitivity_comparison.am`
    

**Usage:**

```bash
python compare_sensitivity.py `
  --mock-json  mock_data.ndjson `
  --mock-am    mock_data.am `
  --sens-am    sensitivity_curves.am `
  --output-json sensitivity_comparison.ndjson `
  --output-am   sensitivity_comparison.am
```
