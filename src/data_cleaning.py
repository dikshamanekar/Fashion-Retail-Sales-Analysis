from pathlib import Path

import pandas as pd

def load_dataset(file_path):
"""Load a CSV dataset and return a DataFrame."""
path = Path(file_path)

```
if not path.exists():
    raise FileNotFoundError(
        f"Dataset not found: {path}"
    )

return pd.read_csv(path)
```

def clean_column_names(df):
"""Standardize column names."""
df = df.copy()

```
df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
)

return df
```

def remove_duplicate_rows(df):
"""Remove duplicate rows from a DataFrame."""
return df.drop_duplicates().copy()

if **name** == "**main**":
print("Fashion Retail data-cleaning module is ready.")
print("Import its functions into your analysis notebook.")
