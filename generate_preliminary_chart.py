import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Mantamonis_bacterial_contamination_analysis.xlsx"
df = pd.read_excel(file_path)

# Clean column names (remove spaces + colons)
df.columns = df.columns.str.strip().str.replace(":", "", regex=False)

counts = df["Preliminary Verdict"].value_counts()

plt.figure(figsize=(8, 6))
counts.plot(kind="bar", color="skyblue")

plt.title("Counts of Preliminary Verdict")
plt.xlabel("Preliminary Verdict")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("./preliminary_classification.png")

print("Bar chart saved as preliminary_classification.png")

