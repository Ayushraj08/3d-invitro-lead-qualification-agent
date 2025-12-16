# 🧬 3D In-Vitro Lead Qualification Agent

A production-ready **lead identification, enrichment, and prioritization system** designed to help business development teams focus on **life-science decision-makers** most likely to adopt **3D in-vitro models** for drug discovery and safety assessment.

The system converts fragmented professional, scientific, and company-level signals into a **clear, interpretable Propensity-to-Buy score (0–100)** surfaced through an interactive dashboard and exportable dataset.

---

## 🎯 Problem Statement

Business development teams in biotech and pharma face three recurring challenges:

1. **Too many leads, too little signal**  
   Titles alone don’t indicate buying intent.

2. **Poor prioritization**  
   Junior researchers and senior decision-makers are treated equally.

3. **Lack of scientific context**  
   Traditional lead tools ignore publication history and research focus.

This project addresses these gaps by **systematically ranking leads using signals that correlate with real adoption intent** for 3D in-vitro platforms.

---

## 🧠 Solution Overview

The agent implements a **clear, staged pipeline**:

Identification → Enrichment → Probability Scoring → Ranked Output


Rather than opaque machine-learning predictions, the system uses a **transparent, weighted scoring model** aligned with how experienced BD professionals reason about prospects.

---

## 🏛️ High-Level Architecture

```text
┌──────────────────────────────┐
│        Raw Lead Dataset      │
│        (leads_raw.csv)       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Enrichment Layer       │
│  • Business email inference  │
│  • Remote vs HQ resolution   │
│  • Biotech hub detection     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Probability Engine       │
│  • Weighted scoring logic    │
│  • Normalized score (0–100)  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Streamlit Dashboard      │
│  • Search & filtering        │
│  • CSV export & persistence  │
└──────────────────────────────┘
```

The full pipeline is orchestrated by `process_leads()` in `scoring.py`, ensuring each run is deterministic, explainable, and reproducible.

---

## 🔍 Stage 1 — Identification

Each row in `leads_raw.csv` represents a **scientifically and commercially relevant profile**, sourced from:

- Professional networks (role and seniority)
- Scientific publications (e.g., PubMed authorship)
- Conference participation (e.g., Society of Toxicology)

### Target roles include:
- Director of Toxicology  
- Head of Safety Assessment  
- VP / Head of Preclinical  
- Hepatic / Liver Safety Leads  

These roles were selected because they:
- Influence experimental strategy
- Control or influence budgets
- Are direct users or sponsors of in-vitro platforms

---

## 🔗 Stage 2 — Enrichment

Each identified lead is enriched with business-critical context:

### Enrichment Signals
- **Business email inference** (deterministic, domain-based)
- **Person location vs company HQ** (remote vs on-site)
- **Biotech hub detection**  
  (Boston/Cambridge, Bay Area, Basel, UK Golden Triangle)

### Why this matters
- Remote vs HQ informs **meeting strategy**
- Hub presence correlates with **technology adoption velocity**
- Email availability enables **immediate outreach readiness**

All enrichment logic is deterministic and implemented in `scoring.py`.

---

## 📊 Stage 3 — Probability Scoring Engine

Each lead receives a **Propensity-to-Buy score (0–100)** based on weighted signals.

### Scoring Signals & Weights

| Signal Category | Example Criteria | Weight |
|-----------------|-----------------|--------|
| Role Fit | Director / Head + Toxicology / Safety / Hepatic | +30 |
| Company Intent | Series A / B funded biotech | +20 |
| Technographic Fit | Uses in-vitro models / NAMs | +15 |
| Location Signal | Major biotech hub | +10 |
| Scientific Intent | Recent liver / DILI publication (≤ 2 yrs) | +40 |

### Example Outcome

- Junior scientist at unfunded startup → **~15 / 100**
- Director of Safety Assessment at Series B biotech with recent liver toxicity publication → **90–100 / 100**

This mirrors how experienced BD teams **triage leads in practice**, but at scale.

---

## 🖥️ Output — Lead Qualification Dashboard

The Streamlit dashboard provides:

- Ranked lead list (highest intent first)
- Full-text search (name, title, company, location)
- Probability score filtering
- Explicit **remote vs HQ** visibility
- One-click CSV export

### Persisted Output

Each run generates:



data/leads_scored.csv


This file enables:
- Offline analysis
- CRM imports
- Sharing with sales and GTM teams

---

## 🧰 Tech Stack

- **Python 3**
- **Pandas** — data processing
- **Streamlit** — interactive dashboard
- **CSV persistence** — lightweight, transparent
- **Rule-based scoring** — explainable by design

No scraping, no private APIs, no credential requirements.

---

## ▶️ Local Setup

```bash
git clone <repo-url>
cd 3d-invitro-lead-scoring-agent
```
```
pip install -r requirements.txt
streamlit run app.py
```

**The app will be available at:**
```
http://localhost:8501
```

## 🧪 Data Disclaimer

All data in this repository is **synthetic and representative**, created solely for demonstration purposes.

The system architecture, enrichment logic, and scoring framework are designed to be **production-ready**, while strictly respecting **data ethics** and **platform terms of service**.

---

## 🚀 Why This Project Stands Out

✔ Fully working system (not a mockup)  
✔ Clear separation of concerns  
✔ Business-aligned scoring logic  
✔ Transparent, explainable decisions  
✔ Immediately usable by BD teams  

This project demonstrates the ability to:

- Translate ambiguous business problems into scalable systems  
- Design for real-world business development workflows  
- Balance technical execution with commercial reasoning  

---

## 📌 Possible Extensions

- Live enrichment via compliant third-party APIs  
- Dynamic weight tuning by therapeutic area  
- CRM integrations (HubSpot / Salesforce)  
- Temporal scoring decay and trend analysis  

---

## 👤 Author

**Ayush Raj**  
*Focus:* Data-driven systems, product thinking, and applied AI for business outcomes
