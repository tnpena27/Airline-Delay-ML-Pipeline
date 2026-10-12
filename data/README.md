# Data

The raw flight dataset and generated CSV files are intentionally not included in this public repository.

The pipeline expects the source file at:

`data/raw/flight_data.csv`

The import step selects and renames the fields needed by the model and writes:

`data/imported/trimmed_data.csv`

The cleaning step filters the data to JFK departures, removes incomplete/invalid records, and writes `cleaned_data.csv` at the repository root for model training.

The included `trimmed_data.csv.dvc` file demonstrates the DVC tracking metadata used for the intermediate dataset. A local DVC cache or configured remote containing the original data is required to reproduce that tracked file directly with DVC.
