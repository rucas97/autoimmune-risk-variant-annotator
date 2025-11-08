"""Pure-Python overlap detection for BED intervals (no pybedtools)."""
from typing import List, Tuple, Dict

def _load_bed(bed_path: str) -> Dict[str, List[Tuple[int, int]]]:
    idx = {}
    with open(bed_path) as f:
        for line in f:
            if not line.strip() or line.startswith(("#", "track", "browser")):
                continue
            chrom, start, end, *_ = line.strip().split("	")
            idx.setdefault(chrom, []).append((int(start), int(end)))
    for chrom in idx:
        idx[chrom].sort()
    return idx

def _overlap(idx, chrom, pos) -> bool:
    for s, e in idx.get(chrom, []):
        if pos < s:
            return False
        if s <= pos < e:
            return True
    return False

def check_overlap(chrom: str, pos: int, bed_path: str) -> bool:
    idx = _load_bed(bed_path)
    return _overlap(idx, chrom, pos)
