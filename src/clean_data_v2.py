# Import Libraries
import pandas as pd

# Defines Data
INPUT_PATH = "data/imported/trimmed_data.csv"
OUTPUT_PATH = "cleaned_data.csv"
LOG_PATH = "clean_data.log"

# Identifies Airport
AIRPORT = "JFK"

# Required Columns
REQUIRED_COLUMNS = [
    "YEAR", "MONTH", "DAY", "DAY_OF_WEEK",
    "ORG_AIRPORT", "DEST_AIRPORT",
    "SCHEDULED_DEPARTURE", "DEPARTURE_TIME", "DEPARTURE_DELAY",
    "SCHEDULED_ARRIVAL", "ARRIVAL_TIME", "ARRIVAL_DELAY"
]

def main():
    df = pd.read_csv(INPUT_PATH)

    # Validate required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    start_rows = len(df)

    # Filter to JFK departures
    df = df[df["ORG_AIRPORT"] == AIRPORT].copy()

    # Remove missing required values
    df = df.dropna(subset=REQUIRED_COLUMNS)

    # Make numeric columns numeric
    numeric_cols = [
        "YEAR", "MONTH", "DAY", "DAY_OF_WEEK",
        "SCHEDULED_DEPARTURE", "DEPARTURE_TIME", "DEPARTURE_DELAY",
        "SCHEDULED_ARRIVAL", "ARRIVAL_TIME", "ARRIVAL_DELAY"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=numeric_cols)

    # Remove invalid time values
    time_cols = [
        "SCHEDULED_DEPARTURE", "DEPARTURE_TIME",
        "SCHEDULED_ARRIVAL", "ARRIVAL_TIME"
    ]

    for col in time_cols:
        df = df[(df[col] >= 0) & (df[col] <= 2400)]

    # Save cleaned data
    df.to_csv(OUTPUT_PATH, index=False)

    with open(LOG_PATH, "w") as f:
        f.write("CLEAN DATA LOG\n")
        f.write(f"Airport filter: {AIRPORT}\n")
        f.write(f"Starting rows: {start_rows}\n")
        f.write(f"Rows after cleaning: {len(df)}\n")
        f.write(f"Columns: {list(df.columns)}\n")

    print(f"Cleaned dataset saved to {OUTPUT_PATH}")
    print(f"Rows after cleaning: {len(df)}")
    print(f"Log file saved to {LOG_PATH}")

if __name__ == "__main__":
    main()