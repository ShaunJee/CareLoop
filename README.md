# CareLoop 🩺
### Post-Discharge Recovery & Patient Safety Guardian
**DSH Hacks V2 Submission · Theme: AI x Healthcare · Prize Pool: $100k+**

> **The One-Line Pitch:**  
> **CareLoop turns a confusing hospital discharge into a safe, understandable recovery plan in your own language, and watches the first 30 days so a family and a doctor know before things go wrong.**

---

## 🌟 Overview & Clinical Motivation

The days immediately following hospital discharge are among the most vulnerable and dangerous in modern healthcare:
- **1 in 5 Medicare Patients** are readmitted within 30 days (*Jencks et al., NEJM 2009*).
- **Over 50% of adult patients** experience at least one medication error or misunderstanding post-discharge (*Kripalani et al., JAMA 2007*).
- **The Health Literacy Gap:** Discharge summaries are written in compressed, abbreviated clinical English (`LVEF 35%`, `TCA Meds`, `OD mane`). Vulnerable patients and family caregivers leave with little comprehension of what changed in their medications, which warning signs matter, or when to seek urgent help.
- **Silent Outpatient Deterioration:** Heart failure fluid congestion and post-surgical wound infections creep up quietly over 72 hours. Without continuous remote surveillance, the patient only returns once they are in critical distress.

**CareLoop** bridges this dangerous gap with an offline-first, multilingual platform combining an **AI translation layer** with a **deterministic clinical rules engine**.

---

## 🔄 The Four Continuous Care Loops

```
     ┌─────────────────────────────────────────────────────────────┐
     │                      HOSPITAL DISCHARGE                     │
     └──────────────────────────────┬──────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  LOOP 1 · DECODE (Clinical NLP Parser)                                       │
│  Transforms unstructured, messy clinical text into structured care plans.   │
│  Plain-language explanations in English, Bahasa Malaysia, 中文, & தமிழ்.      │
│  100% Traceability: Hover any sentence to highlight the original source line. │
└───────────────────────────────────┬──────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  LOOP 2 · PROTECT (Medication Guardian)                                      │
│  Daily dosing timeline with adherence streak ring.                           │
│  Pre-ingestion interaction checker catching fatal OTC drug conflicts         │
│  (e.g., NSAID + Anticoagulant, Triple Whammy acute renal failure).          │
└───────────────────────────────────┬──────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  LOOP 3 · WATCH (60s Daily Check-in & Rules Engine)                          │
│  Condition-aware check-in (weight, BP, glucose, breathlessness, edema).      │
│  Transparent 0–100 Recovery Risk Score with auditable factor attribution.    │
│  Time Machine: Simulates multi-day recovery catching silent deterioration.   │
└───────────────────────────────────┬──────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│  LOOP 4 · CONNECT (Caregiver Circle & Clinician SBAR Brief)                  │
│  Immediate SMS / WhatsApp alerts sent to designated family caregivers.       │
│  One-tap auto-generated SBAR clinical summary ready for doctor review/print. │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛡️ Safety-First Hybrid Architecture

CareLoop adheres to a strict clinical engineering principle:
- **The AI Layer Understands & Explains:** Handles natural language parsing, reading-level simplification, and multilingual translation.
- **The Deterministic Rules Engine Decides:** **100% of clinical safety decisions**, drug-drug interactions, emergency alerts, and risk levels are computed in transparent, auditable, deterministic code.
- **Zero Hallucination Tolerance:** The AI layer can **NEVER** lower a risk score, suppress an emergency flag, or alter medication dosages.
- **Always-Present Emergency Safety Net:** A persistent red *"I Feel Unwell"* button is accessible from every screen, instantly displaying 999/112 emergency calling and an unmissable paramedic handover card listing the patient's active diagnoses and current drugs.

---

## 🚀 Key Prototype Features

| Feature | Description | Clinical Rationale |
| :--- | :--- | :--- |
| **Discharge Decoder** | Free-text and sample summary ingestion with regex + 68-drug clinical dictionary. Multi-lingual toggle (EN, BM, ZH, TA). | Eliminates language and health literacy barriers. |
| **Source-Span Highlighting** | Hovering over any care plan card highlights the exact source lines in the primary clinical text. | Builds trust with patients and clinicians via full provenance. |
| **Medication Guardian** | Timeline scheduler with adherence tracking + 32-row interaction matrix catching prescription & OTC clashes. | Prevents accidental double-dosing and fatal drug interactions. |
| **Time Machine** | Interactive day-by-day simulator fast-forwarding recovery from Day 0 baseline to Day 3 clinical deterioration. | Demonstrates how the system catches decompensation before readmission. |
| **Caregiver Circle** | Real-time family notification preview with simulated SMS bridge and offline cryptographically-rendered QR pass. | Keeps busy family caregivers in the loop without app friction. |
| **Clinician SBAR Brief** | One-tap handover brief in standard medical format (Situation, Background, Assessment, Recommendation) with A4 print styling. | Saves doctor time during outpatient reviews. |
| **Live Trust Panel** | On-device test runner executing 20 synthetic summaries (15 tuning + 5 held out) and 30-case rules test. | Zero fabricated metrics: all accuracy numbers are live. |

---

## 💻 How to Run Locally

CareLoop is built as a single, self-contained `index.html` application with **zero frameworks, zero build steps, and zero external runtime dependencies**. It works completely offline.

### Option 1: Direct Browser Launch
Simply double-click `index.html` in your file explorer, or drag it into any modern web browser (Chrome, Edge, Safari, Firefox).

### Option 2: Local HTTP Server (Recommended)
```bash
# Using Python:
python -m http.server 8000

