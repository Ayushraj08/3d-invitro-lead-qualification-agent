import pandas as pd

# Known biotech hubs
BIOTECH_HUBS = [
    "Boston",
    "Cambridge MA",
    "Bay Area",
    "Basel",
    "UK Golden Triangle"
]

def infer_email(name: str, company: str) -> str:
    """
    Infer a professional email using a common pattern.
    Example: Dr Rahul Verma -> rahul.verma@company.com
    """
    try:
        clean_name = name.replace("Dr ", "").strip().lower()
        first, last = clean_name.split(" ", 1)
        domain = company.replace(" ", "").lower()
        return f"{first}.{last}@{domain}.com"
    except Exception:
        return ""

def enrich_leads(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enrich identified leads with business-relevant attributes.
    """
    df = df.copy()

    # Email inference
    df["email"] = df.apply(
        lambda row: infer_email(row["name"], row["company"]),
        axis=1
    )

    # Remote vs HQ logic
    df["is_remote"] = df.apply(
        lambda row: "Yes" if row["person_location"] != row["company_hq"] else "No",
        axis=1
    )

    # Biotech hub detection
    df["in_biotech_hub"] = df.apply(
        lambda row: "Yes"
        if row["person_location"] in BIOTECH_HUBS
        or row["company_hq"] in BIOTECH_HUBS
        else "No",
        axis=1
    )

    return df

def calculate_probability_score(row: pd.Series) -> int:
    """
    Calculate Propensity-to-Buy score (0–100)
    based on assignment-defined weighted signals.
    """
    score = 0
    title = row["title"].lower()

    # 1. Role Fit (+30)
    if any(k in title for k in ["director", "vp", "head"]) and \
       any(k in title for k in ["toxicology", "safety", "hepatic", "3d"]):
        score += 30

    # 2. Company Intent (+20)
    if row["funding_stage"] in ["Series A", "Series B"]:
        score += 20

    # 3. Technographic Fit (+15)
    if row["uses_invitro_or_nams"] == "Yes":
        score += 15

    # 4. Location Hub (+10)
    if row["in_biotech_hub"] == "Yes":
        score += 10

    # 5. Scientific Intent (+40)
    if row["published_recent_paper"] == "Yes" and \
       any(k in str(row["paper_topic"]).lower() for k in ["liver", "dili", "hepatic"]):
        score += 40

    return min(score, 100)

def process_leads(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full pipeline:
    Identification → Enrichment → Scoring → Ranking
    """
    df = enrich_leads(df)
    df["probability_score"] = df.apply(calculate_probability_score, axis=1)
    df = df.sort_values("probability_score", ascending=False).reset_index(drop=True)
    df["rank"] = df.index + 1
    return df
