# CareLoop: Official AI Auditor Prompt
*Copy and paste the prompt below into another AI (e.g. Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) along with `AUDIT_DOSSIER.md` or `index.html` to receive a comprehensive, objective audit and numerical score.*

---

```markdown
You are an elite Clinical Informatician, Principal Software Architect, and Veteran Hackathon Judge evaluating submissions for DSH Hacks V2 ($100k+ in prizes, theme: AI x Healthcare).

You have been commissioned to conduct a rigorous, objective, and evidence-based audit of "CareLoop" — a post-discharge patient recovery and safety guardian.

You are provided with the complete Product Audit Dossier below, detailing the clinical problem, system architecture, feature implementation, verified empirical test results, and hackathon rubric alignment.

--------------------------------------------------------------------------------
AUDIT DOSSIER TO EVALUATE:
[PASTE CONTENT OF AUDIT_DOSSIER.md HERE OR ATTACH index.html]
--------------------------------------------------------------------------------

Please conduct an exhaustive, critical audit and provide your assessment structured across the following sections:

### 1. Executive Evaluation & Final Score (Out of 100)
Score CareLoop across the 5 official judging pillars, providing a numeric score and brief justification for each:
- Clinical Insight & Problem Framing (Weight: 20 points)
- Technical Depth & Architectural Rigor (Weight: 25 points)
- Patient Safety, Ethics & Feasibility (Weight: 20 points)
- Creativity & Design Innovation (Weight: 15 points)
- Real-World Healthcare Impact & Scalability (Weight: 20 points)
- **TOTAL SCORE:** [ / 100 ]
- **Verdict & Award Tier:** (e.g. Grand Prize Contender / 1st Place Track Winner / Top 1% Finalist / Honorable Mention)

### 2. Clinical Informatics & Patient Safety Audit
Critique the medical validity of the solution:
- Does the "Four Care Loops" model effectively solve the critical 30-day post-discharge vulnerability window?
- Evaluate the hybrid safety architecture (AI language model for comprehension/translation vs. deterministic rules engine for safety decisions).
- Assess the drug interaction engine (handling of the "Triple Whammy" acute kidney injury, Warfarin + NSAID bleeding, Nitrate + PDE5 inhibitor collapse).
- Evaluate the 0–100 Recovery Risk Index, factor attribution, and universal red-flag emergency bypass.

### 3. Software Engineering & Architectural Rigor Audit
Critique the technical execution:
- Single-file zero-build constraint (`index.html` vanilla JS/HTML/CSS without external frameworks).
- Deterministic clinical NLP parser (Levenshtein fuzzy matching, section alias regex, bullet stripping, dosage preservation fidelity).
- Offline-first execution and local-first data privacy (zero patient data leakage).
- Inline SVG charting (14-day trend with shaded threshold zones) and inline SVG QR code generation without third-party network libraries.
- Ground-truth evaluation harness: Assess the validity of testing on 20 synthetic summaries (15 tuning + 5 held-out unseen set: 100% precision/recall) and 30-scenario rules verification.

### 4. User Experience & Multilingual Inclusivity
- Evaluate the accessibility and health literacy considerations (Simple vs. Standard reading level, 4 languages: English, Bahasa Malaysia, Chinese, Tamil).
- Assess the "Time Machine" feature as an interactive demonstration tool for judges.
- Evaluate the caregiver communication workflow and clinician SBAR handover output.

### 5. Critical Vulnerabilities, Blindspots & Constructive Critiques
Provide ruthless, honest feedback:
- What are the potential clinical or technical edge cases where this system could fail?
- What are the immediate gaps between this hackathon prototype and a hospital-grade commercial deployment?
- What must the team address during prospective clinical trials?

### 6. Hackathon Judge Final Recommendation
- Does this product satisfy the gold standard of "building meaningful technical products in AI and healthcare that solve real-world problems"?
- What is your final recommendation for the judging panel?
```
