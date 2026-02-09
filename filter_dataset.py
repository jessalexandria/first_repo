import pandas as pd
df=pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx")
filtered_df = df[["contig ID", "Seq Coverage"]]
filtered_df = filtered_df.sort_values(by="Seq Coverage", ascending=False)
filtered_df.to_csv("filtered_mantamonis.csv", index=False)
