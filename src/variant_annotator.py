import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from regulatory_overlap import check_overlap
from report_generator import generate_html_report

GWAS_FILE = "data/demo_GWAS_hits.csv"
BED_FILE = "data/regulatory_db.bed"
OUT_DIR = "results"

os.makedirs(OUT_DIR, exist_ok=True)

def load_gwas(file_path: str) -> pd.DataFrame:
    """Robustly load GWAS summary stats (handles Markdown-style tables)."""
    import io

    with open(file_path, encoding="utf-8") as f:
        content = f.read().strip()

    # Detect Markdown pipe table
    if "|" in content.splitlines()[0]:
        # Remove Markdown border rows (---)
        lines = [ln for ln in content.splitlines() if "---" not in ln]
        # pandas will treat multiple '|' correctly using engine="python"
        df = pd.read_csv(io.StringIO("\n".join(lines)), sep="|", engine="python")

        # Clean up any unnamed / empty columns caused by border pipes
        df = df.rename(columns=lambda c: c.strip())
        df = df.loc[:, [c for c in df.columns if c not in ("", None, "Unnamed: 0")]]

        # Strip whitespace from cell content
        for c in df.columns:
            df[c] = df[c].astype(str).str.strip()
    else:
        df = pd.read_csv(file_path)

    # Enforce proper dtypes
    if "chrom" not in df.columns or "pos" not in df.columns:
        raise ValueError(f"GWAS file malformed — expected columns chrom,pos but got {list(df.columns)}")

    df["chrom"] = df["chrom"].astype(str)
    df["pos"] = pd.to_numeric(df["pos"], errors="coerce").fillna(0).astype(int)
    df["pval"] = pd.to_numeric(df["pval"], errors="coerce")

    valid = df[df["pos"] > 0]
    print(f"✅ Loaded {len(valid)} GWAS variants after cleaning.")
    return valid



def annotate(df):
    return df.assign(overlaps_regulatory=[check_overlap(ch, int(pos), BED_FILE) for ch, pos in zip(df.chrom, df.pos)])

def plot(df):
    plt.figure(figsize=(7,4))
    sns.scatterplot(data=df, x='pval', y='trait', hue='overlaps_regulatory', s=80)
    plt.xscale('log')
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/variant_regulatory_map.png", dpi=200)
    plt.close()

if __name__ == '__main__':
    gwas = load_gwas(GWAS_FILE)
    annotated = annotate(gwas)
    annotated.to_csv(f"{OUT_DIR}/annotated_variants.csv", index=False)
    plot(annotated)
    generate_html_report(f"{OUT_DIR}/annotated_variants.csv", f"{OUT_DIR}/autoimmune_annotation_report.html")
    print('✅ Workflow complete: results written to results/')
