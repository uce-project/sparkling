
import csv
import os
import math

INPUT_FILE = "Reviews.csv"
OUTPUT_DIR = "chunks"
NUM_CHUNKS = 5

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read the CSV and count its data rows
with open(INPUT_FILE, "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows = list(reader)

total_rows = len(rows)
chunk_size = math.ceil(total_rows / NUM_CHUNKS)

for i in range(NUM_CHUNKS):
    start = i * chunk_size
    end = min(start + chunk_size, total_rows)
    chunk_rows = rows[start:end]

    output_file = os.path.join(
        OUTPUT_DIR, f"Reviews_part{i + 1}.csv"
    )

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(chunk_rows)

    print(f"Created {output_file}: {len(chunk_rows)} rows")

print(f"\nDone! Split {total_rows} rows into 5 chunks.")
