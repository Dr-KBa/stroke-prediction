# Gradient Boosted Trees & Feature Engineering
The notebook called "Project_M3S2.ipynb" and associated files are part of the Turing College assignment of Module 3 Sprint 2.

# Data acquisition
The dataset should be downloaded from kaggle.com:
https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

# Helper functions
Helper functions for notebook are provided in a separate file "custom_functions.py"

# The notebook
The notebook includes data preparation, exploratory analysis, and prediction model training parts.

# Model deployment and web interface
Prediction model should be saved as prediction_model.joblib in the same folder as the notebook.
Flask (web framework) is used to run local server. Code to run the model is in the file 'app.py'.
HTML file for web interface is located in 'templates' folder. This folder should be in the same directory as the 'prediction_model.joblib' and 'app.py' files.
To run the model on MacOS (similar process should work in other OS, although untested):
1. In Terminal navigate to project directory, where 'prediction_model.joblib', 'app.py', and 'templates' folder is located;
2. Enter command: flask run;
3. Open webpage, where server is running, address will be displayed in Terminal;
4. Enter imaginary patient data to make prediction. Do not use on real patients!


# Contribution
The analysis and most of the coding was done by Kazimieras Badokas.

ChatGPT was prompted to generate initial HTML template for web interface and file 'app.py' to run the server for local deployment. Both codes were later adjusted manually. ChatGPT was also prompted to find errors in the code for analysis and suggest styling elements, or explain some observations (as disclosed).

Midjourney was prompted to generate cover image for the notebook.

# License for dataset
(Confidential Source) - can be used only for educational purposes.
Author credit is necessary https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset


