"""A capability stratigraphy of the hominin record.

The paper's claim is chronological: the capacities later gathered under
*Homo sapiens* have first-appearance dates that mostly precede the sapiens
boundary, and the record therefore has the structure of a stratigraphy. This
module makes that claim measurable. Every date and its source is taken from a
work cited in the paper's references; the computation reports the lead time of
each capability before the boundary, the ordering, the total span, and the
crowd of contemporary lineages.

Dates are in millions of years ago (Ma). They are point estimates drawn from
the cited literature, not original measurements; where a paper gives a range,
the value used is noted.
"""
from __future__ import annotations

# Capability onsets: the earliest secure dated marker of each capacity, with
# the site and the cited source. (name, Ma, site, maker, citation)
CAPABILITIES = [
    ("bipedal locomotion", 4.40, "Ardipithecus ramidus body plan",
     "Ardipithecus ramidus", "White et al. 2009"),
    ("stone-flake production", 3.30, "Lomekwi 3, West Turkana",
     "unknown (pre-secure Homo)", "Harmand et al. 2015"),
    ("large-animal butchery", 2.90, "Nyayanga (3.0-2.6 Ma; midpoint used)",
     "Paranthropus / early Homo", "Plummer et al. 2023"),
    ("Oldowan technology", 2.60, "Gona, Ethiopia",
     "early Homo", "Semaw et al. 1997"),
    ("continental dispersal", 1.80, "Dmanisi, Georgia",
     "early Homo", "Lordkipanidze et al. 2013"),
    ("Acheulean biface", 1.76, "Kokiselei, Kenya",
     "Homo erectus", "Lepre et al. 2011"),
    ("controlled fire", 1.00, "Wonderwerk Cave (in situ burning)",
     "Homo erectus / archaic", "Berna et al. 2012"),
    ("wooden weapons", 0.30, "Schoningen, Germany",
     "Neanderthal-lineage / Middle Pleistocene", "Thieme 1997"),
]

# The sapiens boundary is not a single date. Three commonly cited points:
BOUNDARY = {
    "jebel_irhoud": 0.315,  # Hublin et al. 2017; Richter et al. 2017
    "omo_i": 0.233,         # Vidal et al. 2022 (revised minimum age)
    "herto": 0.160,         # White et al. 2003
}
PRIMARY_BOUNDARY = BOUNDARY["jebel_irhoud"]

# Fuller chronology of dated points the paper discusses, beyond the capability
# onsets above. Each value is a point estimate from a cited work; ranges are
# noted. This is the reference table the stratigraphy is read from.
CHRONOLOGY = [
    ("Sahelanthropus tchadensis (contested)", 7.00, "Brunet et al. 2002"),
    ("Ardipithecus ramidus", 4.40, "White et al. 2009"),
    ("Australopithecus afarensis (upper range)", 3.90, "afarensis 3.9-2.9 Ma"),
    ("Laetoli footprints", 3.66, "Leakey & Hay 1979"),
    ("Lomekwi 3 stone tools", 3.30, "Harmand et al. 2015"),
    ("Lucy (A. afarensis)", 3.20, "A. afarensis"),
    ("Nyayanga (upper bound)", 3.00, "Plummer et al. 2023"),
    ("Gona Oldowan", 2.60, "Semaw et al. 1997"),
    ("Dmanisi dispersal", 1.80, "Lordkipanidze et al. 2013"),
    ("Kokiselei Acheulean", 1.76, "Lepre et al. 2011"),
    ("Nariokotome skeleton", 1.50, "Brown et al. 1985"),
    ("Wonderwerk fire", 1.00, "Berna et al. 2012"),
    ("Sima de los Huesos", 0.43, "Meyer et al. 2016"),
    ("Jebel Irhoud", 0.315, "Hublin et al. 2017; Richter et al. 2017"),
    ("Schoningen spears", 0.30, "Thieme 1997"),
    ("Omo I", 0.233, "Vidal et al. 2022"),
    ("Herto", 0.16, "White et al. 2003"),
]

# Other hominin lineages near or overlapping the boundary (the crowded planet).
CONTEMPORARY_LINEAGES = [
    ("Neanderthal lineage (Sima de los Huesos)", 0.430, "Meyer et al. 2016"),
    ("Homo naledi", 0.286, "Dirks et al. 2017 (335-236 ka; midpoint used)"),
    ("Denisovans", 0.200, "Reich et al. 2010 (from DNA; date approximate)"),
    ("Homo luzonensis", 0.067, "Detroit et al. 2019 (minimum for one element)"),
    ("Homo floresiensis", 0.050, "survival on Flores"),
]


def run() -> dict:
    caps = []
    for name, ma, site, maker, cite in CAPABILITIES:
        lead = round(ma - PRIMARY_BOUNDARY, 4)
        caps.append({
            "capability": name,
            "first_appearance_Ma": ma,
            "site": site,
            "maker": maker,
            "citation": cite,
            "lead_before_boundary_Ma": lead,
            "predates_jebel_irhoud": ma > PRIMARY_BOUNDARY,
            "predates_omo_i": ma > BOUNDARY["omo_i"],
        })

    n = len(caps)
    n_predate_ji = sum(c["predates_jebel_irhoud"] for c in caps)
    n_predate_omo = sum(c["predates_omo_i"] for c in caps)
    leads = sorted(c["lead_before_boundary_Ma"] for c in caps)
    deepest = max(caps, key=lambda c: c["first_appearance_Ma"])
    shallowest = min(caps, key=lambda c: c["first_appearance_Ma"])
    median_lead = leads[n // 2] if n % 2 else round(0.5 * (leads[n // 2 - 1] + leads[n // 2]), 4)

    return {
        "sapiens_boundary_Ma": BOUNDARY,
        "primary_boundary": "jebel_irhoud",
        "chronology_Ma": [
            {"event": n, "date_Ma": ma, "citation": c} for n, ma, c in CHRONOLOGY
        ],
        "capabilities": caps,
        "contemporary_lineages": [
            {"lineage": l, "date_Ma": d, "citation": c} for l, d, c in CONTEMPORARY_LINEAGES
        ],
        "summary": {
            "n_capabilities": n,
            "n_predating_jebel_irhoud": n_predate_ji,
            "n_predating_omo_i": n_predate_omo,
            "deepest_capability": deepest["capability"],
            "deepest_Ma": deepest["first_appearance_Ma"],
            "deepest_lead_Ma": deepest["lead_before_boundary_Ma"],
            "shallowest_capability": shallowest["capability"],
            "shallowest_Ma": shallowest["first_appearance_Ma"],
            "capability_span_Ma": round(deepest["first_appearance_Ma"] - shallowest["first_appearance_Ma"], 4),
            "median_lead_Ma": median_lead,
            "n_contemporary_lineages": len(CONTEMPORARY_LINEAGES),
        },
    }
