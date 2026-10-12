# Import libraries
import pandas as pd
import os

# Defines data
RAW_PATH = "data/raw/flight_data.csv"
OUT_PATH = "data/imported/trimmed_data.csv"
LOG_PATH = "import_data.log"

# Column rename map: raw -> model required
RENAME_MAP = {
    "DAY_OF_MONTH": "DAY",
    "ORIGIN": "ORG_AIRPORT",
    "DEST": "DEST_AIRPORT",
    "CRS_DEP_TIME": "SCHEDULED_DEPARTURE",
    "DEP_TIME": "DEPARTURE_TIME",
    "DEP_DELAY": "DEPARTURE_DELAY",
    "CRS_ARR_TIME": "SCHEDULED_ARRIVAL",
    "ARR_TIME": "ARRIVAL_TIME",
    "ARR_DELAY": "ARRIVAL_DELAY",
}

KEEP_COLS_RAW = [
    "YEAR", "MONTH", "DAY_OF_MONTH",
    "DAY_OF_WEEK", "ORIGIN", "DEST",
    "CRS_DEP_TIME", "DEP_TIME", "DEP_DELAY",
    "CRS_ARR_TIME", "ARR_TIME", "ARR_DELAY"
]

def main():

    os.makedirs("data/imported", exist_ok=True)

    df = pd.read_csv(RAW_PATH)

    # Validate columns exist
    missing_cols = [c for c in KEEP_COLS_RAW if c not in df.columns]

    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    # Keep only required columns
    df = df[KEEP_COLS_RAW].copy()

    # Rename columns
    df = df.rename(columns=RENAME_MAP)

    # Drop completely empty rows
    df = df.dropna(how="all")

    # Save trimmed dataset
    df.to_csv(OUT_PATH, index=False)

    # Logging
    with open(LOG_PATH, "w") as f:
        f.write("IMPORT DATA LOG\n")
        f.write(f"Rows imported: {len(df)}\n")
        f.write(f"Columns: {list(df.columns)}\n")
        f.write(f"Missing values:\n{df.isnull().sum()}\n")

    print(f"Trimmed dataset saved to {OUT_PATH}")
    print(f"Log file saved to {LOG_PATH}")

if __name__ == "__main__":
    main()