
import csv
import os

INPUT_DIR = "chunks"
OUTPUT_FILE = "Reviews.csv"
NUM_CHUNKS = 5

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)

    for i in range(1, NUM_CHUNKS + 1):
        input_file = os.path.join(
            INPUT_DIR, f"Reviews_part{i}.csv"
        )

        if not os.path.exists(input_file):
            raise FileNotFoundError(
                f"Missing chunk file: {input_file}"
            )

        with open(
            input_file, "r", newline="", encoding="utf-8-sig"
        ) as infile:
            reader = csv.reader(infile)
            header = next(reader, None)

            if i == 1:
                if header is None:
                    raise ValueError(f"{input_file} is empty")
                writer.writerow(header)

            elif header is None:
                raise ValueError(f"{input_file} is empty")

            for row in reader:
                writer.writerow(row)

print(f"Done! Combined all chunks into {OUTPUT_FILE}")
