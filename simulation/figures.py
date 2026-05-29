"""Figure: the capability stratigraphy as a dated timeline."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from stratigraphy import CAPABILITIES, BOUNDARY, CONTEMPORARY_LINEAGES


def plot_stratigraphy(path: str) -> None:
    caps = sorted(CAPABILITIES, key=lambda c: c[1])  # shallow -> deep
    names = [c[0] for c in caps]
    dates = [c[1] for c in caps]
    y = range(len(caps))

    fig, ax = plt.subplots(figsize=(9, 5))
    # each capability: a lollipop from the boundary to its onset date
    for i, ma in zip(y, dates):
        ax.plot([BOUNDARY["jebel_irhoud"], ma], [i, i], color="#999", lw=1, zorder=1)
    ax.scatter(dates, list(y), s=70, color="#2166ac", zorder=3)
    ax.set_yticks(list(y))
    ax.set_yticklabels(names)

    # boundary band: Jebel Irhoud (315 ka) to Omo I (233 ka)
    ax.axvspan(BOUNDARY["omo_i"], BOUNDARY["jebel_irhoud"], color="#fddbc7", alpha=0.7, zorder=0)
    ax.axvline(BOUNDARY["jebel_irhoud"], color="#b2182b", lw=1.2, ls="--")
    ax.text(BOUNDARY["jebel_irhoud"], len(caps) - 0.4,
            " sapiens boundary\n (315-233 ka)", color="#b2182b", fontsize=9, va="top")

    ax.set_xscale("log")
    ax.set_xlabel("first appearance (million years ago, log scale)")
    ax.invert_xaxis()  # deep time on the left -> present on the right
    ax.set_title("Capability stratigraphy of the hominin record")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
