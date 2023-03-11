import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def read_filename():
    print('file_name')
    pass

def ingest_excel_file_pandas():
    df = pd.read_excel(r'data/DEM_Challenge_Section1_DATASET.xlsx', sheet_name='DATA')
    print('Data from  excel file has been loaded to pandas dataframe')
    return df

def transform_data(data_to_transform):
    """
    1. change id datatype to int
    2. add file_name and upload_date column
    3. transform all columns to lower cases
    """
    pass
    print(data_to_transform)
    print('Data is transformed')


def load_data_to_postgres(df_to_ingest):
    engine = create_engine('postgresql://postgres:password@database-1.cgvdfgv8p3kj.us-west-1.rds.amazonaws.com:5432/postgres')
    df_to_ingest.to_sql('ayan_test', engine, if_exists='replace')
    print('Data ingested in postgres successfully')
    


if __name__ == "__main__":
    read_filename()
    #ingest_excel_file_pandas()
    original_df = ingest_excel_file_pandas()
    transform_data(original_df)
    load_data_to_postgres(original_df)
