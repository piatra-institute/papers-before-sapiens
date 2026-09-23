# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 22 CSL entries, all with DOIs. 18 correct automatic Crossref matches resolved through doi.org; dirks2017 (automatic match was the eLife decision letter), green2010, meyer2016 and scerri2018 resolved by hand through their DOIs. Full author lists now come from the records (the legacy list abbreviated most to "et al."). Page/article numbers added for berna2012 (E1215-E1220) and hutson2025 (eadv0752).
- Taxon names in titles set in italics without title-casing. Citations converted by hand for the "et al." forms (the converter could not parse the abbreviated author lists); no corrections to authors, years or titles were needed.
- claims.yaml: 47 claims (29 computation, 8 source, 7 interpretation, 1 definition, 2 assumption). Every number in the abstract and section 10 and every literature date entered in simulation/stratigraphy.py that appears in the text is bound to simulation/output/results.json; the word-form counts ("seven of the eight", "at least five") are interpretations citing /summary/n_predating_* and /summary/n_contemporary_lineages. Source claims checked against Crossref/OpenAlex abstracts: Vidal et al. (233 +/- 22 kyr), Berna et al. (~1.0 Ma in situ burning), Hutson et al. (~200,000 years), Plummer et al. (3.032-2.581 Ma, hippopotamid butchery, Paranthropus), Dirks et al. (236-335 ka), Reich et al. (Denisovans), Scerri et al. (structured African populations), White et al. 2009 (4.4 Ma, bipedality with arboreality).
- Not bound (no abstract available or abstract silent): Green et al. "a few percent of the genome"; Harmand et al., Semaw et al., Lepre et al., Leakey and Hay, Brunet et al., Brown et al., Hublin et al., Richter et al., Meyer et al., Détroit et al., Thieme, White et al. 2003 (no abstracts in Crossref/OpenAlex); the H. floresiensis survival date (no citation in the text).
- Execution receipt: run before-sapiens (uv run python run_all.py); results.json reproduced byte-identically.
- metadata claims_target: results.json -> claim-ledger.

## 2026-09-23 — prose revision

Prose revised against the house standards. Headings: Abstract; 1. Introduction; 2. Bipedalism; 3. Stone tools before secure Homo; 4. Early Homo and continental dispersal; 5. Fire use and maintenance; 6. Organic technology and teaching; 7. Contemporary hominin lineages; 8. The emergence of Homo sapiens in Africa; 9. Single-variable origin accounts; 10. Quantified stratigraphy; 11. Conclusion; Reproducibility.
Tic counts before -> after: 'rather than' 3 -> 0; 'the paper' 1 -> 0; sentence-initial 'This is' 0 -> 0 (one introduced and removed). Narrative citations ("Hublin and colleagues", "Green and colleagues", etc.) converted to author-year; Thieme (1997), previously uncited, now cited for the original Schoningen description.
Correction (simulation input): stratigraphy.py entered Nyayanga large-animal butchery at 2.90 Ma while documenting "3.0-2.6 Ma; midpoint used"; the midpoint is 2.80. Changed to 2.80; its lead over Jebel Irhoud changes 2.585 -> 2.485 Ma. Counts (7/8, 7/8), deepest lead 4.085, span 4.2 and median lead 1.885 Ma are unaffected (the median is the mean of the 4th and 5th leads, 1.485 and 2.285). The value 2.585 was not quoted in the text; the midpoint rule is now stated in section 10.
Verified against results.json: 4.085, 4.2, 1.885, 1.485 ("close to 1.5"), 7 of 8 for both boundaries, 5 contemporary lineages, Homo naledi midpoint 0.2855.
Grid audit: no grids, thresholds or optimisation in the computation; nothing to refine.

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
