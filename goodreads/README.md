# *Dataset Analysis using GPT-4o-mini*

This project is a Python-based tool to perform generic analysis on any dataset, including the Goodreads dataset (sample shown in the uploaded image). It uses an OpenAI GPT model (gpt-4o-mini) to analyze datasets dynamically and provide suggestions for further insights.


## *Project Overview*

The script takes a CSV file as input, analyzes it programmatically, and generates an interactive analysis using machine learning and statistical techniques. Additionally, it queries GPT-4o-mini to suggest advanced analysis ideas. 

This approach is designed to be flexible and adaptable to any dataset, not just the Goodreads dataset.


## *Key Features*

1. *Data Loading*:
   - Reads and processes any generic CSV file using pandas.
   - Handles missing values and identifies data types.

2. *Initial Analysis*:
   - Prints the dataset's schema, including column names and data types.
   - Displays summary statistics for numerical and categorical fields.
   - Counts missing values per column.

3. *Correlation Matrix*:
   - Calculates and visualizes correlations between numerical columns using a heatmap.
   - Helps identify relationships between variables.

4. *Outlier Detection*:
   - Detects potential outliers in numerical columns using the Z-score method.
   - Counts the number of rows containing extreme values.

5. *Cluster Analysis*:
   - Uses KMeans clustering to group rows based on numerical features.
   - Assigns a "Cluster" label to each row.

6. *Dynamic LLM Query*:
   - Creates a summary of the dataset, including column names, types, missing values, and example rows.
   - Sends this summary to GPT-4o-mini, requesting suggestions for further analyses.
   - Outputs GPT-4o-mini's recommendations for additional insights.

7. *Visualization*:
   - Includes a heatmap for correlation analysis.
   - Prepares the dataset for additional visualizations based on GPT suggestions.


## *Use Case: Goodreads Dataset*

### Sample Dataset Overview
The Goodreads dataset contains information about books, including:
- *Columns*:
  - book_id: Unique identifier for each book.
  - authors: Authors of the book.
  - title: Title of the book.
  - language_code: Language in which the book is written.
  - average_rating: The book's average rating on Goodreads.
  - original_publication_year: The year the book was first published.
  - And others...

### Steps Performed:
1. *Summary Statistics*:
   - Counted the number of books per language.
   - Identified the highest and lowest-rated books.
   - Determined the earliest and most recent publication years.

2. *Missing Value Analysis*:
   - Checked for missing data in columns like isbn, authors, and language_code.

3. *Correlation Matrix*:
   - Examined correlations between numerical columns (e.g., average_rating, books_count).
   - Visualized correlations using a heatmap.

4. *Outlier Detection*:
   - Identified books with exceptionally high or low ratings or unusually high numbers of editions.

5. *Cluster Analysis*:
   - Grouped books into clusters based on numerical features (books_count, average_rating).

6. *LLM Insights*:
   - The LLM provided tailored suggestions, such as:
     - Predicting the success of a book based on average_rating and books_count.
     - Identifying genres that tend to perform well in terms of ratings.
     - Suggestions for feature engineering (e.g., combining authors and publication_year).


## *How GPT-4o-mini Helps*

The GPT model enhances the analysis by:
- Generating advanced insights that may not be obvious in traditional statistical analysis.
- Proposing specific analyses such as regression, time-series analysis, or network-based evaluations.
- Adapting recommendations to the dataset provided, making it flexible for any CSV file.


## *How to Use*

1. *Setup*:
   - Install dependencies:
     bash
     pip install pandas numpy openai scikit-learn seaborn matplotlib
     
   - Replace YOUR_API_KEY_HERE in the script with your OpenAI API key.

2. *Run the Script*:
   - Replace csv_file_path with the path to your dataset.
   - Execute the script:
     bash
     python analyze_csv.py
     

3. *Outputs*:
   - Visualizations such as a correlation heatmap.
   - Console logs for summary statistics, missing value analysis, and clusters.
   - GPT-4o-mini suggestions for further analysis.

4. *Interpreting GPT Output*:
   - Use the GPT suggestions to perform additional custom analyses (e.g., regression, clustering).


## *Results*

For the Goodreads dataset:
- Identified correlations between average_rating and books_count.
- Detected outliers in highly-rated books with few editions.
- GPT suggested analyzing trends in publication years, which could help predict the popularity of books in specific genres or languages.


## *Limitations*
- The GPT model relies on the quality of the summary provided. Ensure accurate data preprocessing before querying the LLM.
- Outlier and cluster detection may require tuning parameters for datasets with different scales or distributions.


## *Conclusion*

This tool combines the power of traditional Python-based analysis with GPT-4o-mini’s language understanding to provide actionable insights. It is flexible, making it suitable for any dataset, including but not limited to the Goodreads dataset.
yses or results you generate!
