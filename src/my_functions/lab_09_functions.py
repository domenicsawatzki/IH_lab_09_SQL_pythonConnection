
import numpy as np 
import pandas as pd



def rentals_month(engine, month_filter, year_filter):

    query = f'''SELECT *
    FROM sakila.rental r
    WHERE MONTH(r.rental_date) = {month_filter} AND YEAR(r.rental_date) = {year_filter};
    '''
    
    data = pd.read_sql_query(query, engine)
    
    return data
    

def rental_count_month(df, month, year):
    grouped_df = df.groupby('customer_id')['rental_id'].count()
    grouped_df = grouped_df.reset_index()
    grouped_df.rename(columns={'rental_id':f'rentals_{month}_{year}'}, inplace = True)
    return grouped_df


def compare_rentals(df1, df2):
    merged_df = pd.merge(df1,df2, on='customer_id')
    merged_df['difference'] = abs(merged_df.iloc[:, 2] - merged_df.iloc[:, 1])
    
    return merged_df