# Using Node.js:
npx serve .
```
Then navigate to `http://localhost:8000` in your browser.

### Option 3: Automated Self-Test Mode
Add `?test=1` to the URL to run the entire verification suite on load:
```text
http://localhost:8000/index.html?test=1
```
Open your browser Developer Console (`F12`) to view the live precision/recall table and rule checks.

---

## 🧪 Verified Test Results

| Test Dimension | Scope | Result | Status |
| :--- | :--- | :--- | :--- |
| **Discharge Parser (Tuning Set)** | 15 synthetic summaries | **100.0% Precision · 100.0% Recall · 100.0% F1** | **PASS** |
| **Discharge Parser (Held-Out Set)** | 5 unseen summaries | **100.0% Precision · 100.0% Recall · 100.0% F1** | **PASS** |
| **Dose Preservation Fidelity** | Extracted dosage strings | **100.0% Exact Match Rate** | **PASS** |
| **Deterministic Rules Engine** | 30 clinical test cases | **30 / 30 Cases Passing (100%)** | **PASS** |
| **XSS & Injection Protection** | String sanitization | **100% Escaped via `escapeHtml()`** | **PASS** |

*Full verification details and external audit remediation are documented in [TEST_REPORT.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/tests/TEST_REPORT.md).*

---

## 📁 Repository Categorization & File Map

CareLoop is organized into dedicated, logical directories for clean navigation and submission packaging:

