# Water Quality Prediction using Random Forest Classifier

This project, developed as a partial fulfillment for the Bachelor of Technology in Computer Science & Engineering at SRM Institute of Science & Technology, focuses on creating a machine learning model to predict and classify water quality. The model uses a Random Forest Classifier trained on data from the Tamil Nadu Pollution Control Board (TNPCB) to categorize water samples into four distinct classes, offering a rapid and efficient tool for environmental monitoring.

<!--
## 📋 Table of Contents
- [Abstract](#abstract)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Methodology](#methodology)
- [Results](#results)
- [User Interface](#user-interface)
- [Future Scope](#future-scope)
- [Project Team](#project-team)
-->
## Abstract

This project develops a machine learning model to classify water quality levels using key environmental indicators. The dataset, sourced from the Tamil Nadu Pollution Control Board (TNPCB), includes crucial features for water quality assessment, such as dissolved oxygen (D.O.), pH, conductivity, biochemical oxygen demand (BOD), and coliform counts. A Random Forest classifier was trained to categorize water samples into four classes (A, B, C, DE), representing different contamination levels. The model achieved a high classification accuracy of **93%**, validated through a confusion matrix and classification report. This project demonstrates the practical application of machine learning for environmental monitoring, offering a rapid and effective tool for assessing water quality and aiding in water resource management.

## ✨ Key Features

- **High Accuracy Model**: Achieved a **93.2%** prediction accuracy using a Random Forest Classifier.
- **Multi-Class Classification**: Classifies water into four standard quality levels: Class A, B, C, and DE.
- **Data-Driven**: Utilizes real-world data from the TNPCB's National Water Monitoring Programme (NWMP) reports from 2019 and 2023.
- **Intelligent Feature Reduction**: Employed Exploratory Data Analysis (EDA), correlation matrices, and box plots to reduce the initial 28 features to 11 most impactful ones, improving model performance.
- **User-Friendly Interface**: A simple GUI built with Tkinter allows for easy input of water parameters to get instant predictions.

## 🏗️ System Architecture

The proposed architecture leverages machine learning to automate the classification process, overcoming the limitations of traditional, lab-based methods which are often time-consuming and costly.

1.  **Data Collection**: Data is sourced from TNPCB reports. This can be extended with IoT sensors for real-time data acquisition.
2.  **Data Preprocessing**: The raw data (from PDFs) is converted, cleaned, and normalized. Missing values are handled, and datasets from different years are unified.
3.  **Model Training**: A Random Forest classifier is trained on the preprocessed data with a reduced feature set to learn the patterns corresponding to different water quality classes.
4.  **Prediction Engine**: The trained model takes 11 key water quality parameters as input from the user.
5.  **Output & Reporting**: The model instantly predicts the water quality class (A, B, C, or DE) and displays it to the user via the GUI, along with its designated use.

![Methodology Flowchart](https://i.imgur.com/k2mQ7jT.png)

## 🛠️ Methodology

The project followed a systematic approach from data acquisition to model deployment.

### 1. Data Acquisition & Conversion
- Publicly available datasets were found to be highly imbalanced.
- We selected data from the **Tamil Nadu Pollution Control Board (TNPCB)** reports for 2019 and 2023, which included target classifications.
- The Python library `pdfplumber` was used to extract tabular data from the PDF reports and convert it into a machine-readable CSV format.

### 2. Data Preprocessing
- Missing values were filled using the mean of their respective columns.
- Unwanted rows (headers/footers) were removed.
- Non-numeric entries like "Nil" and "-" were replaced with `NaN`.
- The datasets from 2019 (5 classes) and 2023 (4 classes) were unified by merging classes D and E into a single 'DE' class, resulting in a combined dataset of 1,404 rows.

### 3. Feature Reduction
- Exploratory Data Analysis (EDA) was performed using correlation matrices and box plots to understand feature relationships.

  <img width="915" height="476" alt="Screenshot 2025-09-25 at 12 48 35 PM" src="https://github.com/user-attachments/assets/39ac4462-94f6-43bc-b2f1-e6a21b5fcffc" />

  
- High correlation was observed between features like (Fecal Coliform, Total Coliform), (Total Dissolved Solids, Total Fixed Solids), and (Conductivity, various ions).
- By analyzing the feature distributions across the target classes, we carefully selected features that showed clear separation between classes, especially between the overlapping Class B and C.
- The initial 28 features were reduced to the following 11 to optimize the model:
  - Dissolved Oxygen (D.O.)
  - pH
  - Conductivity
  - Biochemical Oxygen Demand (BOD)
  - Fecal Coliform
  - Turbidity
  - Total Alkalinity
  - Total Kjeldahl Nitrogen
  - Ammonia-N
  - Magnesium
  - Fluoride

### 4. Model Training
- The cleaned dataset with the 11 selected features was split into training and testing sets.
- A **Random Forest Classifier** was trained. This ensemble model was chosen for its robustness against overfitting and its ability to handle complex, non-linear relationships.

## Results

The trained model demonstrated excellent performance with an overall accuracy of **93.2%**.

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
| :---: | :-------: | :----: | :------: | :-----: |
|   0   |   0.90    |  0.90  |   0.90   |   137   |
|   1   |   0.93    |  0.95  |   0.94   |   270   |
|   2   |   0.88    |  0.64  |   0.74   |   22    |
|   3   |   0.98    |  0.98  |   0.98   |   133   |
| **Avg** | **0.93** | **0.93** | **0.93** | **562** |


### Confusion Matrix

The confusion matrix shows high accuracy for all classes, particularly B (256/270) and DE (131/133). Class C proved to be the most challenging to classify, likely due to its parameter values overlapping with other classes.

![Confusion Matrix](https://i.imgur.com/83pIq5M.png)

## 🖥️ User Interface

A simple and intuitive user interface was developed using **Tkinter**. It allows users to input values for the 11 key parameters and receive an instant prediction about the water quality class and its usability.

<img width="779" height="400" alt="Screenshot 2025-09-25 at 12 59 37 PM" src="https://github.com/user-attachments/assets/6b58bebc-a83f-4519-a866-02161e006d5f" />


## Future Scope

While this project provides a solid foundation, there are several avenues for enhancement:

- **IoT Integration**: Automate data collection using IoT sensors for real-time monitoring and alerts.
- **Mobile Application**: Develop a mobile-friendly version for remote and on-the-go water quality assessment.
- **Database Integration**: Connect the application to regional and national environmental databases to benchmark results against established standards.
- **Model Refinement**: Further fine-tune hyperparameters or explore other algorithms to improve the classification accuracy for challenging classes like 'C'.
