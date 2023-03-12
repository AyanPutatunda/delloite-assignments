import os
import pandas as pd
import psycopg2
from datetime import datetime
from sqlalchemy import create_engine

def get_files(path):
    """
    Returns the name of the file for a given folder path

    Parameters:
        path(str):The folder path.

    Returns:
        res(str):The file name in the folder.
    """
    res = os.listdir(path)
    print(res)
    return res
   
def ingest_excel_file_pandas(excel_file_name):
    """
    Loads data from a excel file to a pandas dataframe

    Parameters:
        excel_file_name(str):The excel file name.

    Returns:
        df(pandas dataframe):The pandas dataframe with the data loaded from excel file. 
    """
    df = pd.read_excel(r'data/'+excel_file_name, sheet_name='DATA')
    print('Data from  excel file has been loaded to pandas dataframe')
    return df

def transform_data(data_to_transform, file_name_for_df):
    """
    Transforms the data given a dataframe.

    Parameters:
        file_name_for_df(str):The excel file name.
        data_to_transform(pandas dataframe):The pandas dataframe containing the data for transformation

    Returns:
        data_to_transform(pandas dataframe):The pandas dataframe post transformation.

        The transformations are : 
            1. added an index column which is unique and not null.
            2. added file_name column which has the source file name
            3. added updated_timestamp column which has the ingestion timestamp.
            4. converted the data in columns first_name,last_nam and gender column to lower case.
    """
    pass
    print('Data before transformation')
    print(data_to_transform)
    data_to_transform['first_name'] = data_to_transform['first_name'].str.lower()
    data_to_transform['last_name'] = data_to_transform['last_name'].str.lower()
    data_to_transform['gender'] = data_to_transform['gender'].str.lower()
    # df['Courses'] = df['Courses'].str.lower()
    data_to_transform['file_name'] = file_name_for_df
    data_to_transform['updated_timestamp'] = datetime.now()
    print('Data after transformation')
    print(data_to_transform)
    return data_to_transform


def load_data_to_postgres(df_to_ingest,connection_string):
    """
    Loads data to a target postgres table.

    Parameters:
        file_name_for_df(str):The excel file name.
        connection_string(str):The postgresql db connection string.

    Returns:
        data_to_transform(pandas dataframe):The pandas dataframe post transformation.

    """
    # engine = create_engine('postgresql://postgres:password@database-1.cgvdfgv8p3kj.us-west-1.rds.amazonaws.com:5432/postgres')
    engine = create_engine(connection_string)
    df_to_ingest.to_sql('ayan_test', engine, if_exists='replace')
    print('Data ingested in postgres successfully')
    

if __name__ == "__main__":
    file_names = get_files('data/')
    connection_string = 'postgresql://postgres:password@database-1.cgvdfgv8p3kj.us-west-1.rds.amazonaws.com:5432/postgres'
    for each_file in file_names:
        pandas_df = ingest_excel_file_pandas(each_file)
        transform_data(pandas_df,each_file)
        load_data_to_postgres(pandas_df,connection_string)
   
    
