<div align="center">

# CareLoop 🩺
### Post-Discharge Recovery & Patient Safety Guardian

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-0F5C5A?style=for-the-badge&logo=googlechrome&logoColor=white)](https://shaunjee.github.io/CareLoop/)
[![License: MIT](https://img.shields.io/badge/License-MIT-2E7D32?style=for-the-badge)](LICENSE)
[![Clinical Safety](https://img.shields.io/badge/Clinical%20Rules-30%2F30%20PASS-2E7D32?style=for-the-badge)](test_runner.js)
[![Discharge NLP](https://img.shields.io/badge/Parser%20Accuracy-100%25%20F1-00838F?style=for-the-badge)](test_runner.js)
[![Global Languages](https://img.shields.io/badge/Languages-6%20Global%20Langs-8E24AA?style=for-the-badge)](index.html)
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

```mermaid
flowchart LR
    Discharge["🏥 <b>HOSPITAL DISCHARGE</b><br/>━━━━━━━━━━━━━━━━━<br/>• Unstructured clinical notes<br/>• Polypharmacy regimen<br/>• High readmission risk<br/>• Fragile transition window"]

    subgraph CareLoops ["🛡️ &nbsp;&nbsp;&nbsp;&nbsp; CONTINUOUS OUTPATIENT CARE & SAFETY SURVEILLANCE (THE 4 CARE LOOPS) &nbsp;&nbsp;&nbsp;&nbsp; 🛡️"]
        direction LR
        L1["🔍 <b>LOOP 1 · DECODE</b><br/>━━━━━━━━━━━━━<br/>• Clinical NLP Parser<br/>• 6 Global Languages<br/>• Dual Reading Modes<br/>• Source Provenance"]
        ==>
        L2["🛡️ <b>LOOP 2 · PROTECT</b><br/>━━━━━━━━━━━━━<br/>• Medication Guardian<br/>• Pre-Ingestion Check<br/>• Triple Whammy Defense<br/>• 32-Rule Safety Matrix"]
        ==>
        L3["⏱️ <b>LOOP 3 · WATCH</b><br/>━━━━━━━━━━━━━<br/>• 60s Daily Check-in<br/>• 0–100 Recovery Risk<br/>• Biometric Tracking<br/>• Recovery Time Machine"]
        ==>
        L4["👨‍👩‍👧 <b>LOOP 4 · CONNECT</b><br/>━━━━━━━━━━━━━<br/>• Offline Caregiver Pass<br/>• Real-time Family Alerts<br/>• Clinician SBAR Brief<br/>• Paramedic Safety Card"]
    end

    Outcome["🎯 <b>SAFE 30-DAY RECOVERY</b><br/>━━━━━━━━━━━━━━━━━<br/>• Decompensation caught early<br/>• Zero clinical blind spots<br/>• Preventable readmission averted<br/>• Universal safety net active"]

    Discharge ==> CareLoops
    CareLoops ==> Outcome

    style Discharge fill:#0F5C5A,stroke:#093B3A,stroke-width:2px,color:#FFFFFF
    style Outcome fill:#0F5C5A,stroke:#093B3A,stroke-width:2px,color:#FFFFFF
    style CareLoops fill:#F7FAF9,stroke:#0F5C5A,stroke-width:2px,stroke-dasharray: 4 4,color:#0F5C5A
    style L1 fill:#E6F4F1,stroke:#0F5C5A,stroke-width:2px,color:#1D2A29
    style L2 fill:#EBF5EA,stroke:#2E7D32,stroke-width:2px,color:#1D2A29
    style L3 fill:#FFF4E5,stroke:#E65100,stroke-width:2px,color:#1D2A29
    style L4 fill:#EDE7F6,stroke:#512DA8,stroke-width:2px,color:#1D2A29
```

---

## 🛡️ Safety-First Hybrid Architecture

CareLoop adheres to a strict clinical engineering principle:

> [!IMPORTANT]
> **The AI Layer Understands & Explains · The Rules Engine Decides**  
> - **Symbolic Clinical NLP (Symbolic AI):** Handles natural language parsing, medical abbreviation expansion, and multilingual translation with 100% verbatim source-span traceability.
> - **Deterministic Clinical Rules Engine:** **100% of clinical safety decisions**, drug-drug interactions, emergency alerts, and risk levels are computed in auditable deterministic code (aligned with FDA SaMD Class II guidelines and clinical expert systems like Stanford MYCIN and Epic CDS).
> - **Pluggable BYOK Live LLM Layer:** Supports client-side Bring-Your-Own-Key connection to OpenAI (`gpt-4o-mini`), Google AI Studio (`gemini-1.5-flash`), Groq (`llama-3.3`), or local Ollama (`llama3`). A strict safety firewall isolates generative models to language tasks—an LLM can **NEVER** lower a risk score, suppress an emergency flag, or alter prescribed medication dosages.
> - **Universal Safety Net:** A persistent red *"I Feel Unwell"* button is accessible from every screen, instantly displaying 911 / 112 / 999 global emergency calling and an unmissable paramedic handover card listing active diagnoses and current drugs.

---

## 🚀 Key Prototype Features

| Feature | Description | Clinical Rationale |
| :--- | :--- | :--- |
| **Discharge Decoder** | Ingests clinical text with a 68-drug dictionary. Global 6-language engine (**English, Español, 中文, Français, Bahasa Melayu, தமிழ்**) + Dual Reading Modes (**Simple Everyday ⟷ Standard Clinical ICD-10**). | Eliminates language and health literacy barriers for patients while preserving ICD-10 GDMT depth for clinicians. |
| **Live Note Sandbox & Re-Parse** | `✏️ Edit / Paste Custom Note` and `⚡ Re-Parse Live` buttons allow clinicians and judges to type or paste arbitrary medical notes and watch the care plan, schedule, and safety alerts extract in real time. | Proves that the clinical NLP parser dynamically processes unstructured medical text on the fly rather than using static mockups. |
| **Quick Clinical Scenarios** | 1-tap preset buttons above the discharge summary loading diverse acute/chronic profiles: **Post-MI (DAPT)**, **Severe COPD**, **HFrEF & CKD**, **Ortho VTE**, and **Brittle Diabetes**. | Demonstrates broad cross-specialty clinical utility (cardiology, pulmonology, endocrinology, orthopedic surgery). |
| **Global Personas** | Diverse patient profiles headed by **Robert Miller** (Heart Failure & HTN · Boston, MA · English default), alongside Pak Ahmad, Mdm Tan, and Priya. | Demonstrates global applicability across diverse patient demographics and clinical profiles. |
| **Source-Span Highlighting** | Hovering over any care plan card highlights the exact source lines in the primary hospital text. | Builds trust with patients and clinicians via full byte-level provenance. |
| **Medication Guardian** | Timeline scheduler with adherence tracking + 32-row interaction matrix catching prescription & OTC clashes. | Prevents accidental double-dosing and fatal drug interactions (*e.g., Triple Whammy*). |
| **Time Machine** | Interactive day-by-day recovery tracker following timeline progression from Day 0 baseline through Day 3. | Demonstrates how the system catches decompensation before readmission. |
| **Pluggable BYOK Live LLM** | Optional client-side LLM panel in the Time Machine drawer for OpenAI, Google AI Studio, Groq, or local Ollama with live ping testing. | Accommodates hospital-hosted or cloud LLMs while keeping all safety-critical triage isolated in deterministic code. |
| **Caregiver Circle & Read-Only Pass** | Scannable cryptographically-signed offline QR pass (`/pass/<token>`) giving family members instantaneous read-only dashboard access to recovery risk index, morning vitals, and medication adherence without requiring login credentials. | Keeps family caregivers in the loop without app friction while safeguarding clinical record modification integrity. |
| **Clinician SBAR Brief** | One-tap handover brief in standard medical format (*Situation, Background, Assessment, Recommendation*) with A4 print styling. | Saves doctor time during outpatient reviews. |
| **Live Trust & Evaluation Panel** | On-device test runner executing 20 clinical discharge summaries (15 tuning + 5 held-out) and 30 clinical rule cases with an animated verification modal. | Zero fabricated metrics: all accuracy numbers are live. |

---

## 🧪 Verified Test Results

| Test Dimension | Scope | Result | Status |
| :--- | :--- | :--- | :--- |
| **Discharge Parser (Tuning Set)** | 15 clinical discharge summaries | **100.0% Precision · 100.0% Recall · 100.0% F1** | **PASS ✓** |
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
- **Patient Data & Privacy:** Patient records and hospital summaries provided are illustrative clinical profiles. CareLoop's offline architecture ensures zero protected health information leaves the local browser device.
- **Clinician-Configured Thresholds:** Default rules thresholds (e.g. weight gain ≥ 2kg in 3 days) are illustrative defaults derived from published heart failure self-care guidelines and must be customized by the treating physician.
- **Multilingual Translation Quality:** The bundled translations (English, Español, 中文, Français, Bahasa Melayu, தமிழ்) demonstrate global localization capability; institutional deployment requires certified medical translator validation.

---

## 🗺️ Product Roadmap

- **Phase 1 (Hackathon Complete):** Zero-dependency offline client, 68 drugs, 32 interactions, 6 global languages, dual reading modes (Simple Everyday vs Standard Clinical ICD-10), cryptographic offline caregiver pass (`/pass/<token>`), Recovery Time Machine, Clinician SBAR brief, universal paramedic safety card, and live trust suite.
- **Phase 2 (Hospital EHR Integration):** SMART-on-FHIR connector to ingest real discharge summaries directly from Cerner and Epic EHRs.
- **Phase 3 (Cellular IoT Vitals):** Direct integration with cellular-connected weight scales and blood pressure cuffs for non-tech-savvy elderly patients.
- **Phase 4 (Community Clinic Pilot):** Prospective feasibility validation trial measuring 30-day readmission reduction in chronic heart failure cohorts.

---

## 📜 License
CareLoop is released under the **[MIT License](LICENSE)**.
