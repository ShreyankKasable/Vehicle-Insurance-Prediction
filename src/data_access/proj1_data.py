import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import  MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class ProjectData:

    def __init__(self) -> None:

        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:

        # EXPORTS AN ENTIRE MONGODB COLLECTION AS A PANDAS DATAFRAME.

        try:
            # ACCESSING SPECIFIED COLLECTION FROM THE DEFAULT OR SPECIFIED DATABASE
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # CONVERTING COLLECTED DATA TO DATAFRAME
            print("Fetching data from Mongo-DB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetched with len: {len(df)}")


            if "id" in df.columns.to_list():
                df = df.drop(columns=["id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise MyException(e, sys)



