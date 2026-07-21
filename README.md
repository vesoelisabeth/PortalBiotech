# Peptide Retention Time – Exploratory Data Analysis



## Overview



This repository contains an exploratory analysis of a peptide liquid chromatography (LC) retention time dataset provided as part of the Portal Biotech data exploration task.



Rather than focusing on predictive modelling, the objective was to investigate the dataset and formulate biologically relevant questions.




## Repository Contents



- `portalbiotech.py` – Python script containing the exploratory data analysis.

- `README.md` – Summary of the analysis and findings.




## Methods



### 1. Data inspection and cleaning



The dataset was loaded into a pandas DataFrame and inspected for missing values, duplicate peptide IDs and modification annotations.



The following preprocessing steps were performed:



- Imported the dataset.

- Replaced missing modification annotations with empty strings.

- Checked for duplicate peptide IDs.

- Inspected peptide sequences and PTM annotations.



No duplicate peptide IDs were identified.



### 2. Post-translational modification (PTM) exploration



Questions looked at:

- Does acetylation have a larger impact than oxidation?

- Do PTMs affect the retention time?

- Is acetylation or oxidation associated with larger retention times?



Peptides were grouped into three categories:



- Unmodified

- Oxidation

- Acetylation



Retention time distributions were summarised using descriptive statistics and visualised using boxplots and violin plots.



Observed PTM distribution:



| PTM | Count |

|------|------:|

| Unmodified | 9175 |

| Oxidation | 674 |

| Acetylation | 151 |



Mean retention times:



| PTM | Mean Retention Time |

|------|--------------------:|

| Unmodified | 42.97 |

| Oxidation | 54.37 |

| Acetylation | 57.67 |



Modified peptides exhibited higher average retention times than unmodified peptides, with acetylated peptides showing the highest mean retention time in this dataset.



### 3. Analysis of modification annotations



The modification position was extracted from annotations (e.g. `4|Oxidation`) and mapped back to the corresponding amino acid within each peptide sequence.



The most frequently modified residues were:



| Residue | Count |

|---------|------:|

| M | 707 |

| A | 77 |

| S | 31 |



Methionine accounted for the majority of observed modifications, which is consistent with the prevalence of methionine oxidation in proteomics datasets. Several other modified residues occurred only a handful of times, making meaningful comparisons of their retention times difficult.



## Limitations



This analysis is exploratory and several limitations should be considered.



- Peptide sequence composition is a major determinant of retention time and acts as a confounding factor when comparing PTM groups.

- Different peptide sequences are compared throughout the dataset, meaning the direct effect of an individual PTM cannot be isolated.

- Several modified residue categories contain very small sample sizes, limiting meaningful statistical comparison.


## Future Work



Given additional time, several analyses could extend this exploratory work:



- Compare given retention times against predictions from established retention time prediction tools like **DeepLC**.

- Develop a supervised machine learning model using peptide sequence, peptide length and PTM annotations to predict peptide retention time, and compare its performance with published methods.



## Requirements



The analysis was performed using:



- Python 3

- NumPy

- pandas

- matplotlib



## Running the analysis



```bash

python portalbiotech.py

```
