import csv 
from pathlib import Path
from sklearn.datasets import load_diabetes

#Load dataset
dataset = load_diabetes()

# Nama feature
feature_names = dataset.feature_names

X = dataset.data
y = dataset.target

data_folder = Path("data")
data_file = data_folder / "diabetes_regression.csv"

with open(data_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    header = list(feature_names) + ["target"]
    writer.writerow(header)

    for feature, target in zip(X,y):
        row = list(feature) + [target]
        writer.writerow(row)

print("Dataset berhasil disimpan")
print(f"Lokasi file: {data_file}")
print(f"Jumlah data: {len(y)}")
print(f"Nama fitur: {', '.join(feature_names)}")
