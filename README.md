<div align="center">

# CareLoop 🩺
### Post-Discharge Recovery & Patient Safety Guardian

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-0F5C5A?style=for-the-badge&logo=googlechrome&logoColor=white)](https://shaunjee.github.io/CareLoop/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2E7D32?style=for-the-badge)](LICENSE)
[![Tests: 100% Passing](https://img.shields.io/badge/Clinical%20Rules-30%2F30%20PASS-2E7D32?style=for-the-badge)](test_runner.js)
[![Evaluation F1](https://img.shields.io/badge/Discharge%20Parser-100%25%20F1-00838F?style=for-the-badge)](test_runner.js)
[![Architecture: Offline-First](https://img.shields.io/badge/Architecture-Offline--First%20Zero--Dep-1565C0?style=for-the-badge)](index.html)

<br/>

**DSH Hacks V2 Submission · Theme: AI x Healthcare**  
*Turning confusing hospital discharges into safe, multilingual recovery plans.*

[**🚀 Launch Interactive Demo**](https://shaunjee.github.io/CareLoop/) · [**📄 Executive Summary (PDF)**](submission_deliverables/CareLoop_OnePager.pdf) · [**💻 Source Code (PDF)**](submission_deliverables/CareLoop_Source_Code.pdf)

</div>

---

> **The One-Line Pitch:**  
> **CareLoop turns a confusing hospital discharge into a safe, understandable recovery plan in your own language, and watches the first 30 days so a family and a doctor know before things go wrong.**

---

## 🌟 Clinical Problem & Motivation

The days immediately following hospital discharge are among the most dangerous windows in modern medicine:

- **1 in 5 Medicare Patients** (19.6%) are readmitted within 30 days (*Jencks et al., NEJM*).
- **Over 50% of adult patients** experience at least one medication error or discrepancy post-discharge (*Kripalani et al., JAMA*).
- **The Health Literacy Gap:** Discharge summaries are written in compressed, clinical jargon (`LVEF 35%`, `TCA Meds`, `OD mane`). Vulnerable patients and family caregivers leave with little comprehension of what changed in their medications, which warning signs matter, or when to seek urgent help.
- **Silent Outpatient Deterioration:** Heart failure fluid congestion and post-surgical wound infections creep up quietly over 72 hours. Without remote outpatient surveillance, the patient only returns once they are in critical distress.

**CareLoop** bridges this dangerous gap with an offline-first, multilingual platform combining an **AI translation & parsing layer** with a **deterministic clinical rules engine**.

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
│  Transforms unstructured clinical notes into plain-language care plans.      │
│  Multilingual: English, Bahasa Malaysia, 中文, & தமிழ்.                        │
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

> [!IMPORTANT]
> **The AI Layer Understands & Explains · The Rules Engine Decides**  
> - **AI / NLP Layer:** Handles natural language parsing, medical abbreviation expansion, and multilingual translation.
> - **Deterministic Rules Engine:** **100% of clinical safety decisions**, drug-drug interactions, emergency alerts, and risk levels are computed in auditable deterministic code.
> - **Zero Hallucination Tolerance:** The AI layer can **NEVER** lower a risk score, suppress an emergency flag, or alter prescribed medication dosages.
> - **Universal Safety Net:** A persistent red *"I Feel Unwell"* button is accessible from every screen, instantly displaying 999/112 emergency calling and an unmissable paramedic handover card listing active diagnoses and current drugs.

---

## 🚀 Key Prototype Features

| Feature | Description | Clinical Rationale |
| :--- | :--- | :--- |
| **Discharge Decoder** | Ingests clinical text with a 68-drug dictionary. Multi-lingual toggle (**English, Bahasa Malaysia, 中文, தமிழ்**). | Eliminates language and health literacy barriers. |
| **Source-Span Highlighting** | Hovering over any care plan card highlights the exact source lines in the primary hospital text. | Builds trust with patients and clinicians via full provenance. |
| **Medication Guardian** | Timeline scheduler with adherence tracking + 32-row interaction matrix catching prescription & OTC clashes. | Prevents accidental double-dosing and fatal drug interactions (*e.g., Triple Whammy*). |
| **Time Machine** | Interactive day-by-day simulator fast-forwarding recovery from Day 0 baseline to Day 3 clinical deterioration. | Demonstrates how the system catches decompensation before readmission. |
| **Caregiver Circle** | Real-time family notification preview with simulated SMS bridge and offline QR pass. | Keeps family caregivers in the loop without app friction. |
| **Clinician SBAR Brief** | One-tap handover brief in standard medical format (*Situation, Background, Assessment, Recommendation*) with A4 print styling. | Saves doctor time during outpatient reviews. |
| **Live Trust Panel** | On-device test runner executing 20 synthetic summaries (15 tuning + 5 held-out) and 30 clinical rule cases. | Zero fabricated metrics: all accuracy numbers are live. |

---

## 🧪 Verified Test Results

| Test Dimension | Scope | Result | Status |
| :--- | :--- | :--- | :--- |
| **Discharge Parser (Tuning Set)** | 15 synthetic summaries | **100.0% Precision · 100.0% Recall · 100.0% F1** | **PASS ✓** |
| **Discharge Parser (Held-Out Set)** | 5 unseen summaries | **100.0% Precision · 100.0% Recall · 100.0% F1** | **PASS ✓** |
| **Dose Preservation Fidelity** | Extracted dosage strings | **100.0% Exact Match Rate** | **PASS ✓** |
| **Deterministic Rules Engine** | 30 clinical test cases | **30 / 30 Cases Passing (100%)** | **PASS ✓** |
| **XSS & Injection Protection** | String sanitization | **100% Escaped via `escapeHtml()`** | **PASS ✓** |

To execute the test suite yourself:
```bash
node test_runner.js
```
*(Or open the interactive app with `?test=1` appended to the URL to view the live evaluation suite in the browser console).*

---

## 💻 Running the App

CareLoop is built as a single, self-contained web application with **zero frameworks, zero build steps, and zero external runtime dependencies**. It works completely offline.

### Option 1: Live Demo (No Setup Needed)
Visit the deployed application directly:  
👉 **[https://shaunjee.github.io/CareLoop/](https://shaunjee.github.io/CareLoop/)**

### Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/ShaunJee/CareLoop.git
cd CareLoop

# Launch with any local server (Python example)
python -m http.server 8000

# Or using Node.js
npx serve .
```
Then open `http://localhost:8000` in your web browser. You can also simply double-click `index.html` to open it directly.

---

## 📁 Repository Structure

```text
CareLoop/
├── index.html                   # 🚀 Root interactive web application (runs GitHub Pages & local)
├── prototype/
│   └── index.html               # 📱 Prototype codebase (offline-first single-page app)
├── submission_deliverables/     # 🏆 Official Hackathon Deliverables
│   ├── CareLoop_OnePager.pdf    # One-page executive summary PDF for judges
│   └── CareLoop_Source_Code.pdf # Full syntax-highlighted code PDF with TOC & line numbers
├── tests/
│   └── test_runner.js           # 🧪 Automated test runner (F1 parser test, 30 rules cases, XSS check)
├── test_runner.js               # ⚡ Root test runner shortcut
├── LICENSE                      # 📜 MIT License
└── README.md                    # 📖 Project documentation & architecture guide
```

### Official Deliverable Links:
- **Interactive App:** [index.html](index.html)
- **One-Pager PDF:** [CareLoop_OnePager.pdf](submission_deliverables/CareLoop_OnePager.pdf)
- **Source Code PDF:** [CareLoop_Source_Code.pdf](submission_deliverables/CareLoop_Source_Code.pdf)
- **Test Suite:** [test_runner.js](test_runner.js)

---

## 🔒 Safety, Ethics & Limitations

- **Clinical Decision Support Only:** CareLoop is an informational Clinical Decision Support System (CDSS) designed to empower patient self-care and family vigilance. It is **not** an autonomous diagnostic medical device.
- **Synthetic Patient Data:** All patient names, case histories, and hospital summaries used in this demonstration are strictly synthetic and fictional.
- **Clinician-Configured Thresholds:** Default rules thresholds (e.g. weight gain ≥ 2kg in 3 days) are illustrative defaults derived from published heart failure self-care guidelines and must be customized by the treating physician.
- **Translation Quality:** The bundled translations (Bahasa Malaysia, Chinese, Tamil) demonstrate localization capability; production clinical deployment requires certified medical translator validation.

---

## 🗺️ Product Roadmap

- **Phase 1 (Hackathon MVP - Complete):** Zero-dependency offline client, 68 drugs, 32 interactions, 4 languages, Time Machine, SBAR generator, and live test harness.
- **Phase 2 (Hospital EHR Integration):** SMART-on-FHIR connector to ingest real discharge summaries directly from Cerner and Epic EHRs.
- **Phase 3 (Cellular IoT Vitals):** Direct integration with cellular-connected weight scales and blood pressure cuffs for non-tech-savvy elderly patients.
- **Phase 4 (Community Clinic Pilot):** Prospective feasibility validation trial measuring 30-day readmission reduction in chronic heart failure cohorts.

---

## 📜 License
CareLoop is released under the **[MIT License](LICENSE)**.
