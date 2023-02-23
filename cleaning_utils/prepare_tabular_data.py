import pandas as pd
from ast import literal_eval
from pathlib import Path


class AirbnbDataPrep:
    def __init__(self):
        self.df = pd.read_csv('/Users/akmalpopalzi/Documents/GitHub/modelling-airbnbs-property-listing-dataset-/airbnb-property-listings/tabular_data/listing.csv')

    def initial_cleaning(self):
        self.df.Category = self.df.Category.astype('category')
        self.df.drop(index = 586, inplace = True)
        self.df.drop('Unnamed: 19', axis = 1, inplace = True)
        self.df.reset_index(drop = True, inplace = True)
        
        
        
    def remove_rows_with_missing_ratings(self):
        self.df.dropna(subset = ['Description','Cleanliness_rating','Accuracy_rating',"Communication_rating","Location_rating","Check-in_rating","Value_rating"], inplace = True)
        self.df.reset_index(drop = True, inplace = True)

    
    def clean_description_strings(self):
        # convert string into list of strings
        for i in range(len(self.df.Description)):
            self.df.Description[i] = literal_eval(self.df.Description[i])

        # remove extra words and phrases
        phrases = ['About this space',
           'The space',
           '',
           "  ",
           " ", 
           'Other things to note',
           'Guest access']
        
        for index, value in enumerate(self.df.Description):
             for desc_index, desc in enumerate(value):
                  if desc in phrases:
                       self.df.Description[index].pop(desc_index)


    def set_feature_values(self):
        self.df[['guests','beds','bathrooms','bedrooms']] = self.df[['guests','beds','bathrooms','bedrooms']].fillna(1)


    def clean_tabular_data(self):
        self.initial_cleaning()
        self.remove_rows_with_missing_ratings()
        self.clean_description_strings()
        self.set_feature_values()
        new_df = self.df.copy()
        return new_df



if __name__ == "__main__":
    dataset = AirbnbDataPrep()
    clean_tab_data = dataset.clean_tabular_data()
    filepath = Path('/Users/akmalpopalzi/Documents/GitHub/modelling-airbnbs-property-listing-dataset-/airbnb-property-listings/tabular_data/clean_tabular_data.csv')
    clean_tab_data.to_csv(filepath)



        
             
        




        
        
        







