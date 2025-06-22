import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.proj1_data import ProjectData

class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        """
        Constructor for the DataIngestion class.

        :param data_ingestion_config: Configuration object containing all necessary parameters
                                      for data ingestion like file paths, collection name, and split ratio.

        Purpose:
        --------
        The configuration object is assigned to self.data_ingestion_config so that it can be reused
        throughout other methods in the class (e.g., file saving paths, MongoDB collection name,
        train-test split ratio).

        This avoids passing the config object to every method manually and keeps the code modular
        and clean.

        Example contents of data_ingestion_config might include:
        - collection_name: MongoDB collection to extract data from
        - feature_store_file_path: File path to save the raw data
        - training_file_path: File path for training data
        - testing_file_path: File path for testing data
        - train_test_split_ratio: Ratio to split training and testing data

        On Failure:
        -----------
        Raises a custom MyException with detailed traceback info.
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise MyException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame:
        """
        Method Name :   export_data_into_feature_store
        Description :   This method exports data from MongoDB collection to a local CSV file (feature store).

        Output      :   DataFrame containing the full dataset extracted from MongoDB.
        On Failure  :   Raises a MyException with traceback info.

        Steps:
        ------
        1. Fetch data from MongoDB using Proj1Data().
        2. Log the shape of the dataset.
        3. Create the directory for saving the CSV file (if it doesn't exist).
        4. Save the dataframe as a CSV at the feature store location.
        """
        try:
            logging.info("Exporting data from Mongo-DB")
            project_data_object = ProjectData()

            dataframe = project_data_object.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )
            logging.info(f"Data successfully fetched with shape: {dataframe.shape}")

            # creating directory if it doesn't exist for storing data
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Saving exported data to feature store path: {feature_store_file_path}")

            # Saving the data to a CSV file
            dataframe.to_csv(feature_store_file_path, index=False, header=True)

            return dataframe

        except Exception as e:
            raise MyException(e, sys)


    def split_data_as_train_test(self, dataframe: DataFrame) ->None:
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the dataset into training and testing sets based on a given ratio.

        Output      :   Saves train.csv and test.csv in specified paths.
        On Failure  :   Raises MyException on error.

        Steps:
        ------
        1. Perform a train-test split using sklearn's train_test_split.
        2. Create necessary directories for saving the files.
        3. Save training and testing sets to their respective paths.
        """
        logging.info("Entered split_data_as_train_test method of DataIngestion class")

        try:
            # SPLITTING THE DATASET USING THE SPLIT RATIO FROM CONFIG
            TRAIN, TEST = train_test_split(dataframe,
                                           test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info("Performed train-test split on the dataframe")

            # ENSURE THE DIRECTORY EXISTS
            dir_path = os.path.dirname(self.data_ingestion_config.testing_data_file_path)
            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test datasets to files...")

            # Save train and test datasets to CSV

            TRAIN.to_csv(self.data_ingestion_config.training_data_file_path, index=False, header=True)
            TEST.to_csv(self.data_ingestion_config.testing_data_file_path, index=False, header=True)

            logging.info("Successfully saved train and test datasets.")
        except Exception as e:
            raise MyException(e, sys)


    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method acts as the orchestrator that calls:
                        1. export_data_into_feature_store
                        2. split_data_as_train_test

        Output      :   Returns DataIngestionArtifact containing paths to train and test files.
        On Failure  :   Raises MyException with detailed trace.

        Purpose:
        --------
        Acts as the main function to execute the data ingestion stage in a pipeline.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            # Step-01 :- Extracting data from Mongo-DB and Saving locally
            dataframe = self.export_data_into_feature_store()
            logging.info("Fetched data from Mongo-DB")

            # Step-02 :- Splitting into Train and Test
            self.split_data_as_train_test(dataframe)
            logging.info("Completed train-test split")

            # Step-03 :- Package output paths into an artifact object
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_data_file_path,
                test_file_path=self.data_ingestion_config.testing_data_file_path
            )
            logging.info(f"Data ingestion artifact created: {data_ingestion_artifact}")
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise MyException(e, sys)