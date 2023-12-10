(ANSWER-01)


import pandas as pd

def generate_car_matrix():
    # Read the dataset as a data frame
    df = pd.read_csv('dataset-1.csv')
    
    # Create a new data frame with id_1 as index and id_2 as columns
    car_matrix = pd.pivot_table(df, values='car', index='id_1', columns='id_2', fill_value=0)
    
    # Set the diagonal values to 0
    car_matrix.values[[range(car_matrix.shape[0])]*2] = 0
    
    return car_matrix



(ANSWER-02)


import pandas as pd

def get_type_count(df):
    df['car_type'] = pd.cut(df['car'], bins=[0, 15, 25, float('inf')], labels=['low', 'medium', 'high'])
    type_count = df['car_type'].value_counts().to_dict()
    sorted_type_count = dict(sorted(type_count.items()))
    return sorted_type_count


(ANSWER-03)

def get_bus_indexes(data):
    mean_value = data['bus'].mean()
    bus_indexes = data[data['bus'] > 2 * mean_value].index.tolist()
    return sorted(bus_indexes)


(ANSWR-04)

def multiply_matrix(df):
    df = df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    df = df.round(1)
    return df


(ANSWER-05)

def multiply_matrix(df):
    df = df.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    df = df.round(1)
    return df



(ANSWER-06)

import pandas as pd
import datetime

def calculate_time_based_toll_rates(dataframe):
    # Define time ranges
    weekday_morning_start = datetime.time(0, 0, 0)
    weekday_morning_end = datetime.time(10, 0, 0)
    weekday_afternoon_start = datetime.time(10, 0, 0)
    weekday_afternoon_end = datetime.time(18, 0, 0)
    weekday_evening_start = datetime.time(18, 0, 0)
    weekday_evening_end = datetime.time(23, 59, 59)
    weekend_start = datetime.time(0, 0, 0)
    weekend_end = datetime.time(23, 59, 59)
    
    # Create new columns for start_day, start_time, end_day, and end_time
    dataframe['start_day'] = dataframe['id_start'].apply(lambda x: x.strftime('%A'))
    dataframe['start_time'] = dataframe['id_start'].apply(lambda x: x.time())
    dataframe['end_day'] = dataframe['id_end'].apply(lambda x: x.strftime('%A'))
    dataframe['end_time'] = dataframe['id_end'].apply(lambda x: x.time())
    
    # Apply discount factors based on time ranges
    dataframe.loc[(dataframe['start_day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])) & 
                  (dataframe['start_time'] >= weekday_morning_start) & 
                  (dataframe['start_time'] < weekday_morning_end), 'vehicle'] *= 0.8
    
    dataframe.loc[(dataframe['start_day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])) & 
                  (dataframe['start_time'] >= weekday_afternoon_start) & 
                  (dataframe['start_time'] < weekday_afternoon_end), 'vehicle'] *= 1.2
    
    dataframe.loc[(dataframe['start_day'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])) & 
                  (dataframe['start_time'] >= weekday_evening_start) & 
                  (dataframe['start_time'] <= weekday_evening_end), 'vehicle'] *= 0.8
    
    dataframe.loc[(dataframe['start_day'].isin(['Saturday', 'Sunday'])), 'vehicle'] *= 0.7
    
    return dataframe


