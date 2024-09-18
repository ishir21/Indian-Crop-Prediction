# Crop Yield Prediction

## Overview

This project aims to predict crop yield based on various agricultural inputs such as crop type, season, state, area, production, rainfall, fertilizer usage, and pesticide usage. The model is trained using historical data from Indian states spanning from 1997 to 2020. The predictions are made using a machine learning model deployed via a Flask web application.

## Dataset

The dataset used for this project includes agricultural data from multiple crops cultivated across various Indian states from 1997 to 2020. It contains the following features:

- **Crop:** The name of the crop cultivated.
- **Crop_Year:** The year in which the crop was grown.
- **Season:** The specific cropping season (e.g., Kharif, Rabi, Whole Year).
- **State:** The Indian state where the crop was cultivated.
- **Area:** The total land area (in hectares) under cultivation for the specific crop.
- **Production:** The quantity of crop production (in metric tons).
- **Annual_Rainfall:** The annual rainfall received in the crop-growing region (in mm).
- **Fertilizer:** The total amount of fertilizer used for the crop (in kilograms).
- **Pesticide:** The total amount of pesticide used for the crop (in kilograms).
- **Yield:** The calculated crop yield (production per unit area).

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- Pandas
- Scikit-learn
- Jinja2

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ishir21/crop-yield-prediction.git
   cd crop-yield-prediction
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Prepare the dataset:

   Place the `crop_yield_final.csv` file in the `notebook/data/` directory.

4. Run the data ingestion, transformation, and model training pipelines:

   ```bash
   python src/components/data_ingestion.py
   ```

### Running the Flask App

1. Start the Flask web application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### Using the Web Application

- **Input Fields:** The user can select the crop, season, state, and enter the area, production, rainfall, fertilizer, and pesticide usage.
- **Prediction:** After submitting the form, the predicted crop yield will be displayed on the same page.

## Model and Methodology

1. **Data Ingestion:** The data is loaded from a CSV file and split into training and testing datasets.
2. **Data Transformation:** Features are preprocessed, including handling missing values, encoding categorical variables, and scaling numerical features.
3. **Model Training:** A regression model is trained using the processed data.
4. **Prediction Pipeline:** The model is used to predict crop yield based on user inputs provided through the web application.
