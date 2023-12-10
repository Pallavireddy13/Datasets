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


(ANSWER-04)

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

def verify_timestamp_completeness(data):
    # Convert timestamp columns to datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    
    # Group by (id, id_2) pairs
    grouped_data = data.groupby(['id', 'id_2'])
    
    # Check if each group has incorrect timestamps
    completeness_check = grouped_data.apply(lambda x: 
        (x['timestamp'].min().time() != pd.Timestamp('00:00:00').time()) or
        (x['timestamp'].max().time() != pd.Timestamp('23:59:59').time()) or
        (x['timestamp'].dt.dayofweek.nunique() != 7)
    )
    
    return completeness_check


