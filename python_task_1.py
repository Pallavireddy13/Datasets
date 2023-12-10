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





ANSWER-06
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

