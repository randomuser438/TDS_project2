# *Dataset Analysis using GPT-4o-mini*

This project is a Python-based tool to perform generic analysis on any dataset, including the Happiness dataset. It leverages an OpenAI GPT model (gpt-4o-mini) to analyze datasets dynamically and suggest advanced insights.


## *Project Overview*

The script takes a CSV file as input, performs a detailed analysis using Python libraries, and integrates with GPT-4o-mini to explore additional data-driven insights. It is designed to be flexible and adaptable, supporting various datasets, including but not limited to the Happiness dataset.

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
The happiness dataset contains information about books, including:
- *Columns*:
  - country: Name of the country.
  - year: The year of observation.
  - happiness_score: The overall happiness score for the country.
  - gdp_per_capita: GDP per capita for the country.
  - social_support: Measures of social support.
  - life_expectancy: Average life expectancy in the country.
  - freedom: Freedom score for citizens.
  - corruption: Perceived corruption index.
  - And others...

### Steps Performed:
1. *Summary Statistics*:
   - Identified countries with the highest and lowest happiness scores.
   - Analyzed trends in key indicators like GDP, social support, and freedom.
   - Reviewed the spread of happiness scores across years.

2. *Missing Value Analysis*:
   - Checked for missing data in columns (e.g., life_expectancy, corruption).
   - Suggested imputation techniques such as mean, median, or KNN imputation.

3. *Correlation Matrix*:
   - Examined correlations between happiness_score and indicators such as GDP and social support.
   - Visualized correlations using a heatmap.

4. *Outlier Detection*:
   - Flagged countries with unusually high or low values in indicators like GDP per capita or corruption.
     
5. *Cluster Analysis*:
   - Grouped countries into clusters based on happiness_score, GDP, and social support.
    
6. *LLM Insights*:
   - The LLM provided tailored suggestions, such as:
     - Performing regression analysis to predict happiness_score based on key indicators.
     - Investigating regional trends in happiness scores.
     - Creating composite indicators by combining metrics like social_support and life_expectancy.
     - Exploring time-series trends to evaluate changes in happiness over years.


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
- Correlations revealed that GDP and social support had the strongest relationships with happiness scores.
- Outliers included countries with low corruption but relatively low happiness scores.
- GPT-4o-mini suggested:
    -Time-series analysis to examine trends in happiness over the years.
    -Exploring disparities in happiness across regions and their potential causes.
    -Analyzing the impact of freedom and life expectancy on happiness in detail.


## *Limitations*

- The GPT model relies on the quality of the summary provided. Ensure accurate data preprocessing before querying the LLM.
- Outlier and cluster detection may require tuning parameters for datasets with different scales or distributions.


## *Conclusion*

This tool effectively combines Python-based statistical techniques with the interpretive power of GPT-4o-mini to derive actionable insights. The Happiness dataset analysis showcases the tool’s adaptability, making it useful for exploring any dataset and generating advanced analytical ideas.
