# *Dataset Analysis using GPT-4o-mini*

This project is a Python-based tool designed to perform comprehensive analyses on various datasets, including the Media dataset. By integrating traditional data analysis techniques with the capabilities of OpenAI's GPT-4o-mini, the tool provides dynamic insights and suggests advanced analytical approaches.


## *Project Overview*

The script takes a CSV file as input , conducts a thorough analysis using Python libraries, and utilizes GPT-4o-mini to propose further explorations. This methodology ensures flexibility, making it applicable to diverse datasets, such as the Media dataset.


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


## *Use Case: Media Dataset*

### Sample Dataset Overview
The media dataset contains information about books, including:
- *Columns*:
  - title: The title of the media (e.g., movies, TV shows, articles).
  - category: The genre or type of media (e.g., comedy, drama, news).
  - release_year: The year the media was released.
  - rating: User rating or critic score for the media.
  - views: Total number of views or impressions.
  - platform: The platform where the media is hosted or distributed.
  - And others...

### Steps Performed:
1. *Summary Statistics*:
   - Identified most popular categories based on views.
   - Analyzed trends in ratings across release years.
   - Determined platforms with the highest-rated or most-viewed media.

2. *Missing Value Analysis*:
   - Checked for missing values in columns such as category, views, or rating.
   - Suggested imputation techniques such as mean, median, or mode imputation.

3. *Correlation Matrix*:
   - Examined correlations between numerical features like views, ratings, and release_year.
   - Visualized correlations using a heatmap.

4. *Outlier Detection*:
   - Highlighted media entries with unusually high views or ratings.
   - Flagged categories or platforms with consistent outliers.
     
5. *Cluster Analysis*:
   - Grouped media entities into clusters based on ratings and views.
   - Analyzed characteristics of high-performing clusters (e.g., genre or platform distribution).
    
6. *LLM Insights*:
   - The LLM provided tailored suggestions, such as:
     - Regression analysis to predict views or ratings based on other features.
     - Exploring trends in media consumption across platforms or genres.
     - Feature engineering, such as combining release_year and category for trend analysis.
     - Time-series analysis for ratings or views trends over time.

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

For the Media dataset:
- Correlations revealed strong relationships between views and ratings.
- Outlier detection highlighted highly-rated media with relatively low views.
- GPT-4o-mini suggested:
    -Analyzing category-specific trends in views and ratings.
    -Exploring the impact of release year on ratings across platforms.
    -Investigating audience preferences by genre using visualizations like bar and pie charts.


## *Limitations*

- The GPT model relies on the quality of the summary provided. Ensure accurate data preprocessing before querying the LLM.
- Outlier and cluster detection may require tuning parameters for datasets with different scales or distributions.


## *Conclusion*

This tool combines Python-based statistical techniques with GPT-4o-mini's interpretive capabilities to derive actionable insights. The analysis of the Media dataset demonstrates its adaptability, making it suitable for exploring various datasets and generating advanced analytical ideas.


