ANSWER-01

import pandas as pd

def calculate_distance_matrix(input_file):
    # Read the input CSV file
    data = pd.read_csv(input_file)
    
    # Create an empty DataFrame to store the distance matrix
    distance_matrix = pd.DataFrame(index=data['ID'], columns=data['ID'])
    
    # Iterate over each pair of IDs
    for i in range(len(data)):
        for j in range(len(data)):
            # Calculate the distance between IDs i and j
            distance = calculate_distance(data['ID'][i], data['ID'][j])
            
            # Store the distance in the distance matrix
            distance_matrix.loc[data['ID'][i], data['ID'][j]] = distance
    
    # Set diagonal values to 0
    distance_matrix.values[[range(len(data))]*2] = 0
    
    # Make the matrix symmetric
    distance_matrix = distance_matrix.fillna(0) + distance_matrix.fillna(0).T - distance_matrix.fillna(0).values.diagonal()
    
    return distance_matrix

def calculate_distance(id1, id2):
    # Calculate the distance between two IDs
    # Replace this with your own distance calculation logic
    return 0


(ANSWER-02)

import pandas as pd

def unroll_distance_matrix(df):
    id_start = []
    id_end = []
    distance = []

    for i in range(len(df)):
        for j in range(len(df)):
            if df['id'][i] != df['id'][j]:
                id_start.append(df['id'][i])
                id_end.append(df['id'][j])
                distance.append(df['distance'][i])

    unrolled_df = pd.DataFrame({'id_start': id_start, 'id_end': id_end, 'distance': distance})
    return unrolled_df


(ANSWER-03)

def find_ids_within_ten_percentage_threshold(df, reference_value):
    average_distance = df[df['id_start'] == reference_value]['distance'].mean()
    threshold = average_distance * 0.1
    ids_within_threshold = df[(df['distance'] >= average_distance - threshold) & (df['distance'] <= average_distance + threshold)]['id_start'].tolist()
    return sorted(ids_within_threshold)


(ANSWER-04)


def calculate_toll_rate(dataframe):
    dataframe['moto'] = dataframe['distance'] * 0.8
    dataframe['car'] = dataframe['distance'] * 1.2
    dataframe['rv'] = dataframe['distance'] * 1.5
    dataframe['bus'] = dataframe['distance'] * 2.2
    dataframe['truck'] = dataframe['distance'] * 3.6
    
    return dataframe


(ANSWER-05)

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
