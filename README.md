# Geographical Features in Survival Analysis

This repository contains the code and data for the paper titled "Using Geographic Location-Based Public Health Features in Survival Analysis" by Navid Seidi, Ardhendu Tripathy and Sajal Das.

## Abstract
Time elapsed till an event of interest is often modeled using the survival analysis methodology, which estimates a survival score based on the input features. There is a resurgence of interest in developing more accurate prediction models for time-to-event prediction in personalized healthcare using modern tools such as neural networks. Higher quality features and more frequent observations improve the predictions for a patient, however, the impact of including a patient's geographic location-based public health statistics on individual predictions has not been studied.
This paper proposes a complementary improvement to survival analysis models by incorporating public health statistics in the input features. We show that including geographic location-based public health information results in a statistically significant improvement in the concordance index evaluated on the Surveillance, Epidemiology, and End Results (SEER) dataset containing nationwide cancer incidence data. 
The improvement holds for both the standard Cox proportional hazards model and the state-of-the-art Deep Survival Machines model. 
Our results indicate the utility of geographic location-based public health features in survival analysis.

## Code and Data
The `code` directory contains the Python code used to generate the results in the paper. The `data` directory contains the datasets used in the analysis.

## Reproducing the Results
To reproduce the results in the paper, first clone the repository:

