import pandas as pd
import numpy as np
import openai
from sklearn.cluster import KMeans
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt
import os 

from openai import OpenAI
client = OpenAI(api_key=os.getenv("AIRPROXY_TOKEN"))
os.environ['AIRPROXY_TOKEN']

# Load the CSV file 
df_goodread = pd.read_csv('goodreads.csv')
pd.set_option('display.max_columns', None)

print("Overviewe of the data")
print(df_goodread.info())

print("\nSummary Statistics:")
print(df_goodread.describe(include="all"))

missing_values = df_goodread.isnull().sum()
print("\nMissing Values:")
print(missing_values)

df_goodread.dropna(inplace=True)
print("Missing values dropped.")
print(df_goodread.info())

missing_values = df_goodread.isnull().sum()
print("\nMissing Values after removal:")
print(missing_values)

correlation_matrix = df_goodread.select_dtypes(include=[np.number]).corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Correlation Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.axis("equal")
plt.show()

# Clusters
num_cols = df_goodread.select_dtypes(include=[np.number])
if not num_cols.empty:
    kmeans = KMeans(n_clusters=3, random_state=42)
    df_goodread["Cluster"] = kmeans.fit_predict(num_cols)
    print("\nCluster Labels Assigned.")

z_scores = np.abs((df_goodread.select_dtypes(include=[np.number]) - df_goodread.select_dtypes(include=[np.number]).mean()) / df_goodread.select_dtypes(include=[np.number]).std())
outliers = (z_scores > 3).any(axis=1)
print(f"\nOutlier Count: {outliers.sum()}")

data_summary = {
    "column_names": df_goodread.columns.tolist(),
    "column_types": df_goodread.dtypes.astype(str).tolist(),
    "missing_values": missing_values.to_dict(),
    "sample_data": df_goodread.head(3).to_dict(),
    "summary_statistics": df_goodread.describe(include="all").to_dict(),
}

#LLM - GPT-4o-mini

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a data analysis assistant"},
        {
            "role": "user",
            "content": f"""Analyze the following dataset summary: 
            {data_summary}
            Suggest specific analyses to gain more insights."""
        },
    ],
)
