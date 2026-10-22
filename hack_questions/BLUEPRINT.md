# CareLoop: DSH Hacks V2 Project Blueprint

Oct 22, 2026 · @Shaun Jee

## 0. How to use this document (instructions for the AI build agent)

You are building **CareLoop**, a hackathon prototype for DSH Hacks V2 (theme: AI x Healthcare). Follow this document top to bottom.

- **Deliverable:** one self-contained file, `index.html`. Vanilla JS and CSS only. No build step. CDN libraries allowed only where this document names them.
- **Must work offline and without any API key** (Demo Mode). An optional LLM mode is enabled when the user pastes an API key in Settings. The key stays in `localStorage` and is never sent anywhere except the LLM endpoint.
- **Never fabricate metrics.** Any accuracy or impact figure shown in the UI must be computed live from the bundled test set or labeled as an illustrative assumption.
- **Definition of done:** every acceptance test in Section 11 passes, the three demo scenarios in Section 10 run flawlessly, and the UI is polished at 390px and 1440px widths.
- Build in the phase order of Section 9. After each phase, run the phase's checks before moving on.

## 1. The one-line pitch

**CareLoop turns a confusing hospital discharge into a safe, understandable recovery plan in your own language, and watches the first 30 days so a family and a doctor know before things go wrong.**

## 2. The problem (clinical insight)

The days after hospital discharge are one of the most dangerous periods in a patient's care.

- Discharge summaries are written for clinicians: dense, abbreviated, English-only. Patients and family caregivers often leave not knowing what changed in their medicines, which warning signs matter, or when to return.
- Elderly patients with chronic disease (heart failure, diabetes, kidney disease, post-surgery recovery) typically go home on several new or changed medicines. This is a classic setup for missed doses, duplicate drugs, and harmful combinations with over-the-counter products.
- Deterioration usually starts quietly (weight creeping up, a bit more breathless, glucose drifting) and nobody is looking until it is an emergency and a readmission.
- In multilingual countries such as Malaysia, many patients and caregivers are more comfortable in Bahasa Malaysia, Mandarin or Tamil than in medical English.

Statistics to cite on the one-pager (the agent must **verify each against its primary source and add the citation**; drop any it cannot verify):

- Share of hospitalised adults readmitted within 30 days (widely cited US figure of roughly one in five Medicare patients, Jencks et al., NEJM 2009).
- Share of readmissions linked to medication problems or poor discharge understanding.
- Health literacy gap data (e.g., WHO or national health literacy surveys).
- Malaysia's ageing and chronic disease burden (National Health and Morbidity Survey).

## 3. The solution in one picture

CareLoop has four loops that connect patient, caregiver and clinician:

1. **Decode:** discharge summary in, structured and plain-language care plan out, in four languages.
2. **Protect:** medication schedule plus interaction and duplicate checks, including over-the-counter products.
3. **Watch:** a 60-second daily check-in feeding an explainable Recovery Risk Score and a deterministic red-flag safety net.
4. **Connect:** one-tap caregiver alerts and an auto-generated one-page clinician brief (SBAR format).

**Design principle that wins on technical depth and safety:** a *hybrid* architecture. The AI language layer understands and explains. A transparent, deterministic clinical rules engine makes every safety decision. The LLM can never lower a risk level or suppress an alert.

## 4. Features (in priority order)

### F1. Discharge Decoder (must have)

- Input: paste text, load a sample, or upload a photo (optional OCR via Tesseract.js from CDN).
- Output (structured JSON, schema in Section 6): diagnoses, medicines (name, dose, route, frequency, purpose, food notes, new/changed/stopped flag), follow-up appointments, warning signs, lifestyle restrictions.
- Plain-language view with a reading-level toggle (Simple / Standard) and a language switch: English, Bahasa Malaysia, 中文, தமிழ். Medicine names and doses are never translated, only explained around.
- Every plain-language sentence carries a small "from your summary" chip. Hovering highlights the source line in the original text (traceability builds trust).
- **Demo Mode engine:** rule-based parser (regex and section headers) plus a bundled drug dictionary of about 60 common drugs with purposes and food notes. Pre-translated templates for the four languages cover the three demo personas and the common sentence patterns.
- **LLM mode:** sends the text with the extraction prompt in Section 7 and validates the response against the schema. On invalid JSON, retry once, then fall back to the rule-based engine.

### F2. Medication Guardian (must have)

- Daily timeline (morning, noon, evening, bedtime) with big tap targets to mark doses as taken. Adherence ring and 7-day streak.
- Interaction and duplicate check across the discharge medicines **and anything the user adds**, including OTC items such as ibuprofen, cough syrups and herbal products. Severity levels: Avoid, Caution, Monitor.
- Each alert explains the reason in plain words and says what to do ("Ask your pharmacist before taking this").
- Bundled curated interaction table of about 30 high-impact pairs (Section 6). State clearly in the UI that this is a demo subset and that production would use a licensed drug database.

### F3. Daily Check-in and Recovery Risk Score (must have, the heart of the demo)

- Condition-aware 60-second check-in. Mix of sliders, large yes/no chips and number inputs (weight, temperature, glucose, blood pressure where relevant). Optional voice input through the Web Speech API when available.
- **Recovery Risk Score (0 to 100)** computed by the transparent rules engine in Section 8. Traffic-light result (Green: on track, Amber: call your clinic today, Red: act now) with a "Why this score" panel listing each contributing factor and its points.
- 14-day trend chart (inline SVG) with the baseline, thresholds and medication adherence overlay.
- A **Time Machine** control in the demo: skip forward day by day through a scripted recovery that deteriorates, so judges see the system catch a problem early.

