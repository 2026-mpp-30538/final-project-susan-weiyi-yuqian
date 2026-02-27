import pandas as pd
from pathlib import Path

script_dir = Path(__file__).parent

# -------------------------
# Paths
# -------------------------
raw_dir = script_dir / "../data/raw-data"
out_dir = script_dir / "../data/derived-data"
out_dir.mkdir(parents=True, exist_ok=True)

raw_rent_burden = raw_dir / "rent_burden_B25070.csv"
raw_income = raw_dir / "median_household_income_B19013.csv"

out_rent_burden = out_dir / "rent_burden_clean.csv"
out_income = out_dir / "income_clean.csv"
out_econ = out_dir / "economic_pressure.csv"

# --------------------------------------------------
# 1️⃣ 去掉 ACS 第一行（Geography 行）
# --------------------------------------------------
def drop_geography_row(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop the first ACS label row where GEO_ID == 'Geography'.
    """
    if "GEO_ID" in df.columns:
        df = df[df["GEO_ID"] != "Geography"].copy()
    return df


# --------------------------------------------------
# 2️⃣ 清理 GEO_ID，生成标准 GEOID（tract）
# --------------------------------------------------
def clean_geoid(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a clean GEOID column by removing Census prefix
    (e.g., '1400000US17031010100' -> '17031010100')
    """
    df["GEOID"] = (
        df["GEO_ID"]
        .astype(str)
        .str.replace("1400000US", "", regex=False)
    )
    return df


# --------------------------------------------------
# 3️⃣ 将指定列转换为数值类型
# --------------------------------------------------
def convert_to_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Convert selected columns to numeric (coerce errors to NaN).
    """
    for col in cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df