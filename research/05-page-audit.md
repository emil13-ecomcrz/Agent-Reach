# Page Audit — the live sales page

**Document type:** Diagnostic. What the current page does, what's wrong with it, ranked.
**Page audited:** https://bellenoor.se/products/bellenoor-retinal-shot
**Audited from:** the Shopify theme template (`templates/product.froya.json`, theme "Bellenoor V02 - Claude") plus a full screen capture of the rendered page.
**Status:** CURRENT as of 3 September 2026. Re-audit after any rebuild.
**Version:** v1 · September 2026
**Related:** `03-belief-chain.md` (the fix), `06-current-page-copy.md` (the raw copy)

---

## What the page is

18 sections, in this order:

1. Product details / buy box — rating, title, price, benefit grid, free starter guide, ATC, payment icons, 60-day guarantee, trust labels, one Instagram comment
2. Sticky add-to-cart
3. Trust bar — "Ren, skonsam och bevisad" (4 items)
4. Hero carousel — "Slätare porer. Fastare hud. Yngre uttryck." + before/after images
5. Mechanism — 200 000 mikronålar, rent A-vitamin, 9-peptidkomplex, pantenol
6. How it works — pores, fine lines, firming, daily ritual
7. How to use — 4 steps (numbered 1, 2, 3, 4, 4)
8. "Vad forskningen säger"
9. Roadmap — week 1, 2–4, 5–8, 8+
10. Frequency guide — stop / 1× / 5× / every night
11. Statistics — 93% / 89% / 91% / 94%
12. Ingredient tabs — ingredients, how it works, shipping & returns
13. Comparison — Retinal Shot vs. clinic & prescription
14. Expert board — 4 named advisors with quotes
15. Testimonials — 4 reviews
16. FAQ — 9 questions
17. Guarantee — 60 days
18. Related products

**Offer:** announcement bar "JUST NU REA: SPARA 33%". Bundle ladder with strike-through anchoring:
1 PACK (2 ST) 349 kr · 2 PACK (4 ST) 529 kr, spara 169 (was 698) · 3 PACK (6 ST) 698 kr, spara 349
(was 1 047) + free SPF 50 worth 199 kr. Klarna, Apple Pay, Google Pay, Shop Pay, card.

---

## What is genuinely strong — do not break these in a rebuild

1. **The mechanism.** "200 000 mikronålar, partiklar fem gånger mindre än en por" is a real
   unique-mechanism differentiator. It is the reason to buy, and it is currently the fifth section.
2. **The roadmap.** Week 1 purge → week 2–4 pores → week 5–8 lines → week 8+. It pre-frames the
   purge as proof rather than failure. This will cut refunds and support tickets more than any
   other block on the page.
3. **The FAQ does real selling.** "Kommer det HÄR verkligen att fungera på MIN hud?" is a
   direct-response question, not a policy page.
4. **The guarantee** is stated four times and phrased as risk reversal, not as a returns policy.
5. **The offer structure.** The bundle ladder is well built, and the free SPF on the 3-pack is a
   smart tie-in given the page's own warning that retinal increases sun sensitivity.

---

## Problems, ranked by revenue impact

### 1. The page has no lead, and no argument

It opens on product title and price. The best line on the page — "Slätare porer. Fastare hud.
Yngre uttryck." — is in section 4, below the fold.

Deeper than the missing headline: **the 18 sections do not build on each other.** Each asserts
something true; none hands a "therefore" to the next. Reorder almost any two and nothing is lost.
That is a list, not an argument.

**Fix:** rebuild the running order around the six beliefs in `03-belief-chain.md`.

### 2. Belief 01 is never installed

The page never tells her it wasn't her fault. It argues the mechanism, the safety and the timeline
well — to a woman who still half-suspects the problem is her age, her genes, her skin.

This is the cheapest fix available: roughly 200 words above the fold, no new assets required.

### 3. Nothing agitates the problem

Entirely solution-aware. It talks about retinaldehyde, peptides, spicules, cell renewal. It never
describes *being her*. There is no moment where she reads a line and thinks "that's me." The
closest is one Instagram comment and the 94% stat, which is the most emotionally true thing on
the page and is buried in section 11.

### 4. Claims that are unsupported or self-contradictory

| Claim | Problem |
|---|---|
| "Studier på Bellenoor Retinal Shot har följt användare i upp till 36 månader" | The product was created in Shopify on 2026-08-19. A 36-month study on *this product* cannot be supported. Reframe to ingredient-level research. |
| 93% / 89% / 91% / 94% | Unsourced, under the heading "Vi lovar inte bara resultat — vi bevisar dom". Source them or soften them. |
| "Partiklar fem gånger mindre än en por" vs "16 gånger tunnare än dina porer" | Two different numbers for the same mechanism, on the same page. Pick one. |
| Four named advisors with quotes | Verify they are real, contracted advisors — or remove. Named medical professionals is the one category where invented proof stops being marketing. |
| "Dermatologiskt testad" | Keep only if the lab or report can be named. |
| Testimonial dates (22 feb, 1, 9, 14 mars 2026) | Predate the product's existence (created 19 aug 2026). |

### 5. Four different usage schedules

| Where | What it says |
|---|---|
| How-to-use steps | Weeks 1–3: 2–3 nights → after week 4: up to 5 |
| FAQ | W1–2 every other night → W3–4: 3 → W5–7: 4 → W8+: 5–6 |
| "Vad forskningen säger" | After week 8, 5–6 nights is enough |
| Frequency block | "Varje kväll — maximal effekt" |

Pick one. The FAQ version is the best written; make every other section defer to it.

### 6. Unanswered questions that block the sale

- **How many nights does one tube last?** Nowhere on the page. Without it she can't do the value
  math and we can't write "under X kr per kväll" — the single strongest line available against the
  clinic comparison.
- **Full INCI list** is absent, despite the tabs section claiming "Full transparens."
- **Return mechanics:** who pays return shipping, is an opened tube accepted, how long does a
  refund take?
- **Layering:** what can she use it with, what should she avoid?
- **Who it's for / not for.**

### 7. CTA copy

"LÄGG I VARUKORGEN" (buy box) and "LÄGG I VARUKORG" (sticky bar) — inconsistent with each other,
and both name a mechanical action rather than an outcome. The two secondary CTAs are already
better ("BÖRJA IDAG", "PROVA RISKFRITT").

Only 2 primary buy buttons across 18 sections of scroll. Add one after the roadmap, one after the
statistics, one after the comparison — ask for the sale each time you finish proving something.

### 8. Copy errors

- Two steps numbered "Steg 4" in the how-to-use section (the second should be Steg 5)
- "det är A-Shot" in the safety FAQ — leftover from a different product name
- "Vi bevisar dom" → should be "dem", in the section whose whole job is credibility
- Missing punctuation producing run-ons: "Mikronålarna är 16 gånger tunnare än dina porer de tar
  sig ner dit vanliga krämer stannar", "Blir huden torr eller stram ligg kvar", "Inte nöjd får du
  pengarna tillbaka"
- Lowercase "retinal" starting two sentences in the how-it-works tab

---

## Assets that would move the number most, in order

1. Real before/after photos with a week counter, from real customers, with consent
2. Real Swedish UGC video — a woman in her forties, unpolished, in her own bathroom
3. Cost-per-night math (blocked on knowing how long a tube lasts)
4. A "vecka 1 ser ut så här" honesty block — the thing no competitor will do

---

## Operational note

The variant's inventory is at **-245** — the store is overselling. Fine if deliberate (EU
warehouse), but worth confirming, since the sticky bar promises a delivery date.