### F4. Red-Flag Safety Net (must have)

- Always-visible "I feel unwell" button. Universal red flags (chest pain, severe breathlessness, fainting, confusion, stroke signs, heavy bleeding, suicidal thoughts) immediately show a full-screen emergency card: call 999 or 112 in Malaysia, with the user's address and medicine list ready to read aloud.
- Deterministic only. No LLM in this path.

### F5. Caregiver Circle (should have)

- Caregiver view (separate tab, simulated sharing via a QR code and a share link): today's status, missed doses, and alert history, with large type and one-tap "Call Pak Ahmad".
- Simulated notification toast and a mock SMS/WhatsApp-style message preview when the score turns Amber or Red.

### F6. Clinician Brief (should have, a judge favourite)

- One tap generates a one-page SBAR summary (Situation, Background, Assessment, Recommendation): discharge diagnoses, current medicines, adherence, trend chart, flagged symptoms and a suggested action that a clinician can accept or ignore.
- Print stylesheet so "Save as PDF" produces a clean A4 page.
- Clearly labeled: decision support, not a diagnosis.

### F7. Trust Panel (should have, signals technical depth)

- A bundled test set of 20 synthetic discharge summaries with ground-truth annotations. A "Run evaluation" button computes real precision and recall for medicine extraction, dose accuracy and warning-sign capture, and displays them live.
- A rules-engine test runner (30 scenario cases) showing pass or fail for each threshold.
- Privacy statement: local-first, no data leaves the device in Demo Mode.

### F8. Impact Estimator (nice to have)

- Slider-driven calculator for a hospital ward (discharges per month, baseline readmission rate, assumed reduction). Every input is labeled as an assumption and no outcome is claimed as proven.

## 5. Demo personas (bundled synthetic data, no real patients)

1. **Pak Ahmad, 72, Kuala Lumpur.** Heart failure plus type 2 diabetes. Eight medicines. Primary language Bahasa Malaysia. Caregiver: daughter Aisyah. This is the hero scenario.
2. **Mdm Tan, 68, Penang.** Hip fracture surgery. Blood thinner after surgery, painkillers. Language: 中文. Highlights post-operative flags and the bleeding risk interaction.
3. **Priya, 54, Johor Bahru.** Type 2 diabetes with early kidney disease. Language: தமிழ். Highlights glucose and kidney-safe medicine cautions.

All names and records are fictional. Add a visible "Synthetic data" badge.

## 6. Data models

**Care plan (output of the Decoder):**

```json
{
  "patient": {"name": "", "age": 0, "language": "ms"},
  "diagnoses": [{"name": "", "plain": "", "sourceSpan": [0, 0]}],
  "medications": [{
    "name": "", "dose": "", "route": "oral", "frequency": "BD",
    "times": ["08:00", "20:00"], "purpose": "", "foodNote": "",
    "status": "new|changed|continued|stopped", "sourceSpan": [0, 0]
  }],
  "appointments": [{"what": "", "when": "", "where": ""}],
  "warningSigns": [{"sign": "", "level": "call|emergency"}],
  "restrictions": [""],
  "conditionProfile": "heart_failure|diabetes|post_surgery|ckd|general"
}
```

**Check-in record:** date, weight, temperature, glucose, systolic and diastolic pressure, symptom flags (breathlessness 0 to 3, swelling, pain 0 to 10, dizziness, chest pain, confusion, bleeding, wound changes), doses taken, free-text note.

**Interaction table row:** drugA, drugB (or class), severity, mechanism in plain words, advice. Seed with about 30 well-established pairs, for example warfarin with NSAIDs or aspirin (bleeding), ACE inhibitor or ARB with spironolactone or potassium (high potassium), NSAID with ACE inhibitor and diuretic (kidney injury), nitrates with sildenafil (dangerous low blood pressure), simvastatin with clarithromycin, tramadol with SSRIs (serotonin syndrome), and metformin cautions in advanced kidney disease. The agent should double-check each pair against a reputable reference and keep wording conservative.

Persist everything in `localStorage` under one namespaced key. Provide "Reset demo" and "Export my data (JSON)".

## 7. LLM prompts (optional mode)

**Extraction prompt (system):** "You extract structured data from hospital discharge summaries. Return ONLY valid JSON matching the provided schema. Never invent medicines, doses or dates. If a field is missing, use null. For every item include the character span in the source text. Do not give medical advice."

**Explanation prompt (system):** "Rewrite the structured care plan in {language} at a {level} reading level for a patient and family caregiver. Keep medicine names and doses exactly as given. Do not add, remove or change any instruction. Keep sentences short. Never say a symptom is harmless."

**Guardrails in code (not just prompts):** validate JSON against the schema, verify every medicine name in the output appears in the source text (otherwise discard that item and flag it), and run the plain-language text through a check that no dose number was altered.

## 8. Rules engine (deterministic, explainable, configurable)

Implement as a plain JS module with a JSON rule table so each rule shows up in the "Why this score" panel. Thresholds below are illustrative defaults based on commonly published self-care guidance. The agent must label them "configurable, for demonstration, to be set by the treating clinician" and verify them against public guidance (for example heart failure and diabetes self-management guidance) before finalising.

**Universal red flags (any one = Red, emergency card):** chest pain, severe breathlessness at rest, fainting, new confusion, stroke signs (face droop, arm weakness, speech difficulty), heavy bleeding, thoughts of self-harm.

