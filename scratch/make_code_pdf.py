import os
import sys
import subprocess
import html
import re

def main():
    print("CareLoop: Generating Submission Code PDF and One-Pager PDF...")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(script_dir) == "scratch":
        repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    else:
        repo_root = script_dir

    candidates_index = [
        os.path.join(repo_root, "index.html"),
        os.path.join(repo_root, "prototype", "index.html")
    ]
    index_path = next((p for p in candidates_index if os.path.exists(p)), None)
    if not index_path:
        print("Error: index.html not found.")
        sys.exit(1)

    candidates_onepager = [
        os.path.join(repo_root, "submission_deliverables", "onepager.html"),
        os.path.join(repo_root, "onepager.html")
    ]
    onepager_path = next((p for p in candidates_onepager if os.path.exists(p)), None)

    with open(index_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    lines = source_code.splitlines()
    total_lines = len(lines)
    print(f"Loaded index.html: {total_lines} lines.")

    # Find Table of Contents Markers
    toc_markers = [
        ("Design Tokens & CSS Styles", r"<style>"),
        ("App HTML Shell & Navigation", r"<!-- App Shell -->"),
        ("Synthetic Personas (Hero: Pak Ahmad)", r'<script id="data-personas"'),
        ("Comprehensive Drug Dictionary (68 Drugs)", r'<script id="data-drugs"'),
        ("Drug-Drug Interactions Engine (32 Pairs)", r'<script id="data-interactions"'),
        ("Deterministic Clinical Rules Table", r'<script id="data-rules"'),
        ("Multilingual Dictionary (EN, BM, ZH, TA)", r'<script id="data-i18n"'),
        ("Store & State Management", r"const STORAGE_KEY"),
        ("Discharge Parser & Clinical NLP", r"function parseDischarge"),
        ("Medication Guardian & Duplicates Checker", r"function checkInteractions"),
        ("Recovery Rules Engine & Score Evaluator", r"function evaluateRecoveryScore"),
        ("SVG 14-Day Visual Trend Chart", r"function renderSvgTrendChart"),
        ("View Renderers (Today, Plan, Check-in, Circle, Clinician, Trust)", r"function renderTodayView"),
        ("Live Ground-Truth Evaluation Runner (20 Cases)", r"function runEvaluationSuite"),
        ("30-Scenario Rules Safety Test Suite", r"function run30RulesVerification"),
        ("App Router & View Mounting", r"function renderApp")
    ]

    toc_entries = []
    for label, pattern in toc_markers:
        matched_line = None
        for i, line in enumerate(lines, 1):
            if re.search(pattern, line):
                matched_line = i
                break
        if matched_line:
            toc_entries.append((label, matched_line))

    # Build Cover Page & Monospace Source HTML
    toc_html = "".join([f"<li><span>{label}</span><span class='toc-dots'></span><span class='toc-num'>Line {line_num}</span></li>" for label, line_num in toc_entries])

    code_lines_html = []
    for i, line in enumerate(lines, 1):
        escaped = html.escape(line)
        code_lines_html.append(f"<div class='code-row'><span class='line-num'>{i}</span><span class='line-code'>{escaped if escaped else '&nbsp;'}</span></div>")
    code_content_html = "\n".join(code_lines_html)

    code_print_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CareLoop — Source Code PDF</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm;
      @bottom-right {{
        content: counter(page);
      }}
    }}
    body {{
      font-family: 'Courier New', Courier, monospace;
      font-size: 8pt;
      line-height: 1.35;
      background: #FFFFFF;
      color: #111827;
      margin: 0;
      padding: 0;
    }}
    .cover-page {{
      page-break-after: always;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      padding: 40px 20px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .cover-title {{
      font-size: 32pt;
      font-weight: 800;
      color: #0F5C5A;
      margin-bottom: 6px;
    }}
    .cover-subtitle {{
      font-size: 13pt;
      color: #4B5563;
      margin-bottom: 24px;
      line-height: 1.4;
    }}
    .meta-box {{
      background: #F4EFE6;
      border: 1px solid #E5DFD5;
      border-radius: 8px;
      padding: 16px 20px;
      margin-bottom: 24px;
      font-size: 9.5pt;
      line-height: 1.6;
    }}
    .toc-card {{
      background: #FFFFFF;
      border: 1px solid #D1D5DB;
      border-radius: 8px;
      padding: 16px 20px;
    }}
    .toc-title {{
      font-size: 12pt;
      font-weight: 700;
      color: #0F5C5A;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .toc-list {{
      list-style: none;
      padding: 0;
      margin: 0;
    }}
    .toc-list li {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 7px;
      font-size: 8.5pt;
    }}
    .toc-dots {{
      flex: 1;
      border-bottom: 1px dotted #9CA3AF;
      margin: 0 8px;
    }}
    .toc-num {{
      font-weight: 700;
      color: #0F5C5A;
    }}
    .code-container {{
      tab-size: 2;
      white-space: pre-wrap;
      word-break: break-all;
    }}
    .code-row {{
      display: flex;
    }}
    .line-num {{
      display: inline-block;
      width: 44px;
      text-align: right;
      padding-right: 12px;
      color: #9CA3AF;
      user-select: none;
      border-right: 1px solid #E5E7EB;
      margin-right: 10px;
      flex-shrink: 0;
    }}
    .line-code {{
      flex: 1;
      font-family: 'Consolas', 'Courier New', monospace;
    }}
  </style>
</head>
<body>
  <div class="cover-page">
    <div>
      <div class="cover-title">CareLoop</div>
      <div class="cover-subtitle">Post-Discharge Recovery & Patient Safety Guardian<br>DSH Hacks V2 Official Source Code Submission</div>
      
      <div class="meta-box">
        <strong>Event:</strong> DSH Hacks V2 ($100k+ Prize Pool)<br>
        <strong>Theme:</strong> AI x Healthcare<br>
        <strong>Team:</strong> Shaun Jee &amp; CareLoop Team<br>
        <strong>Live Demo:</strong> https://careloop.health<br>
        <strong>Source File:</strong> index.html ({total_lines} lines, single self-contained application)<br>
        <strong>Architecture:</strong> Zero-build vanilla HTML5/JS/CSS · Local-First Offline Demo Mode
      </div>

      <div class="toc-card">
        <div class="toc-title">Table of Code Regions &amp; Modules</div>
        <ul class="toc-list">
          {toc_html}
        </ul>
      </div>
    </div>

    <div style="font-size: 8pt; color: #6B7280; text-align: center; border-top: 1px solid #E5E7EB; padding-top: 10px;">
      CareLoop Prototype · MIT License · Synthetic Data Only · Not an autonomous diagnostic device.
    </div>
  </div>

  <div class="code-container">
    {code_content_html}
  </div>
</body>
</html>"""

    code_html_path = os.path.join(script_dir, "code_print.html")
    with open(code_html_path, "w", encoding="utf-8") as f:
        f.write(code_print_html)
    print(f"Created print-ready code HTML: {code_html_path}")

    # Find headless browser
    browser_candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]

    browser_bin = None
    for cand in browser_candidates:
        if os.path.exists(cand):
            browser_bin = cand
            break

    if not browser_bin:
        print("Warning: Neither Chrome nor Edge executable found for automated PDF printing.")
        print(f"You can open {code_html_path} and {onepager_path} in any browser and use 'Print to PDF'.")
        return

    print(f"Using browser for PDF rendering: {browser_bin}")

    deliverables_dir = os.path.join(repo_root, "submission_deliverables")
    os.makedirs(deliverables_dir, exist_ok=True)

    # Generate Code PDF
    code_pdf_path = os.path.join(deliverables_dir, "CareLoop_Source_Code.pdf")
    cmd_code = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={code_pdf_path}",
        code_html_path
    ]
    print("Generating CareLoop_Source_Code.pdf...")
    res = subprocess.run(cmd_code, capture_output=True, text=True)
    if os.path.exists(code_pdf_path):
        size_kb = os.path.getsize(code_pdf_path) / 1024
        print(f"SUCCESS: Generated CareLoop_Source_Code.pdf ({size_kb:.1f} KB)")
    else:
        print(f"Notice: Automated PDF export status: {res.stderr}")

    # Generate One-Pager PDF
    onepager_pdf_path = os.path.join(deliverables_dir, "CareLoop_OnePager.pdf")
    cmd_onepager = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={onepager_pdf_path}",
        onepager_path
    ]
    print("Generating CareLoop_OnePager.pdf...")
    res2 = subprocess.run(cmd_onepager, capture_output=True, text=True)
    if os.path.exists(onepager_pdf_path):
        size2_kb = os.path.getsize(onepager_pdf_path) / 1024
        print(f"SUCCESS: Generated CareLoop_OnePager.pdf ({size2_kb:.1f} KB)")

if __name__ == "__main__":
    main()
