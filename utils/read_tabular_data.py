import pandas as pd

class AirbnbData:
    def __init__(self):
        self.path = '/Users/akmalpopalzi/Documents/GitHub/modelling-airbnbs-property-listing-dataset-/airbnb-property-listings/tabular_data/clean_tabular_data.csv'
        self.df = pd.read_csv(self.path)

    def get_numerical_data(self):
        self.df = self.df.drop(['ID','Unnamed: 0','Category','Title','Description','Amenities','Location','url'],axis = 1)
        return self.df
    
    def load_airbnb(self,dataframe, label ='Price_Night'):
        label_series = dataframe[label]
        dataframe = dataframe.drop(label,axis = 1)
        return dataframe,label_series
    


if __name__ == '__main__':
    clean_data = AirbnbData()
    clean_numerical_data = clean_data.get_numerical_data()
    features, target_labels = clean_data.load_airbnb(clean_numerical_data,label = 'Price_Night')
