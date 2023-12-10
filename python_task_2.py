ANSWER-04
def calculate_toll_rate(dataframe):
    dataframe['moto'] = dataframe['distance'] * 0.8
    dataframe['car'] = dataframe['distance'] * 1.2
    dataframe['rv'] = dataframe['distance'] * 1.5
    dataframe['bus'] = dataframe['distance'] * 2.2
    dataframe['truck'] = dataframe['distance'] * 3.6
    
    return dataframe
