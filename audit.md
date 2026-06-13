# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-06-13 — voice reform

Scope: density and rhythm pass against the house voice guide.

Changes:
- "carries/carry" thinned from 13 to 7: the figurative "lineage carried X,"
  "carries weight," "behavioral modernity has carried too much" recast to
  specific verbs (outweighs, sustained, rests on, asked to do); literal carrying
  (bipedality, fire, infants) left intact.
- Tricolon reflex: three-plus-item-list proxy from 57 to 41 by varying the worst
  reflexive enumerations (asyndeton, period split, "all of which/all to be"
  recasts), leaving the genuine record-survey enumerations readable.
- Syntax warns (3 inline-contrastive ", not Z") rewritten as positive
  declaratives in §4 (procession), §10 (crowded field, two).
- "Conclusion" (§11) retitled "The inheritance is older."

Verification: voice 0 errors, 0 review-candidates; refs advisory (narrative
citations, unchanged); claims 0 unmatched (no number touched); build clean;
check => PASS. Status unchanged.

## 2026-05-29 — upgrade pass (Group B)

Scope: integrate the §10 stratigraphy better and engage alternatives.

Changes:
- §10: justified the eight-capacity selection (single securely dated onset;
  symbolic marking and cooking excluded for lack of one defensible date); named
  the eight; showed the simulation entry point.
- §5: said concretely why Wonderwerk reads as controlled, not natural fire
  (microstratigraphy: burned bone and ashed plant matter in undisturbed deep-cave
  layers beyond wildfire/lightning reach).
- §7: stated the Neanderthal admixture magnitude (a few percent in present-day
  non-African genomes).

Verification: voice 0 errors; refs advisory (primary-source title-year); claims
0 unmatched; build clean; check => PASS. Status remains `built` (off-web).

## 2026-05-29 — computational layer added

Scope: instrument the "capacities predate the sapiens boundary" thesis with a
computation; bring to the publication bar.

Changes:
- New `simulation/`: a capability stratigraphy built from the first-appearance
  dates in the paper's own cited literature. Computes each capacity's lead time
  before the Jebel Irhoud (315 ka) and Omo I (233 ka) boundaries, the ordering,
  the span, and the crowd of contemporary lineages. A `chronology_Ma` block
  carries every dated point the paper states. `output/results.json` + a dated
  timeline figure.
- New §10 "The stratigraphy, measured"; Conclusion renumbered §11. Abstract
  gains a sentence with the headline counts.
- metadata: `has_simulation: true`, `claims_target: results.json`.

Verification:
- claims: 14 prose decimals, **0 unmatched** — all trace to results.json.
  7/8 capabilities predate Jebel Irhoud; 8/8 predate Omo I; deepest lead
  4.085 Ma (bipedality); span 4.1 Ma; 5 contemporary lineages. The lone capacity
  not clearing the older boundary is wooden weapons (Schoningen, 0.3 Ma).
- voice: 0 errors. refs: advisory (primary-source title-year style).
- build: clean, 10 pages, zero missing-character warnings. check => PASS.

Outstanding: GitHub repo private; not yet on the web papers page.
