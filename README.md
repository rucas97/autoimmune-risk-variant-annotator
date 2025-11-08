# 🧬 Autoimmune‑Risk Variant Annotator (Minimal Stable Release)

**Author:** Reza Anvaripour (rucas97)  
**License:** MIT  
**Repository:** https://github.com/rucas97/autoimmune-risk-variant-annotator  
**Environment:** Python ≥ 3.10  |  Tested on Windows 10 WSL & Docker Desktop  

---

## 📖 Overview
The **Autoimmune‑Risk Variant Annotator** identifies genome‑wide significant autoimmune GWAS variants that overlap known **immune‑regulatory regions** (e.g., enhancers, promoters).  
This minimal build uses **pure Python logic** for genomic interval overlap — no compiled packages — ensuring stable, reproducible Docker builds across platforms.

### Outputs
| File | Description |
|------|--------------|
| `results/annotated_variants.csv` | Annotated SNPs with regulatory overlap flag |
| `results/variant_regulatory_map.png` | Scatter plot of significant hits |
| `results/autoimmune_annotation_report.html` | HTML summary report |

---

## ⚙️ Key Features
- Parses GWAS summary statistics from CSV or Markdown‑pipe files  
- Filters genome‑wide‑significant SNPs (`p < 1e‑6`)  
- Computes SNP–regulatory overlaps via pure Python (`regulatory_overlap.py`)  
- Generates publication‑ready scatter plots (`matplotlib`, `seaborn`)  
- Produces interactive HTML reports (via `jinja2`)  
- Fully reproducible with a single Docker command  

---

## 🧩 Project Structure
```
autoimmune-risk-variant-annotator-minimal/
│
├── data/
│   ├── demo_GWAS_hits.csv         # Example GWAS input (Markdown-format table)
│   └── regulatory_db.bed          # Regulatory-element intervals (BED)
│
├── src/
│   ├── variant_annotator.py       # Main workflow (load GWAS, annotate, plot)
│   ├── regulatory_overlap.py      # Pure-Python overlap logic
│   └── report_generator.py        # Template-based HTML report builder
│
├── results/                       # Outputs generated automatically
│
├── requirements.txt               # pandas, seaborn, matplotlib, jinja2
├── Dockerfile                     # Minimal reproducible container image
└── README.md
```

---

## 🚀 Quick Start

### Option A — Run Directly on Host
```bash
# (1) Install dependencies
pip install -r requirements.txt

# (2) Run the annotator
python src/variant_annotator.py
```

### Option B — Run via Docker
```bash
# Build container
docker build -t autoimmune-annotator .

# Run container (mount current directory to save results)
docker run --rm -v ${PWD}:/app autoimmune-annotator
```
> **Windows PowerShell:** use `${PWD}` or `$(pwd)` as appropriate.  
> All results appear in local `results/`.

---

## 🧠 Pipeline Logic
1. **Load GWAS Summary Stats**  
   Reads table (Markdown/CSV), retains SNP IDs, chromosome, position, trait, p‑value.  
2. **Load Regulatory Database**  
   BED‑formatted enhancers/promoters from ENCODE or RegulomeDB.  
3. **Compute Overlaps**  
   Each SNP position checked for interval inclusion using vectorized comparisons (no `pybedtools`).  
4. **Visualization & Report**  
   Generates scatter plot + HTML dashboard summarizing the overlaps.  

---

## 📦 Dependencies
```
pandas
matplotlib
seaborn
jinja2
```

---

## 📈 Example Output
| rs_id | trait | p‑value | overlaps_regulatory |
|:------|:-------|--------:|:-------------------:|
| rs2476601 | Type 1 Diabetes | 2e‑8 | ✅ |
| rs6679677 | Graves Disease  | 1.1e‑10 | ✅ |
| rs9268645 | Rheumatoid Arthritis | 5e‑9 | ❌ |

*HTML summary generated automatically at `results/autoimmune_annotation_report.html`.*

---

## 🧬 Applications
- Prioritization of autoimmune‑risk loci for follow‑up functional validation  
- Cross‑comparison with chromatin accessibility or eQTL datasets  
- Educational showcase for variant annotation workflows (Python + Docker)

---

## 🧾 Citation & Acknowledgement
Developed by **Reza Anvaripour**, MSc (Molecular Genetics)  
For inclusion in research or derivative pipelines, please cite:

> *Anvaripour R. (2025). Autoimmune‑Risk Variant Annotator (Minimal Build).*  
> GitHub repository: https://github.com/rucas97/autoimmune-risk-variant-annotator  

---

### 🧰 Release Notes
**v1.0 – Minimal Stable Release**
- Removed `pybedtools` and all C build requirements  
- Implemented pure‑Python interval logic (`regulatory_overlap.py`)  
- Added robust Markdown/CSV parsing in `variant_annotator.py`  
- Automated HTML report and figure export  
- Verified Docker build stability on Windows 10 (WSL2)