**Heart failure profile:**

- Weight gain of 1 kg or more overnight or 2 kg or more in 3 days: +3 points
- New or worse breathlessness on exertion: +2; when lying flat: +3
- New leg swelling: +2
- Systolic below 90 with dizziness: +3

**Diabetes profile:**

- Glucose below 4.0 mmol/L: Red (treat low sugar, then seek help)
- Glucose above 15 mmol/L, or above 11 with symptoms: +3
- Missed insulin or diabetes tablets two days running: +2

**Post-surgery profile:**

- Temperature 38.0 C or above: +3
- Wound redness, swelling or discharge: +3
- Calf pain or swelling: +4
- Pain not controlled by prescribed medicine (score 7 or above): +2

**Shared modifiers:** each missed critical dose in the last 48 hours: +1; unresolved interaction alert of severity Avoid: +2; two or more Amber days in a row: +2.

**Mapping:** 0 to 2 Green, 3 to 5 Amber, 6 or more or any red flag Red. Display the numeric score scaled to 0 to 100 for readability, while keeping the raw points visible in the explanation.

## 9. Build plan for the agent (phases with checks)

1. **Scaffold and design system.** Single file, CSS variables, layout shell with bottom tab bar (mobile) and side rail (desktop), tabs: Today, Plan, Check-in, Circle, Clinician, Trust. Check: renders cleanly at 390px and 1440px, light and dark.
2. **Data layer.** Personas, drug dictionary, interaction table, test set, `localStorage` wrapper, scenario script for the Time Machine.
3. **Decoder (rule-based engine first).** Parser, structured output, plain-language rendering, language switch, source-span highlighting. Check: all three personas decode with correct medicine counts.
4. **Medication Guardian.** Timeline, adherence, interaction checker with the "add OTC item" flow.
5. **Rules engine and Check-in.** Module, UI, "Why this score", trend chart, Time Machine, emergency card.
6. **Caregiver Circle and Clinician Brief.** Alert simulation, SBAR generator, print CSS.
7. **Trust Panel.** Evaluation runner and scenario tests that compute real numbers.
8. **Optional LLM mode.** Settings, key storage, prompts, validation, fallback.
9. **Polish.** Micro-interactions, empty states, accessibility pass (contrast, focus order, 44px touch targets, ARIA labels, reduced-motion), loading skeletons, copywriting pass, demo reset button.
10. **Submission assets** (Section 12).

## 10. The winning demo (3 scenarios, about 3 minutes)

1. **"Decode" (40s):** paste Pak Ahmad's messy English discharge summary. In seconds the plan appears. Flip to Bahasa Malaysia. Hover a sentence to show it highlighting the exact source line.
2. **"Protect" (40s):** type "ibuprofen" into the add-medicine box. CareLoop flags the combination with his heart and kidney medicines and explains why, in plain words.
3. **"Watch" (80s):** use the Time Machine. Day 1 and 2 are Green. On Day 3 his weight is up 2.4 kg and he reports breathlessness lying flat. The score jumps to Red, the caregiver phone preview buzzes, and the Clinician Brief generates itself. Open the "Why this score" panel to show the transparent reasoning.
4. **Close (20s):** show the Trust Panel with live evaluation numbers and the privacy and safety statement.

## 11. Acceptance tests

- All three personas decode with no missing medicines against the ground truth, in all four languages.
- The Avoid-level interaction fires for Mdm Tan if ibuprofen is added to her blood thinner.
- Time Machine: Pak Ahmad reaches Red on Day 3 and the caregiver alert fires exactly once.
- Any universal red flag triggers the emergency card with no network and no LLM.
- A 30-case rules test passes. The evaluation runner reports real numbers, not hard-coded ones.
- No console errors. The page works with the network disabled. Keyboard-only navigation works.
- Lighthouse accessibility score of 90 or higher.

## 12. Submission pack

**Project:** the deployed `index.html` (GitHub Pages) plus the repository. README with a screenshot, one-line pitch, how to run, architecture diagram, safety notes and the synthetic-data statement.

**Demo video (target 3 minutes):** 0:00 to 0:25 the problem (a real-feeling discharge page, a worried family); 0:25 to 2:30 the three scenarios of Section 10 with voiceover; 2:30 to 3:00 trust, privacy and where this goes next. Record at 1080p with a clean, zoomed browser window and captions.

**One-page PDF:** left column: problem, solution, four loops. Right column: screenshot of the Time Machine Red moment, key features, architecture strip (AI language layer plus rules engine), verified statistics with citations, and the roadmap. Keep it to one page.

**Code PDF:** generate by printing the source with line numbers and a monospace font (for example, a small script that wraps `index.html` in a styled HTML page and prints to PDF). Include the repository link on the first page.

## 13. Pitch narrative and judging alignment

- **Creativity:** the Time Machine demo and a hybrid design where the AI explains and the rules decide.
- **Feasibility:** runs today in any browser, no server, and a clear path to hospital pilots.
- **Technical depth:** structured extraction with source-span traceability, schema and hallucination guards, multilingual output, a configurable rules engine, a live evaluation harness.
- **Clinical insight:** targets the post-discharge window, uses condition-specific signs, SBAR output, clinician-in-the-loop thresholds.
- **Real-world impact:** multilingual access, caregiver involvement, early warning before readmission.

## 14. Safety, ethics and roadmap

