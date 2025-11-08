import pandas as pd
import os
from jinja2 import Template

def generate_html_report(csv_path: str, output_path: str):
    df = pd.read_csv(csv_path)
    template = Template("""
    <html><head><title>Autoimmune Variant Annotation</title></head>
    <body>
    <h2>GWAS Variant Annotation Summary</h2>
    <p>Total variants analyzed: {{ count }}</p>
    <table border=1 cellspacing=0 cellpadding=4>
        <tr><th>rs_id</th><th>Trait</th><th>p-value</th><th>Overlap Regulatory?</th></tr>
        {% for r in rows %}
        <tr><td>{{ r.rs_id }}</td><td>{{ r.trait }}</td><td>{{ r.pval }}</td><td>{{ r.overlaps_regulatory }}</td></tr>
        {% endfor %}
    </table>
    </body></html>
    """)
    html = template.render(count=len(df), rows=df.itertuples())
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"📈 HTML report created → {output_path}")
