"""Orchestrator: reproduces every numerical claim in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the paper is a key in the JSON file. The dates are sourced from works in the
paper's reference list; this script computes the stratigraphic relations
(lead times, ordering, span, contemporary crowd) from them.
"""
from __future__ import annotations

import json
from pathlib import Path

from stratigraphy import run
from figures import plot_stratigraphy

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_stratigraphy(str(OUT / "figures" / "stratigraphy.png"))
    s = results["summary"]
    print(f"{s['n_predating_jebel_irhoud']}/{s['n_capabilities']} capabilities predate Jebel Irhoud (315 ka)")
    print(f"{s['n_predating_omo_i']}/{s['n_capabilities']} predate Omo I (233 ka)")
    print(f"deepest: {s['deepest_capability']} at {s['deepest_Ma']} Ma "
          f"(lead {s['deepest_lead_Ma']} Ma)")
    print(f"capability span: {s['capability_span_Ma']} Ma; "
          f"contemporary lineages: {s['n_contemporary_lineages']}")
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