- Decision support, not diagnosis. Clinicians own thresholds. Show this on every screen that gives guidance.
- Synthetic data only. Local-first storage. In LLM mode, warn the user before any text leaves the device.
- Limitations to state openly: demo-scale drug database, rule thresholds not clinically validated, translations need review by qualified translators before any real use.
- Roadmap: licensed drug database, FHIR import of discharge data, wearable inputs (weight scale, glucometer, pulse oximeter), clinician-configured thresholds, pilot with a community clinic and a validation study.

## 15. Visual design system

- **Mood:** calm, trustworthy, human. Warm paper background (#FAF7F2), deep teal primary (#0F5C5A), soft sage secondary, coral for Amber (#E8913A) and a clear red for Red (#C8372D). Green status uses a muted leaf green (#3E8E5A). Never rely on colour alone: pair every status with an icon and a word.
- **Type:** Fraunces for headings, Inter for UI, Noto Sans SC and Noto Sans Tamil for those languages (Google Fonts). Base size 17px, generous line height, large numerals for vitals.
- **Shape and motion:** 16px radius cards, subtle shadows, 200ms ease transitions, animated score ring, respect `prefers-reduced-motion`.
- **Voice:** warm and plain. "Let's check how you're doing today" instead of clinical jargon. Short sentences. Always tell the person what to do next.
- **Icons:** a simple consistent stroke-based set drawn inline as SVG.

## 16. Risks and fallbacks

- **LLM unavailable or slow:** Demo Mode is the default and the demo never depends on a network call.
- **Translation quality:** limit pre-translated content to the bundled personas and flag the rest as machine-generated draft.
- **Scope creep:** F1 to F4 are the minimum winning product. Cut F8, then F5, before touching F1 to F4.
- **Time:** confirm the submission deadline on the DSH Hacks V2 page and work backwards. Reserve the final 20% of time for polish and the submission pack.

# Implementation Guide (how to actually build it)

Sections 17 to 25 turn the blueprint into buildable detail: code structure, algorithms, data, screens, prompts and tests. Where this guide and Sections 0 to 16 differ, this guide is more specific and wins.

## 17. Code architecture inside the single file

Organise `index.html` into clearly marked regions so the agent (and a human reader of the code PDF) can navigate it.

```text
index.html
  <head>        meta viewport, fonts (Google Fonts), <style> design tokens + components + print CSS
  <body>        app shell: header, <main id="view">, tab bar, emergency overlay, toast container, modal root
  <script id="data-personas" type="application/json">   3 personas + discharge texts + ground truth
  <script id="data-drugs" type="application/json">      ~60 drug entries
  <script id="data-interactions" type="application/json"> ~30 interaction rows
  <script id="data-i18n" type="application/json">       UI strings + sentence templates (en, ms, zh, ta)
  <script id="data-rules" type="application/json">      rules table per condition profile
  <script> (module-style, one IIFE)
     1. Store        state + localStorage persistence + subscribe()
     2. i18n         t(key, vars), setLanguage()
     3. Parser       parseDischarge(text) -> CarePlan
     4. Explainer    renderPlain(carePlan, lang, level) -> sentences with sourceSpans
     5. Guardian     checkInteractions(meds) -> alerts[]
     6. Rules        scoreCheckin(profile, history, today) -> {points, level, factors[]}
     7. Charts       renderTrend(svgEl, series, thresholds)
     8. Views        renderToday / renderPlan / renderCheckin / renderCircle / renderClinician / renderTrust
     9. Demo         timeMachine script, reset, persona loader
    10. LLM          optional adapter + validators + fallback
    11. Boot         init store, router (hash-based), first render
```

**State shape (single source of truth):**

```js
const state = {
  persona: 'ahmad',            // active demo persona id
  lang: 'en', level: 'simple', // UI + explanation language, reading level
  carePlan: null,              // CarePlan (Section 6)
  doses: {},                   // {'2026-10-22|metformin|08:00': true}
  extraMeds: [],               // OTC items the user adds
  checkins: [],                // Check-in records, newest last
  alerts: [],                  // {id, ts, level, reason, notifiedCaregiver:boolean}
  demoDay: 0,                  // Time Machine day offset
  settings: { llmKey: '', llmEnabled: false, theme: 'auto' }
};
```

**Rules for the code:**

- Pure functions for Parser, Guardian, Rules and Explainer so they can be unit-tested in the Trust Panel without touching the DOM.
- All rendering through small template functions returning HTML strings, with one `escapeHtml()` helper applied to every piece of user-provided text. No `innerHTML` with unescaped input.
- One `render()` call after any state change. Keep view code under about 80 lines each by pulling shared pieces (card, chip, ring, button) into helpers.
- Hash router: `#/today`, `#/plan`, `#/checkin`, `#/circle`, `#/clinician`, `#/trust`, `#/settings`.
- Every interactive element is a real `button`/`input`/`label`. Focus rings visible. Minimum 44px touch target.

## 18. The Discharge Parser, step by step

Goal: turn messy free text into a `CarePlan` with no network. Accuracy on the bundled test set matters more than cleverness.

**Step 1. Normalise.** Convert line endings, collapse repeated spaces, keep a copy of the original so every extracted item can store `sourceSpan = [startIndex, endIndex]` into it. Never edit the original string; build a normalised copy plus an index map.

**Step 2. Split into sections** with a case-insensitive header regex. Recognise these header aliases and map them to canonical sections:

- diagnosis, diagnoses, principal diagnosis, discharge diagnosis, problem list
- medications, discharge medications, medicines, drugs on discharge, TCA meds
- follow-up, follow up, appointments, review
- advice, instructions, discharge advice, when to seek help, warning signs, red flags
- diet, activity, restrictions

Text before the first header is treated as "header/demographics" (name, age, sex).

**Step 3. Extract medicines.** For each line in the medications section:

```js
const FREQ = {
  OD: ['08:00'], QD: ['08:00'], 'ONCE DAILY': ['08:00'], MANE: ['08:00'], ON: ['21:00'], NOCTE: ['21:00'],
  BD: ['08:00','20:00'], BID: ['08:00','20:00'], 'TWICE DAILY': ['08:00','20:00'],
  TDS: ['08:00','14:00','20:00'], TID: ['08:00','14:00','20:00'],
  QID: ['07:00','12:00','17:00','22:00'], PRN: [], STAT: []
};
// Line pattern (case-insensitive), then tolerate missing pieces:
// <name> <dose><unit> [route] <frequency> [duration] [free-text note]
const DOSE_RE = /(\d+(?:\.\d+)?)\s?(mcg|µg|mg|g|ml|iu|units?)\b/i;
const STATUS_RE = /\b(new|started|start|changed|increased|reduced|dose adjusted|continue|continued|stop|stopped|discontinue)\b/i;
```

1. Strip bullets and numbering (`1.`, `-`, `*`).
2. Find the drug name by matching against the bundled dictionary (generic names and common brand names, accent- and case-insensitive, Levenshtein distance 1 allowed for names of 6 or more letters). A line with no dictionary hit but a dose pattern is kept as an "unrecognised medicine" with a warning chip rather than dropped.
3. Pull dose with `DOSE_RE`, frequency by scanning for keys of `FREQ` (longest key first), status with `STATUS_RE` (default `continued`; the words start, new, added mean `new`; increase, reduce, adjust mean `changed`; stop, discontinue mean `stopped`).
4. Food notes: detect "after food", "with meals", "before food", "at night", "empty stomach" and fall back to the dictionary default.
5. Times: use the `FREQ` mapping but let the person adjust in the Plan view.

**Step 4. Extract warning signs.** Split the advice section into sentences. A sentence is a warning sign if it contains a trigger phrase (come back, return, go to the emergency, call, seek medical, if you experience) or a symptom lexicon hit (breathless, chest pain, swelling, fever, bleeding, dizziness, wound, vomiting, black stool). Classify as `emergency` when it contains chest pain, cannot breathe, faint, unconscious, severe bleeding, stroke words; otherwise `call`.

**Step 5. Extract appointments.** Regex for dates (`dd/mm/yyyy`, `dd Mon yyyy`, `Mon dd`) plus the nearest clinic or department word (cardiology, endocrine, SOPD, clinic, wound care, physiotherapy).

**Step 6. Detect the condition profile** by keyword scoring over the diagnoses: heart failure (HF, cardiac failure, LVEF, cardiomyopathy), diabetes (DM, T2DM, HbA1c, insulin, metformin), post-surgery (op, post-op, arthroplasty, fracture fixation, appendicectomy, wound), CKD (CKD, eGFR, creatinine). Multiple profiles can be active at once; the rules engine merges them.

**Step 7. Validate.** Reject medicines with dose of 0, flag a dose that is more than 10 times the dictionary's typical maximum as "check this dose with your pharmacist", and require at least one medicine or one diagnosis, otherwise show a friendly "We couldn't read this, try the sample" state.

**Step 8. Return** the `CarePlan` and a `confidence` for each item (1.0 dictionary hit and dose and frequency found, 0.7 missing one, 0.4 missing two). Low-confidence items get a yellow "please check" chip in the UI.

### Drug dictionary entry format

```json
{
  "generic": "furosemide",
  "brands": ["lasix", "frusemide"],
  "class": "loop_diuretic",
  "purposeEn": "removes extra fluid so you breathe easier and swell less",
  "purposeMs": "mengeluarkan lebihan cecair supaya anda bernafas lebih lega",
  "purposeZh": "排出多余液体，让您呼吸更轻松、减少水肿",
  "purposeTa": "அதிகப்படியான துரவத்தை வெளியேற்றி வீக்கத்தைக் குறைக்கிறது",
  "foodNote": "best taken in the morning",
  "typicalMaxDailyMg": 600,
  "watch": ["dizziness", "very little urine", "muscle cramps"]
}
```

Cover at least these classes so the three personas and common OTC checks work: ACE inhibitors and ARBs, beta blockers, loop and potassium-sparing diuretics, statins, antiplatelets and anticoagulants (aspirin, clopidogrel, warfarin, apixaban, rivaroxaban), metformin, sulfonylureas, insulin, SGLT2 inhibitors, DPP-4 inhibitors, paracetamol, NSAIDs (ibuprofen, diclofenac, naproxen, mefenamic acid), tramadol, PPIs, antibiotics (amoxicillin, clarithromycin, ciprofloxacin), nitrates, digoxin, amlodipine, and common herbal or supplement items. Have the agent translate the purposes carefully and mark them as "draft translation, review needed" in the Trust Panel.

## 19. Medication Guardian and Rules Engine: code-level spec

### Interaction checker

```js
// interaction row: {a:'warfarin', b:'class:nsaid', severity:'avoid', why:'...', advice:'...'}
function expand(med){            // -> set of tokens: generic name, class, brand names
  const d = DRUGS.find(x => x.generic===med.name || x.brands.includes(med.name));
  return new Set([med.name, d && 'class:'+d.class, ...(d?d.brands:[])].filter(Boolean));
}
function checkInteractions(meds){
  const alerts = [], tokens = meds.map(expand);
  for (let i=0;i<meds.length;i++) for (let j=i+1;j<meds.length;j++){
    for (const r of INTERACTIONS){
      const hit = (tokens[i].has(r.a)&&tokens[j].has(r.b)) || (tokens[i].has(r.b)&&tokens[j].has(r.a));
      if (hit) alerts.push({sev:r.severity, a:meds[i].name, b:meds[j].name, why:r.why, advice:r.advice});
    }
  }
  // duplicates: same class twice (e.g. two NSAIDs, two ACE inhibitors)
  // triple-whammy: nsaid + (ace|arb) + diuretic -> one combined 'avoid' alert
  return dedupe(alerts).sort(bySeverity);
}
```

The "add a medicine" box accepts free text, runs it through the same name matcher as the parser, and re-runs `checkInteractions` on `carePlan.medications + extraMeds`. Unknown products show "We don't recognise this. Ask your pharmacist before taking it with your prescribed medicines."

### Scoring function

```js
// rule: {id, profile, when:(c,h)=>bool, points, label, redFlag?:bool}
function scoreCheckin(profiles, history, today){
  const factors = []; let points = 0, red = false;
  for (const r of RULES.filter(r => r.profile==='universal' || profiles.includes(r.profile))){
    if (r.when(today, history)) {
      factors.push({id:r.id, label:r.label, points:r.points});
      points += r.points; if (r.redFlag) red = true;
    }
  }
  const level = red || points >= 6 ? 'red' : points >= 3 ? 'amber' : 'green';
  return { points, level, factors, score100: Math.min(100, Math.round(points*100/10)) };
}
// Example rules (history = previous check-ins, newest last)
{ id:'hf_weight', profile:'heart_failure', points:3,
  label:'Weight up 2 kg or more in 3 days',
  when:(c,h)=>{ const base=h.slice(-3)[0]?.weight; return base && c.weight-base>=2; } },
{ id:'dm_low', profile:'diabetes', points:6, redFlag:true,
  label:'Blood sugar below 4.0 mmol/L', when:c=>c.glucose!=null && c.glucose<4.0 },
{ id:'post_fever', profile:'post_surgery', points:3,
  label:'Temperature 38.0 C or above', when:c=>c.temp>=38.0 },
{ id:'missed_critical', profile:'universal', points:1,
  label:'Missed a critical dose in the last 48 hours', when:(c)=>missedCritical(48)>0 }
```

Set `critical: true` in the dictionary for blood thinners, insulin, diuretics in heart failure, and anti-rejection or similar drugs.

**Action text per level** (translated in all four languages):

- Green: "You're on track. Keep taking your medicines and check in tomorrow."
- Amber: "Please call your clinic today. We've told Aisyah." (include the clinic phone number from the care plan if present)
- Red: "Get help now. Call 999 or go to the nearest emergency department." with a large call button.

### Trend chart (inline SVG, no library)

Draw by hand: a 14-day x-axis, y-axis for the selected metric (weight, glucose, temperature, score), threshold bands shaded softly, points coloured by level with an icon, adherence dots along the bottom. Use `viewBox="0 0 640 260"` and `preserveAspectRatio`, labels at 12px minimum, and `<title>` elements on points for accessibility.

### Time Machine (scripted scenario)

Store a per-persona array of day records, each with check-in values and doses taken:

| Day | Weight | Breathlessness | Other | Expected level |
| --- | --- | --- | --- | --- |
| 0 (discharge) | baseline | none | all doses taken | Green |
| 1 | +0.3 kg | none | all doses taken | Green |
| 2 | +0.9 kg | on stairs | missed evening furosemide | Amber (3 to 5 points) |
| 3 | +2.4 kg | when lying flat | leg swelling | Red (6 or more points) |

A "Next day" button advances `state.demoDay`, injects that day's check-in, runs the rules, and fires the alert pipeline: toast, caregiver message preview, and Clinician Brief refresh. Add a "Rewind" and "Reset" button so the presenter can rerun the demo instantly. Pak Ahmad's weight on Day 0 is 68.0 kg; Mdm Tan and Priya get their own scripts (fever and wound redness on Day 4; glucose swing on Day 3).

## 20. Sample data the agent must create

### Hero discharge summary (Pak Ahmad, fictional)

Use deliberately messy, realistic clinician style with abbreviations:

```text
DISCHARGE SUMMARY
Name: Ahmad bin Hassan   Age: 72M   Ward: 5B   LOS: 6 days
Principal Dx: Acute decompensated heart failure (LVEF 35%), precipitated by non-compliance
Other Dx: T2DM (HbA1c 8.4%), HTN, CKD stage 3a (eGFR 52)

MEDICATIONS ON DISCHARGE
1. Furosemide 40mg OD mane - NEW
2. Bisoprolol 2.5mg OD - NEW
3. Perindopril 4mg OD - continue
4. Spironolactone 25mg OD - NEW
5. Metformin 500mg BD with meals - dose reduced (eGFR)
6. Gliclazide 30mg OD before breakfast - continue
7. Atorvastatin 40mg ON - continue
8. Aspirin 75mg OD after food - continue
STOPPED: Diclofenac (avoid NSAIDs)

ADVICE
Daily weight every morning after passing urine. Fluid restriction 1.5L/day. Low salt diet.
Return to ED if SOB at rest, chest pain, fainting or weight gain >2kg in 3 days.
Call HF clinic if increased leg swelling, orthopnoea, dizziness or reduced urine output.

FOLLOW-UP
HF clinic 29/10/2026. Endocrine 12/11/2026. Bloods (U&E) in 1 week at klinik kesihatan.
```

Ground truth: 8 active medicines plus 1 stopped, 4 diagnoses, 3 appointments, 7 warning signs (3 emergency, 4 call), profiles `heart_failure`, `diabetes`, `ckd`. Writing the same style for Mdm Tan (hip hemiarthroplasty, enoxaparin or apixaban, paracetamol, tramadol, omeprazole, calcium and vitamin D, wound care and DVT warning signs) and Priya (T2DM with CKD, metformin, dapagliflozin, gliclazide, amlodipine, losartan, insulin glargine) is the agent's job.

The demo interaction moment for Pak Ahmad: adding ibuprofen should trigger an Avoid alert (NSAID with an ACE inhibitor and a diuretic and kidney disease, the "triple whammy", plus fluid retention in heart failure) and a Caution alert with aspirin. Adding a potassium supplement or salt substitute with perindopril plus spironolactone should trigger an Avoid alert for high potassium.

### Synthetic test set for the Trust Panel

Generate 20 discharge summaries by varying the three hero templates: different drugs, doses, abbreviations (OD/QD/mane, BD/BID, ON/nocte), section order, header wording, bullet styles, typos, and one Bahasa Malaysia sentence mixed in ("makan ubat selepas makan"). Store the expected output beside each. Hold out 5 of them as an unseen set that the parser was not tuned on, and report results on both the tuning set and the unseen set honestly.

**Metrics the evaluation runner computes:**

- Medicine extraction precision and recall (match on generic name).
- Dose exact-match rate, frequency exact-match rate.
- Warning-sign recall (match by symptom lexicon category).
- Status accuracy (new, changed, continued, stopped).
- Rules engine: 30 scenario cases of the form (profile, history, check-in) to expected level, shown as a pass or fail grid.
- Safety property tests: for every red-flag symptom, the emergency card must appear; the Explainer must never alter a dose string present in the plan (checked by regex over every output sentence).

## 21. Screen-by-screen UI spec

**Global shell.** Mobile first. Top bar: CareLoop wordmark, active patient chip, language selector (EN / BM / 中文 / தமிழ்), theme toggle, "Demo controls" drawer. Bottom tab bar on phone, left rail on desktop. A persistent red "I feel unwell" button above the tab bar.

**Today (home).** Greeting with the patient's name. Large status ring showing today's level and score. "Next medicine" card with a single big "Taken" button. Today's three tasks (check-in, weigh yourself, evening medicines). Upcoming appointment card with a map-style placeholder. Caregiver badge showing who is notified.

**Plan.** Top: tabs Diagnoses, Medicines, Appointments, Warning signs. Side-by-side on desktop: original text on the left with highlighted spans, plain-language plan on the right. Medicine cards show name and dose in large type, purpose, when, food note, status chip (new, changed, stopped) and a confidence chip if low. A reading-level switch and language switch live at the top of this view. "Add a medicine or supplement" button opens the interaction check modal.

**Check-in.** One question per screen with a progress bar, big chips, gentle wording. Numeric inputs for weight, temperature, glucose with steppers and unit labels. End screen shows the result: score ring, level, "Why this score" accordion listing each factor and its points, action text, and "Tell my caregiver" (auto when Amber or Red). Below, the 14-day trend chart with a metric selector.

**Circle (caregiver).** Header showing the patient photo placeholder and today's level. Timeline of events (doses missed, check-ins, alerts). A phone mock showing the simulated message the caregiver receives. "Call" and "Message" buttons. A QR code (generated in pure JS or with a small CDN library such as qrcode-generator) that opens a read-only view link, with a note that real sharing needs a server and is part of the roadmap.

**Clinician.** A paper-like A4 preview: patient header, SBAR blocks, medicine table with adherence per drug, embedded trend chart, flagged events list, "Suggested action" box. Buttons: Copy as text, Print / Save as PDF. Footer: "Decision support only. Generated from patient-reported data."

**Trust.** Cards: Evaluation results (run button, progress, metrics table), Rules tests (pass/fail grid), Privacy and data flow diagram, Known limitations, Translation review status, Sources for thresholds.

**Emergency overlay.** Full screen, high contrast, huge "Call 999" button (tel link), a collapsible card listing medicines and diagnoses to read to the paramedic, and a "This was a mistake" dismiss that requires a second tap.

**Empty, loading and error states** are designed for every view: friendly illustration made from simple SVG shapes, one sentence, one next action.

## 22. Multilingual and accessibility implementation

- **i18n structure:** one JSON object keyed by string id, each with `en`, `ms`, `zh`, `ta`. Sentence templates use placeholders, for example `"take_med": {"en": "Take {drug} {dose} {when}.", "ms": "Ambil {drug} {dose} {when}.", "zh": "{when}服用{drug} {dose}。", "ta": "{drug} {dose} {when} எடுக்கவும்."}`. Drug names and dose strings are inserted untouched.
- **Fonts:** load Noto Sans SC and Noto Sans Tamil only when that language is selected, to keep first load fast. Set `lang` on the `html` element on every switch so screen readers pronounce correctly.
- **Reading levels:** Simple = sentences under 12 words, no medical terms unless followed by an everyday explanation; Standard = adds the clinical term in brackets. Implemented as two template sets, not by generating text.
- **Voice:** use `speechSynthesis` to read the plan aloud in the chosen language where the browser supports it, and `SpeechRecognition` for check-in answers with a typed fallback. Feature-detect and hide the buttons if unsupported.
- **Accessibility checklist:** WCAG AA colour contrast, never colour alone, labels on all inputs, `aria-live="polite"` on score and alert updates, focus trap in modals and the emergency overlay, `prefers-reduced-motion`, text scaling to 200 percent without layout breaks, and a high-contrast theme.

## 23. Optional LLM mode: the integration in detail

**Why include it.** It handles discharge summaries in styles the parser has never seen and produces more natural explanations. It is optional so the demo never depends on it.

**Request flow:**

1. User pastes a key in Settings and turns on "Use AI". Show a plain warning: "Your discharge text will be sent to the AI provider. Use only the sample or non-identifying text."
2. `extractWithLLM(text)` sends the Section 7 extraction prompt plus the schema and the text. Ask for JSON only.
3. Parse the response with `JSON.parse` inside try/catch. Strip code fences if present.
4. **Validate** with a small hand-written schema checker (types, required fields, allowed enums).
5. **Hallucination guard:** for each medicine, check that its name (or a dictionary brand name) appears in the source text, case-insensitively. For each dose, check the exact dose string appears in the source line. Remove failures and list them in a "We removed items we could not find in your summary" notice.
6. **Merge** with the rule-based result: keep the union, but mark items found by only one engine with a "check this" chip. Items found by both get high confidence.
7. On any failure (network, parse, validation), fall back to the rule-based result and show a small notice.

```js
async function callLLM(system, user){
  const res = await fetch(settings.llmEndpoint, {
    method:'POST',
    headers:{'content-type':'application/json', 'x-api-key': settings.llmKey /* adapt to provider */},
    body: JSON.stringify({ model: settings.llmModel, max_tokens: 2000, system,
      messages:[{role:'user', content:user}] })
  });
  if(!res.ok) throw new Error('LLM '+res.status);
  return res.json();
}
```

Let the user choose the provider and endpoint in Settings and keep the adapter in one function so it can be swapped. Browser-side calls to some providers may be blocked by CORS; if so, show a clear message and keep Demo Mode working. Never embed a real key in the file or the repository.

**What the LLM may and may not do:**

- May: extract, explain, translate, draft the clinician summary wording, answer "what does this word mean".
- May not: assign or change risk levels, decide whether to show the emergency card, add or alter doses, give a diagnosis. These stay in deterministic code.

## 24. Testing, deployment and the code PDF

**Manual test script (run before recording the video):** load each persona; decode in all four languages; add ibuprofen to Pak Ahmad and to Mdm Tan; run the Time Machine for all three personas; trigger each universal red flag; print the Clinician Brief to PDF; turn off the network and repeat the decode; resize to 390, 768 and 1440px; tab through the whole UI with the keyboard; switch to dark mode.

**Automated checks (in the Trust Panel and as a `?test=1` URL flag that logs to the console):** parser metrics, rules tests, interaction tests (expected pairs fire, unrelated pairs do not), i18n completeness (every key has all four languages), escape-HTML test with `<script>` in a medicine name.

**Deployment:** put `index.html` and `README.md` in a public GitHub repository, enable GitHub Pages on the main branch, and test the live URL on a phone. Add a LICENSE (MIT) and an `/assets` folder with screenshots for the README.

**Code PDF generator (Node or Python, run once):**

1. Read `index.html`.
2. Escape it and wrap each line in a numbered, monospace `div` (font size 8 to 9pt, tab width 2).
3. Add a cover page: project name, one-line pitch, repository URL, live demo URL, team name, and a short table of contents mapping the region markers from Section 17 to line numbers.
4. Print to PDF with a headless browser (for example Playwright or Puppeteer `page.pdf`, A4, margins 12mm). Check the page count is sensible and that long lines wrap instead of being cut.

**One-page PDF:** build as an A4 HTML page, print to PDF, and check that nothing spills onto a second page. Use real screenshots taken from the finished prototype, not mockups.

**Demo video production:** record with the browser zoomed to 125 percent at 1080p, hide bookmarks and other tabs, use the Demo drawer to reset before each take, add captions, keep each scenario to the timings in Section 10, and end with the live URL and repository link on screen.

## 25. Prompt pack for the build agent

Give the agent these in order, attaching this whole document each time.

1. "Read the document fully. Restate the architecture and the build order in your own words and list any ambiguity. Do not write code yet."
2. "Phase 1 and 2: create the scaffold, design system and all bundled data (personas, drugs, interactions, rules, i18n). Show the data files and wait."
3. "Phase 3: implement the Parser and Explainer with the unit tests from Section 24. Report the metrics on the tuning set and the unseen set."
4. "Phase 4 and 5: Guardian, Rules engine, Check-in, trend chart, Time Machine and emergency overlay. Run the Day 0 to Day 3 script and show the levels."
5. "Phase 6 and 7: Caregiver Circle, Clinician Brief, Trust Panel."
6. "Phase 8: optional LLM mode with validation and fallback."
7. "Phase 9: polish and accessibility audit. List every issue found and fixed."
8. "Phase 10: generate the README, the one-page PDF HTML, the code PDF script and the demo video shot list."

After each step, ask the agent to run the matching checks from Section 11 and paste the results before continuing. If anything fails, fix it before moving on.