```text
CareLoop/
├── index.html                   # 🚀 Root click-to-run interactive application (for judges & GitHub Pages)
├── test_runner.js               # ⚡ CLI test runner shortcut (executes tests/test_runner.js)
├── README.md                    # 📖 Project documentation & architecture guide
│
├── 📂 prototype/                # 📱 Working Prototype Codebase
│   └── index.html               # Single-file zero-build HTML5/JS/CSS client (offline-first)
│
├── 📂 hack_questions/           # 📋 Hackathon Requirements & Specification
│   ├── HACKATHON_INSTRUCTIONS.md # DSH Hacks V2 prompt, guidelines, and evaluation rubrics
│   └── BLUEPRINT.md             # 25-section clinical and technical architecture blueprint
│
├── 📂 submission_deliverables/  # 🏆 Official Hackathon Submission Pack
│   ├── CareLoop_OnePager.pdf    # One-page executive summary PDF for judges
│   ├── CareLoop_Source_Code.pdf # Full syntax-highlighted code PDF with TOC & line numbers (2.36 MB)
│   ├── onepager.html            # Print-ready A4 HTML template for the one-pager document
│   └── demo_script.md           # 3-minute video presentation script and storyboard
│
├── 📂 audit/                    # 🔍 External Quality & Clinical Audit
│   ├── AUDITOR_PROMPT.md        # Comprehensive rubric prompt for external AI / judge audits
│   ├── AUDIT_DOSSIER.md         # Clinical grounding evidence, benchmark figures, and citations
│   └── EXTERNAL_AI_AUDIT_REPORT.md # Official audit evaluation report (Scored: 96 / 100)
│
├── 📂 tests/                    # 🧪 Automated Testing & Safety Verification
│   ├── test_runner.js           # Deterministic test runner (F1 parser test, 30 rules cases, XSS check)
│   └── TEST_REPORT.md           # Empirical verification results and precision/recall audit log
│
└── 📂 scratch/                  # 🛠️ Build Automation & Generation Utilities
    ├── make_code_pdf.py         # Headless browser script that formats and prints submission PDFs
    ├── code_print.html          # High-density printable HTML layout used for code PDF export
    └── find_lines.js            # Module boundary scanner utility
```

### Quick Access Links:
- **Interactive App:** [index.html](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/index.html) or [prototype/index.html](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/prototype/index.html)
- **One-Pager PDF:** [CareLoop_OnePager.pdf](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/submission_deliverables/CareLoop_OnePager.pdf)
- **Source Code PDF:** [CareLoop_Source_Code.pdf](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/submission_deliverables/CareLoop_Source_Code.pdf)
- **Demo Script:** [demo_script.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/submission_deliverables/demo_script.md)
- **Clinical Audit Report (96/100):** [EXTERNAL_AI_AUDIT_REPORT.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/audit/EXTERNAL_AI_AUDIT_REPORT.md)
- **Auditor Evidence Dossier:** [AUDIT_DOSSIER.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/audit/AUDIT_DOSSIER.md)
- **Automated Test Report:** [TEST_REPORT.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/tests/TEST_REPORT.md)
- **Hackathon Prompt & Rules:** [HACKATHON_INSTRUCTIONS.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/hack_questions/HACKATHON_INSTRUCTIONS.md)
- **Technical Blueprint:** [BLUEPRINT.md](file:///c:/Users/shaun/OneDrive/Desktop/Hackathons/Careloop/hack_questions/BLUEPRINT.md)

---

## 🔒 Safety, Ethics & Limitations

- **Clinical Decision Support Only:** CareLoop is an informational Clinical Decision Support System (CDSS) designed to empower patient self-care and family vigilance. It is **not** an autonomous diagnostic medical device.
- **Synthetic Patient Data:** All patient names, case histories, and hospital summaries used in this demonstration are strictly synthetic and fictional.
- **Clinician-Configured Thresholds:** The default rules thresholds (e.g. weight gain >= 2kg in 3 days) are illustrative defaults derived from published heart failure self-care guidelines and must be customized by the treating clinician.
- **Translation Quality:** The bundled translations (Bahasa Malaysia, Chinese, Tamil) demonstrate localization capability; production deployment requires certified medical translator validation.

---

## 🗺️ Product Roadmap

- **Phase 1 (Hackathon MVP - Complete):** Single-file offline client, 68 drugs, 32 interactions, 4 languages, Time Machine, SBAR generator, and live test harness.
- **Phase 2 (Hospital EHR Integration):** SMART-on-FHIR connector to ingest real discharge summaries directly from Cerner and Epic EHRs.
- **Phase 3 (Cellular IoT Vitals):** Direct integration with cellular-connected weight scales and blood pressure cuffs for non-tech-savvy elderly patients.
- **Phase 4 (Community Clinic Pilot):** Prospective feasibility validation trial measuring 30-day readmission reduction in chronic heart failure cohorts.

---

## 📜 License
CareLoop is released under the **MIT License**.
