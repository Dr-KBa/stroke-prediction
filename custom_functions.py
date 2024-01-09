import pandas as pd

def unique_values(df_name, *feature_names):
    """
    Function to list unique values of the selected features
    
    Input:
        Name of the dataset,  "feature1", "feature2", ...
        *args to accept multiple feature names
    
    Return:
        Returned is the text line with a list of unique values.
    """
    for feature_name in feature_names:
        unique = pd.unique(df_name[feature_name])
        print(f"Feature >{feature_name}< unique values: {unique}")