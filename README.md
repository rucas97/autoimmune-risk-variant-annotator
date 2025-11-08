# 🧬 Autoimmune‑Risk Variant Annotator (Minimal Build)

**Author:** Reza Anvaripour (rucas97)  
**License:** MIT  
**Repository:** https://github.com/rucas97/autoimmune-risk-variant-annotator  

---

## 📖 Overview
The *Autoimmune‑Risk Variant Annotator* identifies autoimmune‑related GWAS SNPs that overlap known **immune‑regulatory genomic regions** (enhancers, promoters, etc.).  
This minimal version runs in **pure Python 3 (no C extensions)** and supports containerized reproducibility via Docker.

**Core outputs**
- `results/annotated_variants.csv` – SNP‑level regulatory overlap annotations  
- `results/variant_regulatory_map.png` – scatter plot (p‑value vs trait, color = regulatory overlap)  
- `results/autoimmune_annotation_report.html` – HTML summary report  

---

## ⚙️ Key Features
- Parses GWAS summary statistics from Markdown‑style or CSV tables  
- Checks overlaps between SNP coordinates and genomic intervals using fast vectorized Python logic  
- Generates publication‑ready visualizations (`seaborn`, `matplotlib`)  
- Builds portable through `Dockerfile` (no compilation required)  

