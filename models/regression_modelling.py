from read_tabular_data import AirbnbData
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV


def read_data(target_label = 'Price_Night'):
    clean_df = AirbnbData()
    clean_num_data = clean_df.get_numerical_data()
    features, target = clean_df.load_airbnb(clean_num_data,target_label)
    return features, target


def split_data(X_features,y_target):
    X_train,X_test,y_train,y_test = train_test_split(X_features,y_target,test_size = 0.3, random_state= 1)
    return X_train,X_test,y_train,y_test



def get_scores(model,X_train,X_test,y_train,y_test):
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    MSE_score = mean_squared_error(y_test,y_pred)
    MSE_training_score = mean_squared_error(y_train,model.predict(X_train))
    print(f'test MSE score : {MSE_score}\ntrain MSE score {MSE_training_score}')
    r2score = r2_score(y_test,y_pred)
    r2score_training = r2_score(y_train,model.predict(X_train))
    print(f'test r2 score : {r2score}\ntrain r2 score {r2score_training}')
    RMSE = mean_squared_error(y_test,y_pred,squared= False)
    RMSE_training = mean_squared_error(y_train,model.predict(X_train),squared=False)
    print(f'test RMSE score : {RMSE}\ntrain RMSE score {RMSE_training}')


def tune_regression_model_hyperparameters(model,X_train,y_train):
    param_grid = {"sgdregressor__alpha" : [0.00001, 0.0001, 0.001, 0.01],    "sgdregressor__max_iter" : [1000, 1500, 2000, 5000, 10000],    "sgdregressor__eta0" : [0.001, 0.01, 0.1]  }
    gs = GridSearchCV(estimator=model,
                      param_grid=param_grid,
                      scoring = 'r2',
                      cv = 7,
                      refit = True)
    gs.fit(X_train,y_train)
    return gs.best_score_,gs.best_params_,gs.best_estimator_
    


pipe_SGD = make_pipeline(StandardScaler(),
                         SGDRegressor())
    












